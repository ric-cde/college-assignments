import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';


class Results extends React.Component {

  render() {
    let pageResults = JSON.parse(this.props.pageResults);
    console.log(pageResults);
    return (
      <div className="App container text-light">
        <header className="App-header row">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>&nbsp;Hacker News</h2>
        </header>

        <div className="row">
            <table className="table table-light text-dark">
                <thead className="thead-dark">
                    <tr>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Comments</th>
                        <th>Points</th>
                    </tr>
                </thead>
                <tbody id="user-table">
                  {/* Adapated from: https://www.pluralsight.com/guides/how-to-display-key-and-value-pairs-from-json-in-reactjs */}
                    
                      { pageResults.map(obj => {
                        return (
                          <tr>
                            <td className="text-left"><a href={obj.url} target="_blank">{obj.title}</a></td>
                            <td>{obj.author}</td>
                            <td>{obj.num_comments}</td>
                            <td>{obj.points}</td>
                        </tr>
                        )
                      }
                      ) }
    
                </tbody>
            </table>
        </div>

        <div className="row justify-content-center">
            <button className="btn btn-primary" onClick={this.props.onClick }>More</button>
        </div>
        <br />
      </div>
    );
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    
    // Code for fetching API data & storing at as this.state = {}
    this.state= {
      pageResults: [],
      currentPage: 0,
    }
    let fetchUrl = 'https://hn.algolia.com/api/v1/search?query=redux&page='
    fetch(fetchUrl)
    .then(response => response.json()
    .then(data => {
      // console.log(data);
      this.setState({'pageResults': data.hits, 'currentPage': parseInt(data.page)});
    }
    )
    );
  }

  handleClick() {
    console.log("click");
    let newPage = parseInt(this.state.currentPage) + 1;
    console.log(newPage);
    this.setState({'currentPage': newPage});
    let fetchUrl = 'https://hn.algolia.com/api/v1/search?query=redux&page=' + newPage
    fetch(fetchUrl)
    .then(response => response.json()
    .then(data => {
      // console.log(data);
      this.setState({'pageResults': data.hits, 'currentPage': newPage});
    }
    )
    );
    console.log(this.state.currentPage);
    window.scrollTo(0, 0);
  }
    
  render() {
    return (
      <Results pageResults={JSON.stringify(this.state.pageResults)} currentPage={this.state.currentPage}
      onClick = {() => this.handleClick()} />
    )
  }
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
