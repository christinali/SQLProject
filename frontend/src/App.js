import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Timeline from './scenes/Timeline';
import Login from './scenes/Login';
import GetInfo from './scenes/GetInfo';
import Header from './scenes/Header';
import './styles/login.css';


class App extends Component {
  state = {screen: 0}


  render() {
    return (
        <div>
            <Header headerText='Froz is a frontend legend'/>
            {(()=> {
              switch(this.state.screen) {
                case 0:
                  return <Login login={() => this.setState({screen: 1})}/>;
                case 1:
                  return <GetInfo logout={() => this.setState({screen: 0})}/>;
                default:
                  return null;
              }
            })()}
        </div>
    );
  }
}

export default App;
