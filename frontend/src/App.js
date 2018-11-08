import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
      var testing = new Promise((resolve, reject) => {
          fetch("https://0.0.0:5000", {
              method: 'GET',
              headers: opts.additionalHeaders || {},
          })
              .then(res => res.json())
              .then(json => {console.log(json); resolve(json)})
              .catch(err => reject(err));
      });
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
            <p>{testing}</p>
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
