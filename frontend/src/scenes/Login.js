import React from 'react';
import firebase from 'firebase';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";



export default class Login extends React.Component {
  state = { email: '', password: '' };

  handleSignup = () => {
    this.props.signup();
  }

  handleLogin = () => {
    const { email, password } = this.state;
    this.props.app
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then(async user => {
      if (user) {
        this.props.login(this.state.email)
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

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };

  getValidationState() {
    const length = this.state.password.length;
    if (length > 6) return 'success';
    else if (length > 0) return 'error';
    return null;
  }

  render() {
    return (
      <div className="Login">
          <div className="inner">
            <h2>Welcome to Our App!</h2>
            <p>Please enter your email and password to login, or click sign up below.</p>
          </div>
          <FormGroup controlId="email" bsSize="large">
            <ControlLabel><p className='name'>Email:</p></ControlLabel>
            <FormControl
              autoFocus
              type="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="password" bsSize="large">
            <ControlLabel><p className='name'>Password:</p></ControlLabel>
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
