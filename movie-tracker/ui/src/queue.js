import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/button';
import ReactStars from "react-stars";
import { BsTrash } from "react-icons/bs";
import { Redirect } from 'react-router-dom';
import { UsersContext } from './contexts/Users';
import { Component } from 'react';


class Queue extends Component {
    static contextType = UsersContext;

    render() {
        return (
            <div className="w-100">
                <h1 className="page-title bg-success">Queue</h1>
                <br />
                <QueueList context={this.context} />
            </div>
        );
    }
  }


function QueueList(props) {

    const [movies, setMovies] = useState();

    useEffect(() => {
        fetchQueue();
    }, []);

    const fetchQueue = () => {
        const url = "/api/movies/queue";
            try {
                fetch(url)
                    .then((res) => res.json())
                    .then((movies) => {
                        // console.log(movies);
                        setMovies(movies.queue);
                    });
            } catch(error) {
                alert(`Error in fetching data from server: ${error.message}`);
            }
    }

    const handleDelete = async (_id) => {
        // console.log(_id);
        const url = "/api/movies/queue";
            
        await fetch(url, { // OR http://localhost:8081/register)
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        method: 'DELETE',
        body: JSON.stringify({ _id }),
        });

        fetchQueue(movies);
    }

    const formatDate = (date) => {
        const formattedDate = new Date (date)
        // console.log(formattedDate);
        const output = formattedDate.getDate() + 
            " " + formattedDate.toLocaleString('default', { month: 'short'}) + 
            " " + formattedDate.toLocaleString('default', { year: 'numeric'});
        // console.log(output);
        return output;
    }

    let moviesReady;  // Pattern adapted from this solution: https://www.debuggr.io/react-map-of-undefined/
    if (movies) {
        // console.log(movies);
        moviesReady = movies.map((movie) => {
            return (
            <tr key={movie._id}>
                <td>{movie.title}</td>
                <td>{movie.year}</td>
                <td>{movie.director}</td>
                <td className=".d-sm-none .d-md-block">{movie.genres}</td>
                <td>{formatDate(movie.date)}</td>
                <td><ReactStars
                        count={5}
                        // onChange={ratingChanged}
                        size={24}
                        value={parseInt(movie.rating)}
                        edit={false}
                        activeColor="#008000"
                    /></td>
                <td><Button 
                        variant="danger" 
                        className="float-right" 
                        onClick={() => handleDelete(movie._id)}
                    >
                        <BsTrash />
                    </Button>
                </td>
            </tr>
            )
        });
    } else {
        moviesReady = "Loading..."
    }
    
    if (props.context.isLoggedIn) {
    return (
        <>
        <div className="">
            <h3 className="float-left">There are currently { movies ? movies.length : 0 } items in your queue.</h3>
            <br /><br /><br />
        </div>
        <table className="table table-light text-dark">
                <thead className="thead-dark">
                    <tr>
                        <th>Title</th>
                        <th>Year</th>
                        <th>Director</th>
                        <th className=".d-sm-none .d-md-block">Genres</th>
                        <th>Added</th>
                        <th>Rating</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody id="user-table">
                    {moviesReady}    
                </tbody>
            </table>
        </>
        )
    }
    return <Redirect to="/" />;
}

  export default Queue;