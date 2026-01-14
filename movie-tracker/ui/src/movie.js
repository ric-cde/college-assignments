import Card from "react-bootstrap/Card"
import Button from "react-bootstrap/Button"
import ReactStars from "react-stars"
import { UsersContext } from "./contexts/Users"
import { useContext } from "react"
import { BsTrash } from "react-icons/bs"

// Component based on documentation example: https://react-bootstrap.netlify.app/components/cards/

export default function Movie({ movie, onSave, onDelete }) {
	const context = useContext(UsersContext)

	return (
		<Card
			className="shadow-lg p-3 mb-5 bg-white rounded mx-auto"
			bg="dark"
			style={{ width: "20rem" }}
		>
			<Card.Img
				variant="top"
				className="mx-auto"
				src="./movie_creation-black-18dp.svg"
				style={{ width: "4rem" }}
			/>
			<Card.Body>
				<ReactStars
					count={5}
					// onChange={ratingChanged}
					size={24}
					value={parseInt(movie.rating)}
					edit={false}
					activeColor="#008000"
				/>
				<Card.Title>
					{movie.title} <small>{movie.year}</small>
				</Card.Title>
				<Card.Text>
					<small>DIRECTOR:</small> {movie.director}
				</Card.Text>
				<small>GENRES:</small> {movie.genres}
				<Card.Text>
					<small>RUNTIME:</small> {movie.runtime}
				</Card.Text>
				{context.isLoggedIn && (
					<Button
						variant={movie.date ? "secondary" : "success "}
						onClick={() => onSave(movie._id)}
						disabled={movie.date && "disabled"}
					>
						{movie.date ? "Queued" : "Save to Queue"}
					</Button>
				)}
				{context.isLoggedIn && movie.date && (
					<Button
						variant="danger"
						className="float-right"
						onClick={() => onDelete(movie._id)}
					>
						<BsTrash />
					</Button>
				)}
			</Card.Body>
		</Card>
	)
}
