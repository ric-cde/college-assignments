import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';
import presentation from './static/SYSARCHSEM220202021b-Cloud_Computing_Overview.pdf';
import report from './static/SYSARCHASS220202021-RichardHerlihy_CA2-final.pdf';


class App extends React.Component {
  constructor(props) {
    super(props);
  }

    
  render() {
    return (
    <div class="container">
      <div class="child">
      <p>{process.env.PUBLIC_URL}</p>
      <p><a href={presentation}>Part 1: Presentation</a><br /><br /></p>
      <p><a href={report}>Part 2-4: Reports</a></p><br />
      <iframe src={presentation} width="1000px" height="800px"></iframe>
      <br /><br />
      <iframe src={report} width="1000px" height="800px"></iframe>
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
