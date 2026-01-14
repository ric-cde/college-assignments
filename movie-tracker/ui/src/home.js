import { useEffect, useState } from 'react';
import Movie from './movie';
import AddMovie from './addmovie';
// import CardColumns from 'react-bootstrap/CardColumns'

export default function Home() {
    return (
      <div className="w-100">
        <h1 className="page-title bg-success">Home</h1>
        <br />
        <Recommended />
      </div>
    );
  }
  
  function Recommended() {
    
    const [movies, setMovies] = useState();
    
    useEffect(() => {
        fetchMovies();
    }, []);

    const fetchMovies = () => {
      const url = "/api/movies";
            try {
                fetch(url)
                  .then((res) => res.json())
                  .then((movies) => {
                      setMovies(movies);
                  });
            } catch(error) {
                alert(`Error in fetching data from server: ${error.message}`);
            }
    }

    const handleSave = async (_id) => {
      // console.log(_id);
      const url = "/api/movies/queue";
            
      await fetch(url, { // OR http://localhost:8081/register)
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify({ _id }),
      });

      fetchMovies(movies);
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

      fetchMovies(movies);
    }


    let moviesReady;  // Pattern adapted from this solution: https://www.debuggr.io/react-map-of-undefined/
    if (movies) {
        moviesReady = movies.map((movie) => {
            return (<Movie key={movie._id} movie={movie} onSave={ () => handleSave(movie._id) }  onDelete={ () => handleDelete(movie._id) }/>)
        });
     } else {
        moviesReady = "Loading..."
     }

     return (
         <>
         <div className="">
            <h2 className="float-left">Recommended Movies</h2>
            <AddMovie /><br /><br /><br />
         </div>
         <div className="d-flex w-100 justify-content-between flex-wrap">{moviesReady}</div>
         </>
     )
  }

