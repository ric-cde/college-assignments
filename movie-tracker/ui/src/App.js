import React from "react"

import Container from "react-bootstrap/Container"
import Col from "react-bootstrap/Col"
import Row from "react-bootstrap/Row"
import Login from "./login"
import Register from "./register"
import Profile from "./profile"
import Search from "./search"
import Queue from "./queue"

import { BrowserRouter as Router, Switch, Route } from "react-router-dom"

//import Form from 'react-bootstrap/Form';
//import FormControl from 'react-bootstrap/FormControl';

//import { render } from 'react-dom';

import Navigation from "./navigation"
import Home from "./home"

import "./App.css"

export default class App extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			list: [],
		}
	}

	render() {
		return (
			<Router>
				<Container fluid="sm">
					<Row>
						<Col>
							<header>
								<Navigation />
							</header>
						</Col>
					</Row>
					<Row className="h-75">
						<Col>
							<Main />
						</Col>
					</Row>
				</Container>
			</Router>
		)
	}
}

// You can think of these components as "pages"
// in your app.

function Main() {
	return (
		<div className="d-flex h-100">
			<Switch>
				<Route exact path="/">
					<Home />
				</Route>
				<Route path="/queue">
					<Queue />
				</Route>
				<Route path="/profile">
					<Profile />
				</Route>
				<Route path="/login">
					<Login />
				</Route>
				<Route path="/register">
					<Register />
				</Route>
				<Route path="/search">
					<Search />
				</Route>
				<Route>
					<NotFound />
				</Route>
			</Switch>
		</div>
	)
}

function NotFound() {
	return (
		<div className="w-100 j-100">
			<h1 className="page-title">404: page not found.</h1>
			<div className="d-flex h-75 text-align-center">
				<p className="my-auto mx-auto ">
					This is not the page you are looking for. 🔦
				</p>
			</div>
		</div>
	)
}
