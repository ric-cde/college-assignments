const express = require("express")
const session = require("express-session")
const bodyParser = require("body-parser")
const path = require("path")
const flash = require("connect-flash")
const cors = require("cors") // Allows CORS in development. (I.e. different ports/proxying due to create-react-app)
const bcrypt = require("bcrypt")
const CSVToJSON = require("csvtojson")

const fileupload = require("express-fileupload")

const app = express()

// https://stackabuse.com/handling-cors-with-node-js/

const corsOptions = {
	origin: process.env.CORS_ORIGIN || "http://localhost:3000",
	optionsSuccessStatus: 200, // some legacy browsers (IE11, various SmartTVs) choke on 204
	credentials: true,
}

app.use(cors(corsOptions), fileupload())

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

// app.use(express.static("public"));
// app.use(bodyParser.urlencoded({ extended: false }));

app.use(
	session({
		secret: process.env.SESSION_SECRET || "movies",
		resave: false,
		saveUninitialized: true,
	})
)

// Login/registration & User class adapted from https://icodemag.com/how-to-build-a-login-register-app-with-the-mern-stack-part-2-setting-up-the-database/

const requireLoggedIn = (req, res, next) => {
	if (!req.session.user) {
		return res.status(403).end()
	}
	next()
}

const requireNotLoggedIn = (req, res, next) => {
	if (req.session.user) {
		return res.status(403).end()
	}
	next()
}

class User {
	async register(username, password, email, firstname, lastname) {
		let statusCode = 409

		try {
			const matchingUsers = await db
				.collection("users")
				.find({ username: username })
				.toArray()

			if (matchingUsers.length === 0) {
				const passwordHash = await bcrypt.hash(password, 10)
				const newUser = {
					username,
					password: passwordHash,
					email,
					firstname,
					lastname,
				}
				await db.collection("users").insertOne(newUser)

				statusCode = 201
			}
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return statusCode
	}

	async login(username, password) {
		let statusCode = 422
		let user = {}

		try {
			const users = await db
				.collection("users")
				.find({ username: username })
				.toArray()

			if (users.length > 0) {
				const passwordCheck = await bcrypt.compare(
					password,
					users[0].password
				)
				if (passwordCheck) {
					statusCode = 204
					user = users[0]
					// console.log(user);
				}
			}
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return { statusCode, user }
	}

	async getProfile(_id, username) {
		let statusCode = 422
		let user = {}
		try {
			const o_id = new ObjectId(_id)
			const users = await db
				.collection("users")
				.find({ _id: o_id })
				.toArray()
			user = users[0]
			statusCode = 200
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return { statusCode, user }
	}

	async updatePhoto(_id, photo) {
		let statusCode = 422
		let user = {}

		try {
			const o_id = new ObjectId(_id)
			const updateDoc = {
				$set: {
					photo: photo,
				},
			}
			await db.collection("users").updateOne({ _id: o_id }, updateDoc)

			user = await db.collection("users").findOne(o_id)
			statusCode = 200
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return { statusCode, user }
	}

	async updateProfile(_id, password, firstname, lastname) {
		let statusCode = 422
		let user = {}

		try {
			const o_id = new ObjectId(_id)
			const updateDoc = {
				$set: {
					firstname: firstname,
					lastname: lastname,
				},
			}
			await db.collection("users").updateOne({ _id: o_id }, updateDoc)
			if (password !== null && password !== "") {
				// console.log(password);
				const passwordHash = await bcrypt.hash(password, 10)
				// console.log(passwordHash);
				const updatePass = {
					$set: {
						password: passwordHash,
					},
				}
				await db
					.collection("users")
					.updateOne({ _id: o_id }, updatePass)
			}
			user = await db.collection("users").findOne(o_id)
			statusCode = 200
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return { statusCode, user }
	}

	async saveToQueue(_id, movie_id) {
		let statusCode = 422
		const user_id = _id
		const date = new Date()
		try {
			const res = await db
				.collection("queue")
				.insertOne({ user_id, movie_id, date })
			console.log(res)
			statusCode = 201
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return { statusCode }
	}

	async deleteFromQueue(_id, movie_id) {
		let statusCode = 422
		const user_id = _id
		const date = new Date()
		try {
			const res = await db
				.collection("queue")
				.deleteOne({ user_id, movie_id })
			console.log(res)
			statusCode = 204
		} catch (err) {
			console.log(err)
			statusCode = 500
		}

		return { statusCode }
	}

	async getQueue(_id) {
		let statusCode = 422
		const user_id = _id
		let queue
		try {
			queue = await db.collection("queue").find({ user_id }).toArray()

			const recommends = await db
				.collection("recommends")
				.find({})
				.toArray()

			let filteredQueue = []

			for (let i = 0; i < queue.length; i++) {
				for (let j = 0; j < recommends.length; j++) {
					if (recommends[j]._id == queue[i].movie_id) {
						recommends[j].date = queue[i].date
						const queueMovie = recommends[j]
						filteredQueue.push(queueMovie)
					}
				}
			}
			console.log(filteredQueue)
			queue = filteredQueue
			statusCode = 200
		} catch (err) {
			console.log(err)
			statusCode = 500
		}
		return { statusCode, queue }
	}

	async addRecommend({
		title,
		year,
		director,
		runtime,
		genres,
		rating,
		imdb,
	}) {
		let statusCode = 422
		try {
			const check = await db
				.collection("recommends")
				.countDocuments({ title, year })
			if (!check) {
				const res = await db.collection("recommends").insertOne({
					title,
					year,
					genres,
					director,
					runtime,
					rating,
					imdb,
				})
				console.log(res)
				statusCode = 201
			} else {
				statusCode = 409
			}
		} catch (err) {
			console.log(err)
			statusCode = 500
		}
		console.log(statusCode)
		return { statusCode }
	}
}

const user = new User()

const { MongoClient, ObjectId } = require("mongodb")
const db_url = process.env.MONGODB_URI || "mongodb://localhost/movie-tracker"
const db_name = process.env.MONGODB_DB_NAME // optional explicit DB name for Atlas
const port = process.env.PORT || 8081
let db

// Linking create-react-app to production build (source: https://dev.to/loujaybee/using-create-react-app-with-express)

app.use(express.static(path.join(__dirname, "ui/build")))

app.get("/", function (req, res) {
	res.sendFile(path.join(__dirname, "ui/build", "index.html"))
})

// app.use(express.static(path.join(__dirname, 'client/build'))); //(move react to client/build, etc.)

async function getRecommends(_id) {
	try {
		// If user logged in, return  queued movies with date field
		if (_id) {
			console.log(_id)
			let recommends = await db
				.collection("recommends")
				.find({})
				.toArray()
			const queue = await db
				.collection("queue")
				.find({ user_id: _id })
				.toArray()
			for (let i = 0; i < queue.length; i++) {
				for (let j = 0; j < recommends.length; j++) {
					if (recommends[j]._id == queue[i].movie_id) {
						recommends[j].date = queue[i].date
					}
				}
			}

			return recommends
		}
		// If user not logged in, return all
		else {
			const recommends = await db
				.collection("recommends")
				.find({})
				.toArray()
			// console.log('Recommends: ', recommends);
			return recommends
		}
	} catch (err) {
		console.log(err)
		throw new Error(err)
	}
}

app.get("/api/movies", (req, res) => {
	// res.send(recommended_list);
	let _id
	if (req.session.user) {
		_id = req.session.user._id
	}
	getRecommends(_id)
		.then((recommends) => {
			// console.log('Found recommends: ', recommends);
			if (!recommends || recommends.length == 0) {
				res.status(404)
				res.send("No movies found.")
			} else {
				res.send(recommends)
			}
		})
		.catch((err) => {
			res.status(500)
			res.send(err)
		})
})

app.post("/api/movies", requireLoggedIn, async (req, res) => {
	console.log(req.body)
	const result = await user.addRecommend(req.body)
	res.status(result.statusCode)
	res.json(result)
})

app.post("/register", requireNotLoggedIn, async (req, res) => {
	//console.log(req.body);
	const { username, password, email, firstname, lastname } = req.body
	const result = await user.register(
		username,
		password,
		email,
		firstname,
		lastname
	)
	res.status(result).end()
})

app.get("/api/currentUser", (req, res) => {
	req.session.user
		? res.json({ user: req.session.user })
		: res.json({ loggedIn: false })
})

app.get("/api/profile", requireLoggedIn, async (req, res) => {
	let { _id } = req.session.user
	const result = await user.getProfile(_id)
	res.status(result.statusCode)
	res.json(result)
})

app.put("/api/profile/update", requireLoggedIn, async (req, res) => {
	const { password, firstname, lastname } = req.body
	let { _id } = req.session.user
	const result = await user.updateProfile(_id, password, firstname, lastname)
	res.status(result.statusCode)
	res.json(result)
})

app.get("/api/movies/queue", requireLoggedIn, async (req, res) => {
	const { _id } = req.session.user
	const result = await user.getQueue(_id)
	res.status(result.statusCode)
	res.json(result)
})

app.post("/api/movies/queue", requireLoggedIn, async (req, res) => {
	const movie_id = req.body._id
	const { _id } = req.session.user
	const result = await user.saveToQueue(_id, movie_id)
	res.status(result.statusCode)
	res.json(result)
})

app.delete("/api/movies/queue", requireLoggedIn, async (req, res) => {
	const movie_id = req.body._id
	const { _id } = req.session.user
	const result = await user.deleteFromQueue(_id, movie_id)
	res.status(result.statusCode)
	res.json(result)
})

// Pattern from https://flaviocopes.com/how-to-handle-file-uploads-node/
app.put("/api/profile/update/photo", requireLoggedIn, async (req, res) => {
	const { photo } = req.files
	let { _id } = req.session.user
	const result = await user.updatePhoto(_id, photo)
	res.status(result.statusCode)
	res.json(result)
})

app.post("/login", requireNotLoggedIn, async (req, res) => {
	const { username, password } = req.body
	const {
		statusCode,
		user: { _id, email },
	} = await user.login(username, password)

	const loggedInUser = { _id, username, email }

	if (statusCode === 204) {
		req.session.user = loggedInUser
	}

	res.json({ user: loggedInUser, statusCode })
})

app.post("/logout", requireLoggedIn, function (req, res) {
	req.session.destroy(() => {
		res.status(200)
		res.redirect("/login")
	})
	// req.logout();
	// res.redirect('/');
})

// Database connection pattern adapted from Pro MERN Stack 2

async function connectToDb() {
	console.log("Connecting to database...")
	const client = new MongoClient(db_url, {
		useNewUrlParser: true,
		useUnifiedTopology: true,
	})
	try {
		await client.connect()
		console.log("Connected to MongoDB at ", db_url)
		db = db_name ? client.db(db_name) : client.db()
	} catch (err) {
		console.log(err)
	}
}

// Auto-seed database if empty (for demo deployments without shell access)
async function autoSeedIfEmpty() {
	if (!db) {
		console.log("Database not connected, skipping auto-seed.")
		return
	}
	const count = await db.collection("recommends").countDocuments()
	if (count > 0) {
		console.log(`Database already has ${count} movies, skipping seed.`)
		return
	}
	console.log("Database is empty, auto-seeding...")

	// Load movies from CSV
	const csvPath = path.join(__dirname, "ratings.csv")
	const movies = await CSVToJSON().fromFile(csvPath)
	await db.collection("recommends").insertMany(movies)
	console.log(`Inserted ${movies.length} movies.`)

	// Create queue index
	await db.collection("queue").createIndex({ user_id: 1, movie_id: 1 }, { unique: true })

	// Create demo user if not exists
	const existing = await db.collection("users").findOne({ username: "demo" })
	if (!existing) {
		await db.collection("users").insertOne({
			username: "demo",
			email: "demo@example.com",
			firstname: "Demo",
			lastname: "User",
			password: await bcrypt.hash("demo1234", 10),
		})
		console.log("Created demo user (demo/demo1234)")
	}
}

;(async () => {
	try {
		await connectToDb()
		await autoSeedIfEmpty()
		app.listen(port, () => {
			console.log(`App started on http://localhost:${port}`)
		})
	} catch (err) {
		console.log("ERROR: ", err)
	}
})()

// This extra route fixes an error in the build version

app.get("*", function (req, res) {
	res.sendFile(path.join(__dirname, "ui/build", "index.html"))
})
