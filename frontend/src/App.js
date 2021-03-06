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
import AllRecs from './scenes/AllRecs';
import AdvSearch from './scenes/AdvSearch';
import axios from 'axios';
import Me from './scenes/Me'
import './styles/app.css';
import './styles/login.css';
import './styles/getInfo.css';
import './styles/ProfClass.css';
import './styles/AllRecs.css';
import './styles/AdvSearch.css';

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
    // console.log("STARTING");
    // axios.post('http://localhost:5000/add-class?user_id=1006&dept=COMPSCI&class_num=201&semester=2013 Fall Term&star_number=1&difficulty=1&comment=1006 Here is a long comment that I input from App.js')
    //     .then(res => {
    //         console.log(res.data);
    //     })
    //     .catch(e => console.log(e))
    this.app = firebase.initializeApp(firebaseConfig);
  }

  //0 = Login
  //1 = Home
  //2 = Sign Up
  //3 = ClassInfo
  //4 = ProfInfo
  //5 = All Recs
  //6 = Adv Search
  state = {screen:0, email: '', currProf: 0, currClass: 0, headerText: 'The Bookbaggregator'}

  render() {
    if (this.state.screen == 0 || this.state.screen == 2) {
      var name = 'main0';
    }
    else {
      var name = 'lmao';
    }

    return (
        <div className={name}>
            <Header headerText={this.state.headerText}
              advanceSearchPage={() => this.setState({screen:6})} loggedin={this.state.screen}
              logout={() => this.setState({screen:0, email: '', currProf: 0, currClass: 0, headerText: 'The Bookbaggregator'})} loggedin={this.state.screen}
              homePage={() => this.setState({screen:1})} loggedin={this.state.screen}
              me={() => this.setState({screen:7})} loggedin={this.state.screen}
              fullRecPage={() => this.setState({screen:5})} loggedin={this.state.screen}
            />
            {(()=> {
              switch(this.state.screen) {
                case 0:
                  return <div ><Login
                            login={(email) => this.setState({screen: 1, email: email, headerText: "Welcome " + email + "!"})}
                            signup={() => this.setState({screen: 2})}
                            app={this.app}
                          /></div>;
                case 1:
                  return <GetInfo
                          email={this.state.email}
                          changeProf={prof => this.setState({screen: 4, currProf: prof})}
                          changeClass={tempClass => this.setState({screen: 3, currClass: tempClass})}
                          getMore={tempEmail => this.setState({screen: 5, email: tempEmail})}
                          advanceSearch={() => this.setState({screen: 6})}
                          logout={() => this.setState({screen: 0})}/>;
                case 2:
                  return <Input
                            exitToLogin={() => this.setState({screen: 0})}
                            app={this.app}
                            />;
                case 3:
                  return <Class
                            changeProf={prof => this.setState({screen: 4, currProf: prof})}
                            currClass = {this.state.currClass}
                            />;
                case 4:
                  return <Prof
                            changeClass={tempClass => this.setState({screen: 3, currClass: tempClass})}
                            currProf={this.state.currProf}
                            />;
                case 5:
                  return <AllRecs
                            changeClass={tempClass => this.setState({screen: 3, currClass: tempClass})}
                            email={this.state.email}
                            />;
                case 6:
                  return <AdvSearch
                            changeProf={prof => this.setState({screen: 4, currProf: prof})}
                            changeClass={tempClass => this.setState({screen: 3, currClass: tempClass})}
                            />;
                case 7:
                  return <Me
                            email={this.state.email}
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
