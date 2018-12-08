import React from 'react';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";


export default class BasicInput extends React.Component {
  saveAndContinue = () => {
    this.props.saveValues(this.state);
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };
  state = this.props.fieldValues;
  render(){
    return(
      <div className="Login">
        <h2>Basic Input</h2>
        <FormGroup controlId="fname" bsSize="large">
          <ControlLabel><p className='name'>First Name:</p></ControlLabel>
          <FormControl
            autoFocus
            type="text"
            value={this.state.fname}
            onChange={this.handleChange}
          />
        </FormGroup>
        <FormGroup controlId="lname" bsSize="large">
          <ControlLabel><p className='name'>Last Name: </p></ControlLabel>
          <FormControl
            value={this.state.lname}
            onChange={this.handleChange}
            type="text"
          />
        </FormGroup>
        <FormGroup controlId="gradyear" bsSize="large">
          <ControlLabel><p className='name'>Graduation Year: </p></ControlLabel>
          <FormControl
            value={this.state.gradyear}
            onChange={this.handleChange}
            type="text"
          />
        </FormGroup>
        <FormGroup controlId="major" bsSize="large">
          <ControlLabel><p className='name'>Major: </p></ControlLabel>
          <FormControl
            value={this.state.major}
            onChange={this.handleChange}
            type="text"
          />
        </FormGroup>
        <Button
          block
          bsSize="large"
          type="submit"
          onClick={this.saveAndContinue}
          bsStyle="warning"
        >
          Continue
        </Button>



      </div>
    );
  }
}
