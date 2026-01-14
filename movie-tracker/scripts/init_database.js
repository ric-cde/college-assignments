const { MongoClient } = require("mongodb")
const bcrypt = require("bcrypt")
const path = require("path")
const CSVToJSON = require("csvtojson")

const db_url = process.env.MONGODB_URI || "mongodb://localhost/movie-tracker"
let db
let client

async function readCsv() {
	const csvPath = path.join(__dirname, "..", "ratings.csv")
	return CSVToJSON().fromFile(csvPath)
}

async function connectToDb() {
	console.log("Connecting to database...")
	client = new MongoClient(db_url, {
		useNewUrlParser: true,
		useUnifiedTopology: true,
	})
	try {
		await client.connect()
		console.log("Connected to MongoDB at ", db_url)
		db = client.db()
	} catch (err) {
		console.log(err)
		throw err
	}
}

;(async () => {
	try {
		const movies = await readCsv()
		await connectToDb()

		// remove any existing recommends (movie) or queue records
		await db.collection("recommends").deleteMany({})
		await db.collection("queue").deleteMany({})

		// add converted CSV data
		await db.collection("recommends").insertMany(movies)
		const count = await db.collection("recommends").countDocuments()
		console.log("Inserted", count, "movies to the recommends collection")

		const result = await db
			.collection("queue")
			.createIndex({ user_id: 1, movie_id: 1 }, { unique: true })
		console.log(`Index created: ${result}`)

		// Create a default demo user if not present
		const demoUser = {
			username: "demo",
			email: "demo@example.com",
			firstname: "Demo",
			lastname: "User",
			password: await bcrypt.hash("demo1234", 10),
		}
		const existing = await db
			.collection("users")
			.findOne({ username: demoUser.username })
		if (!existing) {
			await db.collection("users").insertOne(demoUser)
			console.log("Created default user: demo / demo1234")
		} else {
			console.log("Default user already exists")
		}

		console.log("Closing connection...")
		await client.close()
	} catch (err) {
		console.log("ERROR: ", err)
		if (client) {
			await client.close()
		}
		process.exit(1)
	}
})()

// setTimeout(() => {
//     db.collection('recommends').insertMany(recommended_list[0]);
// },3000)

// db.recommends.createIndex({ imdb: 1 }, { unique: true});
// db.recommends.createIndex({ year: 1 });
// db.recommends.createIndex({ runtime: 1 });
// db.recommends.createIndex({ director: 1 });
