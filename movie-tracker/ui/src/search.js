// import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import Movie from './movie';
import CardColumns from 'react-bootstrap/CardColumns'


export default function Search () {

    const [movies, setMovies] = useState();
    const [resultFilter, setResultFilter] = useState("");

    const query = new URLSearchParams(window.location.search);
    const params = query.get('query').toLowerCase();
    const filter = query.get('filter').toLowerCase();

    const handleInputChange = (e) => {
        setResultFilter(e.target.value);
        // console.log(resultFilter);
    }

    useEffect(() => {
        const url = "/api/movies";
            try {
                fetch(url)
                  .then((res) => res.json())
                  .then((movies) => {
                      //console.log(movies);
                      setMovies(movies);
                  });
                // const url = `https://api.themoviedb.org/3/search/movie?api_key=ce5cdf8c01a58db19bd62357b0a9e55f&language=en-US&query=jurassic&page=1&include_adult=false`;
            } catch(error) {
                alert(`Error in fetching data from server: ${error.message}`);
            }
    }, []);

    let moviesReady;  
    if (movies) {
        const moviesFiltered = movies.filter((movie) => 
            movie.title.toLowerCase().includes(resultFilter) || 
            movie.genres.toLowerCase().includes(resultFilter) ||
            movie.director.toLowerCase().includes(resultFilter) ||
            movie.year.toLowerCase().includes(resultFilter)
        );
        //console.log(moviesFiltered);
        if (filter === "all") {
            moviesReady = moviesFiltered.filter((movie) => 
                movie.title.toLowerCase().includes(params) || 
                movie.genres.toLowerCase().includes(params) ||
                movie.director.toLowerCase().includes(params)
            )
            .map((movie) => {
                return (<Movie key={movie.imdb} movie={movie} />)
            });
        } else if (filter === "director") {
            moviesReady = moviesFiltered.filter((movie) => 
                movie.director.toLowerCase().includes(params)
                )
            .map((movie) => {
                return (<Movie key={movie.imdb} movie={movie} />)
            });
        } else if (filter === "year") {
            moviesReady = moviesFiltered.filter((movie) => 
                movie.year.toLowerCase().includes(params)
                )
            .map((movie) => {
                return (<Movie key={movie.imdb} movie={movie} />)
            });
        } else if (filter === "genre") {
            moviesReady = moviesFiltered.filter((movie) => 
                movie.genres.toLowerCase().includes(params)
                )
            .map((movie) => {
                return (<Movie key={movie.imdb} movie={movie} />)
            });
        }
     } else {
        moviesReady = "Loading..."
     }

    return (
        <>
        <div className="w-100 h-100">
                <h1 className="page-title bg-success">Search</h1>
                <br />
                <div className="mb-5">
                    <p className="h4 text-left d-inline"><span className="capitalise"></span>
                        Search results matching { filter === "all" ? filter + " fields" : filter } for "{ params }": </p>
                    <div className="d-inline">
                        <input className="float-right" name="resultfilter" placeholder="Filter results" onInput={handleInputChange}></input>
                    </div>
                </div>
                <CardColumns className="w-100">{moviesReady}</CardColumns>

        </div>
        </>
        )
}


// function filterField (field) {
//     return movie.title.toLowerCase().includes(params)
// }