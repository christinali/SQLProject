import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Timeline from './scenes/Timeline';
import Login from './scenes/Login';
import GetInfo from './scenes/GetInfo';
import Header from './scenes/Header';
import Input from './scenes/forms/Input';

import './styles/login.css';


class App extends Component {
  state = {screen: 2}

  render() {
    return (
        <div>
            <Header headerText='Froz is a frontend legend'/>
            {(()=> {
              switch(this.state.screen) {
                case 0:
                  return <Login
                            login={() => this.setState({screen: 1})}
                            signup={() => this.setState({screen: 2})}
                          />;
                case 1:
                  return <GetInfo logout={() => this.setState({screen: 0})}/>;
                case 2:
                  return <Input exitToLogin={() => this.setState({screen: 0})}/>;
                default:
                  return null;
              }
            })()}
        </div>
    );
  }
}

export default App;
