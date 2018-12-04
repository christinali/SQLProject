import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Timeline from './scenes/Timeline';
import Login from './scenes/Login';
import GetInfo from './scenes/GetInfo';

class App extends Component {
    state = {login: false}


  render() {
    return (
        <div>
            {this.state.login && <button onClick={() => this.setState({login: false})}>Log out</button>}
            {this.state.login ? <GetInfo/> : <Login login={() => this.setState({login: true})}/>}
        </div>
    );
  }
}

export default App;
