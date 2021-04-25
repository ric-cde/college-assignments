import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';



class App extends React.Component {
  constructor(props) {
    super(props);
  }

    
  render() {
    return (
    <div class="container">
      <div class="child">
      <p><a href={process.env.PUBLIC_URL + "/SYSARCHSEM220202021b-Cloud_Computing_Overview.pdf"}>Part 1: Presentation</a><br /><br /></p>
      <p><a href={process.env.PUBLIC_URL + "/SYSARCHASS220202021-RichardHerlihy_CA2-final.pdf"}>Part 2-4: Reports</a></p><br />
      <iframe src={process.env.PUBLIC_URL + "/SYSARCHSEM220202021b-Cloud_Computing_Overview.pdf"} width="1000px" height="800px"></iframe>
      <br /><br />
      <iframe src={process.env.PUBLIC_URL + "/SYSARCHASS220202021-RichardHerlihy_CA2-final.pdf"} width="1000px" height="800px"></iframe>
      </div>
    </div>
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
