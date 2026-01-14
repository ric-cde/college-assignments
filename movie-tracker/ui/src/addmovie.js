import { useState } from "react"
import Button from "react-bootstrap/Button"
import Modal from "react-bootstrap/Modal"
import { UsersContext } from "./contexts/Users"
import { useContext } from "react"
import Form from "react-bootstrap/Form"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import SweetAlert from "sweetalert-react"
import "sweetalert/dist/sweetalert.css"

import "bootstrap/dist/css/bootstrap.css"
import ReactStars from "react-stars"

// adapted from this tutorial: https://www.pluralsight.com/guides/how-to-open-and-close-react-bootstrap-modal-programmatically

export default function AddMovie() {
	const [show, setShow] = useState(false)
	const [rating, ratingChanged] = useState(0)
	const [showAlert, setAlert] = useState(false)
	const [alertDetails, setDetails] = useState({ title: "", text: "" })

	const handleClose = () => setShow(false)
	const handleShow = () => setShow(true)

	const handleAdd = async (event) => {
		event.preventDefault()
		console.log(event)
		let formData = new FormData(event.target)
		formData.append("rating", rating)
		console.log(formData)
		const result = await fetch("/api/movies", {
			credentials: "include",
			method: "POST",
			body: formData,
		})
		let title
		let text
		console.log(result.statusCode)
		if (result.status === 201) {
			title = "Done"
			text = "Movie successfully added."
		} else if (result.status === 409) {
			title = "Doh"
			text = "That movie/year combination already exists."
		} else {
			title = "Whoops!!"
			text = "Something went wrong."
		}
		setDetails({ title, text })
		setAlert(true)
		// handleClose();
	}
	const context = useContext(UsersContext)

	return (
		<>
			{context.isLoggedIn && (
				<Button
					variant="primary"
					size="md"
					onClick={handleShow}
					className="float-right mb-4"
				>
					Add new recommendation
				</Button>
			)}

			<SweetAlert
				show={showAlert}
				title={alertDetails.title}
				text={alertDetails.text}
				onConfirm={() => setAlert(false)}
			/>

			<Modal show={show} onHide={handleClose} centered>
				<Modal.Header closeButton>
					<Modal.Title>Add new movie recommendation</Modal.Title>
				</Modal.Header>
				<Modal.Body>
					<p className="text-secondary">
						This movie will be visible to all users.
					</p>
					<form onSubmit={handleAdd}>
						<Form.Group as={Row} controlId="movieTitle">
							<Form.Label column sm="2">
								Title
							</Form.Label>
							<Col sm="10">
								<Form.Control
									name="title"
									type="text"
									placeholder="Movie name"
									required
								/>
							</Col>
						</Form.Group>

						<Form.Group as={Row} controlId="movieYear">
							<Form.Label column sm="2">
								Year
							</Form.Label>
							<Col sm="10">
								<Form.Control
									name="year"
									type="number"
									placeholder="Release (YYYY)"
									pattern="[0-9]{4}"
									required
								/>
							</Col>
						</Form.Group>

						<Form.Group as={Row} controlId="movieRating">
							<Form.Label column sm="2">
								Rating
							</Form.Label>
							<Col sm="10">
								<ReactStars
									count={5}
									// onChange={ratingChanged}
									name="rating"
									size={24}
									edit={true}
									onChange={ratingChanged}
									activeColor="#008000"
									required
									className="mb-2"
								/>
							</Col>
						</Form.Group>

						<Form.Group as={Row} controlId="movieDirector">
							<Form.Label column sm="2">
								Director
							</Form.Label>
							<Col sm="10">
								<Form.Control
									name="director"
									type="text"
									placeholder="Film director(s)"
									required
								/>
							</Col>
						</Form.Group>

						<Form.Group as={Row} controlId="movieRuntime">
							<Form.Label column sm="2">
								Runtime (minutes)
							</Form.Label>
							<Col sm="10">
								<Form.Control
									name="runtime"
									type="number"
									placeholder="E.g. 120"
									required
								/>
							</Col>
						</Form.Group>

						<Form.Group as={Row} controlId="movieGenres">
							<Form.Label column sm="2">
								Genres
							</Form.Label>
							<Col sm="10">
								<Form.Control
									name="genres"
									type="text"
									placeholder="E.g. Comedy, Drama"
									required
								/>
							</Col>
						</Form.Group>

						<Form.Group as={Row} controlId="movieIMDb">
							<Form.Label column sm="2">
								IMDb URL
							</Form.Label>
							<Col sm="10">
								<Form.Control
									name="imdb"
									type="url"
									placeholder="Optional"
								/>
							</Col>
						</Form.Group>

						<button className="btn btn-primary btn-block">
							Add recommendation
						</button>
					</form>
				</Modal.Body>
				<Modal.Footer>
					<Button variant="secondary" onClick={handleClose}>
						Close
					</Button>
				</Modal.Footer>
			</Modal>
		</>
	)
}
