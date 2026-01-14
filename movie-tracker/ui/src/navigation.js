import { Component } from "react"
import Navbar from "react-bootstrap/Navbar"
// import Form from 'react-bootstrap/Form';
// import FormControl from 'react-bootstrap/FormControl';
import Button from "react-bootstrap/Button"
import Nav from "react-bootstrap/Nav"
import { Link } from "react-router-dom"
import { UsersContext } from "./contexts/Users"
import { useState } from "react"

function Search() {
	const [selectValue, setSelectValue] = useState("all")

	const handleChange = (e) => {
		setSelectValue(e.target.value)
	}

	return (
		<form className="form-inline" action="/search" method="GET">
			<label>
				<input
					name="query"
					id="SearchTerm"
					type="text"
					placeholder="Search"
					className="form-control mb-sm-2"
				/>
			</label>
			<label>
				<select
					value={selectValue}
					onChange={handleChange}
					name="filter"
					id="searchFilter"
					className="custom-select ml-2 mr-2 mb-sm-2"
				>
					<option value="all">All fields</option>
					<option value="director">Director</option>
					<option value="year">Year</option>
					<option value="genre">Genre</option>
				</select>
			</label>

			<button className="btn btn-outline-light mr-5 mb-2">Search</button>
		</form>
	)
}

class Navigation extends Component {
	static contextType = UsersContext

	render() {
		return (
			<>
				<Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
					<Navbar.Brand as={Link} to="/">
						Film Deck
					</Navbar.Brand>
					<Navbar.Toggle aria-controls="responsive-navbar-nav" />
					<Navbar.Collapse id="responsive-navbar-nav">
						<Nav className="mr-auto">
							<Nav.Link as={Link} to="/">
								Home
							</Nav.Link>
							{this.context.isLoggedIn && (
								<>
									<Nav.Link as={Link} to="/queue">
										Queue
									</Nav.Link>
									<Nav.Link as={Link} to="/profile">
										Profile
									</Nav.Link>
								</>
							)}
						</Nav>
						<Search />
						{!this.context.isLoggedIn && (
							<Nav>
								<Nav.Link as={Link} to="/login">
									Log in
								</Nav.Link>
								<Nav.Link as={Link} to="/register" eventKey={2}>
									Register
								</Nav.Link>
							</Nav>
						)}
						{this.context.isLoggedIn && (
							<Nav>
								<Button
									onClick={this.context.logUserOut}
									variant="secondary"
								>
									Log out
								</Button>
								{/* <Nav.Link as={Link} to="/logout">Log out</Nav.Link> */}
							</Nav>
						)}
					</Navbar.Collapse>
				</Navbar>
			</>
		)
	}
}

export default Navigation
