import React from 'react';
import firebase from 'firebase';
import { Button, FormGroup, FormControl, ControlLabel, HelpBlock } from "react-bootstrap";

export default class ContactInfo extends React.Component {
  state = this.props.fieldValues;

  validateForm() {
    return this.state.email.length > 0 && this.state.password.length > 0;
  }
  handleSignup = () => {
    const { email, password } = this.state;
    this.props.app
    .auth()
    .createUserWithEmailAndPassword(email, password)
    .then(async user => {
      if (user) {
        this.props.saveValues(this.state)
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
            <h2>Thanks for choosing to use our service!</h2>
            <p>Let's get some basic information from you first.</p>
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
          <FormGroup controlId="password" bsSize="large" validationState={this.getValidationState()}>
            <ControlLabel><p className='name'>Password:</p></ControlLabel>
            <FormControl
              value={this.state.password}
              onChange={this.handleChange}
              type="password"
            />
            <FormControl.Feedback />
            <HelpBlock>Password must be above 6 characters.</HelpBlock>
          </FormGroup>
          <Button
            block
            bsSize="large"
            disabled={!this.validateForm()}
            type="submit"
            onClick={this.handleSignup}
            bsStyle="warning"
          >
            Continue
          </Button>
          <Button
            block
            bsSize="large"
            type="submit"
            onClick={this.props.exit}
            bsStyle="warning"
          >
            Exit to login
          </Button>
      </div>
    );
  }
}
