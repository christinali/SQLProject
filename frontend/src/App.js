import React, { Component } from 'react';
import logo from './logo.svg';
import Timeline from './scenes/Timeline';
import Login from './scenes/Login';
import GetInfo from './scenes/GetInfo';
import Header from './scenes/Header';
import Input from './scenes/forms/Input';
import firebase from 'firebase';
import Background from './images/background_image.jpg';
import Class from './scenes/Class';
import Prof from './scenes/Prof';

import './App.css';
import './styles/login.css';
import './styles/getInfo.css';
import './styles/Prof.css';

const firebaseConfig = {
    apiKey: "AIzaSyDfXgvgX2_eyPam6O3eenzLTJHrwHc2tdc",
    authDomain: "sqlproject-b318c.firebaseapp.com",
    databaseURL: "https://sqlproject-b318c.firebaseio.com",
    projectId: "sqlproject-b318c",
    storageBucket: "sqlproject-b318c.appspot.com",
    messagingSenderId: "612693141535"
};

var sectionStyle = {

  backgroundImage: `url(${Background})`
};

class App extends Component {
  constructor(props){
    super(props);
    this.app = firebase.initializeApp(firebaseConfig);
  }

  //0 = Login
  //1 = Home
  //2 = Sign Up
  //3 = ClassInfo
  //4 = ProfInfo
  state = {screen:1, email: '', currProf: null, headerText: 'MISTAAAAAH MOHIIIIPPPPPPEEEENNNNNNNN is a frontend legend'}

  render() {
    return (
        <div>
            <Header headerText={this.state.headerText} logout={() => this.setState({screen:0})} loggedin={this.state.screen}/>
            {(()=> {
              switch(this.state.screen) {
                case 0:
                  return <Login
                            login={(email) => this.setState({screen: 1, email: email, headerText: "Welcome " + email + "!"})}
                            signup={() => this.setState({screen: 2})}
                            app={this.app}
                          />;
                case 1:
                  return <GetInfo
                          email={this.state.email}
                          changeProf={prof => this.setState({screen: 4, currProf: prof})}
                          logout={() => this.setState({screen: 0})}/>;
                case 2:
                  return <Input
                            exitToLogin={() => this.setState({screen: 0})}
                            app={this.app}
                            />;
                case 3:
                  return <Class />;
                case 4:
                  return <Prof
                          id={this.state.currProf}

                  />;

                default:
                  return null;
              }
            })()}
        </div>
    );
  }
}

export default App;
