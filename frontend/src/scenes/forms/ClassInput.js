import React from 'react';
import axios from 'axios';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";


export default class ClassInput extends React.Component {
  handleChange = event => {
    let newfieldValues = this.state.main;
    newfieldValues[event.target.id] = event.target.value;
    this.setState({
      main: newfieldValues
    });
  };
  state = { main: {major: '',
            class: '',
            semester: '',
            year: '',
            overall: '',
            difficulty: '',
            review: ''},
            majors: [], classes: []
  };
  componentDidMount() {
    axios.get('http://localhost:5000/get-all-majors')
        .then(res => {
            console.log(res.data);
            this.setState({majors: res.data});
        })
        .catch(e => console.log(e))

  }
  compress = () => {
    let fieldValues = this.props.fieldValues;
    let gg = this.state.main;

    /*let ret = {
                'user_id': fieldValues.user_id,
                'dept_id': gg.major,
                'class_num': gg.class,
                'semester': gg.year + " " + gg.semester + " Term",
                'star_number': gg.overall,
                'difficulty': gg.difficulty,
                'comment_id': gg.review,
    };*/
    let ret = '';
    ret += 'user_id=' + fieldValues.user_id + '&' + 'SHIT HERE' + 'semester=' + gg.year + ' ' + gg.semester + ' Term' + '&'
      + 'star_number=' + gg.overall + '&' + "difficulty=" + gg.difficulty;


    axios.post('http://localhost:5000/feroze-add-class', ret)
        .then(res => {
            console.log(res.data);
        })
        .catch(e => console.log(e))

    fieldValues.classes.push(gg);
    this.props.saveValues(fieldValues);
    this.setState({ main: {
      major: '',
      class: '',
      semester: '',
      year: '',
      overall: '',
      difficulty: '',
      review: ''
    }
    });
  };
  render(){
    const majors = this.state.majors;
    axios.get('http://localhost:5000/get-classes-in-major?major=' + this.state.main.major)
        .then(res => {
            console.log(res.data);
            this.setState({classes: res.data});
        })
        .catch(e => console.log(e))
    const classes = this.state.classes;
    return(
      <div className="Login">
      <h2>Add a Class</h2>
        <FormGroup controlId="major" bsSize="large">
          <ControlLabel><p className='name'>Class Department </p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
            {majors.map(key => {
              return <option value={key}>{key}</option>
            })}
          </FormControl>
        </FormGroup>
      <FormGroup controlId="class" bsSize="large">
        <ControlLabel><p className='name'>Class Name </p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
            {classes.map(key => {
              return <option value={key.name}>{key.dept + " " + key.num + ": " + key.name }</option>
            })}
          </FormControl>
      </FormGroup>
      <FormGroup controlId="semester" bsSize="large">
        <ControlLabel><p className='name'>Semester Taken </p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
              <option value="">...</option>
              <option value="F">Fall</option>
              <option value="S">Spring</option>
          </FormControl>
      </FormGroup>
      <FormGroup controlId="year" bsSize="large">
        <ControlLabel><p className='name'> Year Taken</p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
              <option value="">...</option>
              <option value="15">2015</option>
              <option value="16">2016</option>
              <option value="17">2017</option>
              <option value="18">2018</option>
              <option value="19">2019</option>
          </FormControl>
      </FormGroup>
      <FormGroup controlId="overall" bsSize="large">
        <ControlLabel><p className='name'> Overall Rating (out of 5)</p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
              <option value="">...</option>
              <option value="1">1 - Hated it</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5 - Loved it</option>
          </FormControl>
      </FormGroup>
      <FormGroup controlId="difficulty" bsSize="large">
        <ControlLabel><p className='name'> Difficulty Rating (out of 5)</p></ControlLabel>
          <FormControl componentClass="select"
            onChange={this.handleChange}>
              <option value="">...</option>
              <option value="1">1 - Piece of cake</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5 - Hard</option>
          </FormControl>
      </FormGroup>
      <FormGroup controlId="review" bsSize="large">
        <ControlLabel><p className='name'>Review (optional)</p></ControlLabel>
        <FormControl
          componentClass="textarea"
          placeholder="Say how you really feel!"
          value={this.state.review}
          onChange={this.handleChange}
          type="text"
        />
      </FormGroup>
      <Button
        block
        bsSize="large"
        type="submit"
        onClick={this.compress}
        bsStyle="primary"
      >
        Add another class
      </Button>
      <Button
        block
        bsSize="large"
        type="submit"
        onClick={this.props.exit}
        bsStyle="warning"
      >
        Submit
      </Button>



      </div>
    );
  }
}
