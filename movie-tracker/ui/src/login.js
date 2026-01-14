import Card from "react-bootstrap/Card"
import { UsersContext } from "./contexts/Users"
import { Component } from "react"
import { Redirect } from "react-router-dom"
import SweetAlert from "sweetalert-react"
import "sweetalert/dist/sweetalert.css"

// form adapted from https://getbootstrap.com/docs/4.0/components/forms/

class Login extends Component {
	static contextType = UsersContext

	// state & form handling methods adapted from https://icodemag.com/how-to-build-a-login-register-app-with-the-mern-stack-part-4-setting-up-frontend-routes/

	state = {
		username: "",
		password: "",
		alert: {
			showAlert: false,
			title: "",
			text: "",
		},
	}

	handleFormSubmit = async (e) => {
		e.preventDefault()
		const { username, password } = this.state
		const { title, text } = await this.context.logUserIn(username, password)

		// alert(`${title} ${text}`);

		this.setState({
			alert: {
				showAlert: true,
				title,
				text,
			},
		})
	}

	handleInputChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value,
		})
	}

	render() {
		if (!this.context.isLoggedIn) {
			const { showAlert, title, text } = this.state.alert

			return (
				<div className="w-100 h-100">
					<SweetAlert
						show={showAlert}
						title={title}
						text={text}
						onConfirm={() =>
							this.setState({ alert: { showAlert: false } })
						}
					/>
					<h1 className="page-title bg-success">Login</h1>
					<div className="d-flex h-75">
						<Card className="my-auto mx-auto shadow-lg p-3 mb-5 bg-white rounded">
							<Card.Body>
								<form onSubmit={this.handleFormSubmit}>
									{" "}
									{/* action="/login" method="post" */}
									<div className="form-group">
										<label htmlFor="InputUsername">
											Username:
										</label>
										<input
											type="text"
											className="form-control"
											id="InputUsername"
											aria-describedby="inputHelp"
											name="username"
											placeholder="Enter username"
											autoComplete="username"
											value={this.state.username}
											onChange={this.handleInputChange}
											required
										/>
										{/* <small id="inputHelp" className="form-text text-muted"></small> */}
									</div>
									<div className="form-group">
										<label htmlFor="InputPassword">
											Password:
										</label>
										<input
											type="password"
											className="form-control"
											id="InputPassword"
											name="password"
											placeholder="Enter a password"
											autoComplete="current-password"
											value={this.state.password}
											onChange={this.handleInputChange}
											required
										/>
									</div>
									<button
										type="submit"
										className="btn btn-primary"
									>
										Log in
									</button>
								</form>
							</Card.Body>
						</Card>
					</div>
				</div>
			)
		}

		return <Redirect to="/" />
	}
}

export default Login
