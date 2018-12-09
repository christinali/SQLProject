import React from 'react';
import axios from 'axios';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";


export default class BasicInput extends React.Component {
  constructor(props){
    super(props);
    this.state = {fieldValues: this.props.fieldValues, majors: ''};
  }
  saveAndContinue = () => {
    this.props.saveValues(this.state.fieldValues);
  }

  handleChange = event => {
    let newfieldValues = this.state.fieldValues;
    newfieldValues[event.target.id] = event.target.value;
    this.setState({
      fieldValues: newfieldValues
    });
  };

  componentDidMount() {
    axios.get('http://localhost:5000/get-all-majors')
        .then(res => {
            console.log(res.data);
            this.setState({majors: res.data});
        })
        .catch(e => console.log(e))
  }

  render(){

    const majors = this.state.majors;
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
          <FormControl componentClass="select"
            onChange={this.handleChange}>
              <option value="">...</option>
              <option value="2019">2019</option>
              <option value="2020">2020</option>
              <option value="2021">2021</option>
              <option value="2022">2022</option>
          </FormControl>
        </FormGroup>
        <FormGroup controlId="major" bsSize="large">
          <ControlLabel><p className='name'>Major: </p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
            {Object.keys(majors).map(key => {
              return <option value={key}>{key}</option>
            })}
          </FormControl>
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
