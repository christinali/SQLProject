import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Timeline from './scenes/Timeline';
import Login from './scenes/Login';

class App extends Component {
    state = {login: false}


  render() {
    return (
        <div>
            {this.state.login && <button style={{position: 'fixed', left: 0, top: 0}} onClick={() => this.setState({login: false})}>Log out</button>}
            {this.state.login ? <Timeline/> : <Login login={() => this.setState({login: true})}/>}
        </div>
    );
  }
}

export default App;
