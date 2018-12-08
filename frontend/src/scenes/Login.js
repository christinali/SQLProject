import React from 'react';
import firebase from 'firebase';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";

const firebaseConfig = {
    apiKey: "AIzaSyDfXgvgX2_eyPam6O3eenzLTJHrwHc2tdc",
    authDomain: "sqlproject-b318c.firebaseapp.com",
    databaseURL: "https://sqlproject-b318c.firebaseio.com",
    projectId: "sqlproject-b318c",
    storageBucket: "sqlproject-b318c.appspot.com",
    messagingSenderId: "612693141535"
};


const app = firebase.initializeApp(firebaseConfig);

export default class Login extends React.Component {
  state = { email: '', password: '' };

  handleLogin = () => {
    const { email, password } = this.state;
    app
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then(async user => {
      if (user) {
        this.props.login()
        alert("You logged in successfully")
      }
    })
    .catch(e => {
      alert(e.message);
      console.log(e)
    });
  };
  validateForm() {
    return this.state.email.length > 0 && this.state.password.length > 0;
  }
  handleSignup = () => {
    const { email, password } = this.state;
    app
    .auth()
    .createUserWithEmailAndPassword(email, password)
    .then(async user => {
      if (user) {
        this.props.signup()
        alert("You signed up successfully")
      }
    })
    .catch(e => {
      alert(e.message);
      console.log(e);
    });
  };

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };

  render() {
    return (
      <div className="Login">
          <div className="inner">
            <h2>Welcome to Our App!</h2>
            <p>Please enter your email and password to login/sign up below.</p>
          </div>
          <FormGroup controlId="email" bsSize="large">
            <ControlLabel><p class='name'>Email:</p></ControlLabel>
            <FormControl
              autoFocus
              type="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="password" bsSize="large">
            <ControlLabel><p class='name'>Password:</p></ControlLabel>
            <FormControl
              value={this.state.password}
              onChange={this.handleChange}
              type="password"
            />
          </FormGroup>
          <Button
            block
            bsSize="large"
            disabled={!this.validateForm()}
            type="submit"
            onClick={this.handleLogin}
            bsStyle="warning"
          >
            Login
          </Button>
          <Button
            block
            bsSize="large"
            disabled={!this.validateForm()}
            type="submit"
            onClick={this.handleSignup}
            bsStyle="warning"
          >
            Sign up
          </Button>
      </div>
    );
  }
}
