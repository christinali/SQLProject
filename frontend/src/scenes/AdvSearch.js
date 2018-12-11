import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';


class AdvSearch extends React.Component {
    constructor() {
        super();
        this.state = {
            id: null, //whatever the user login id is
            email: '', //replace with ''
            currClass: null,
            currProf: null,
            allClasses: [], //load at start
            allProfs: [], //load at start
            allMajors: [],
            query: '',
            resultOut: [],
            searchCat: 'classname' //default to searching by class name
        }

        this.getAllClasses();
        this.getAllProfs();
        this.getAllMajors();
    }

    componentDidMount() {
        this.setState({
            email : this.props.email,
        })
        this.getAllClasses();
        this.getAllProfs();
        this.getAllMajors();
    }

    getAllClasses() {
        axios.get('http://localhost:5000/get-all-classes')
          .then(res => {
            this.setState({
              allClasses: res.data,
            })
          })
          .catch(e => console.log(e))
    }

    getAllProfs() {
        axios.get('http://localhost:5000/get-all-profs')
          .then(res => {
            this.setState({
              allProfs: res.data,
            })
          })
          .catch(e => console.log(e))
    }

    getAllMajors() {
      axios.get('http://localhost:5000/get-all-majors')
          .then(res => {
              this.setState({
                allMajors: res.data,
              });
          })
          .catch(e => console.log(e))
    }

    makeMajorOptions(array) {
      var res = [];
      if (array) {
          for (var i = 0; i < array.length; i++) {
            String temp = 'value: ' +array[i].toLowerCase() + ', ' + 'label: ' +array[i].toUpperCase();
            res.append(temp)
          }
      }
      return res;
    }

    peruse(result) {
        if (this.state.searchCat === 'classname') {
            let resultCopy = this.state.allClasses;
            resultCopy = this.state.allClasses.filter(c => {
              return c.name.toLowerCase().includes(result.target.value.toLowerCase());
            })
            this.setState({
              query: result.target.value,
              resultOut: resultCopy,
            })
        }
        else if (this.state.searchCat === 'prof') {
            let resultCopy = this.state.allProfs;
            resultCopy = this.state.allProfs.filter(c => {
              return c.name.toLowerCase().includes(result.target.value.toLowerCase());
            })
            this.setState({
              query: result.target.value,
              resultOut: resultCopy,
            })
        }
        else if (this.state.searchCat === 'classid') {
            let resultCopy = this.state.allClasses;
            resultCopy = this.state.allClasses.filter(c => {
              if (c.dept && c.num) {
                let temp = c.dept.toLowerCase() + c.num;
                return temp.includes(result.target.value.toLowerCase());
              }
            })
            this.setState({
              query: result.target.value,
              resultOut: resultCopy,
            })
        }
    }

    changeCat = (newValue: any) => {
        if (newValue) {
            this.setState ({
              searchCat: newValue.value,
              query: ''
            })
        }
        else {
            this.setState ({
              searchCat: ''
            })
        }
    }

    render() {
        const currClass = this.state.currClass;
        const currProf = this.state.currProf;

        const dropdownOptions = [
          { value: 'classid', label: 'Class ID' },
          { value: 'classname', label: 'Class Name' },
          { value: 'prof', label: 'Professor' }
        ];

        const aokOptions = [
          { value: 'alp', label: 'ALP' },
          { value: 'cz', label: 'CZ' },
          { value: 'ns', label: 'NS' },
          { value: 'qs', label: 'QS' },
          { value: 'ss', label: 'SS' }
        ];

        const moiOptions = [
          { value: 'cci', label: 'CCI' },
          { value: 'ei', label: 'EI' },
          { value: 'sts', label: 'STS' },
          { value: 'fl', label: 'FL' },
          { value: 'w', label: 'W' },
          { value: 'r', label: 'R' }
        ];

        const defaultOption = [
          {value: 'classname', label: 'Class Name' }
        ]

        return (
            <div className = 'Overall'>
                <div className = 'Advanced'>
                  <h2> Search: </h2>
                  <div className = 'topRow'>
                      <form>
                        <textarea
                          type="text"
                          placeholder = 'Enter search here...'
                          value = {this.state.query}
                          onChange = {result => this.peruse(result)}
                        />
                      </form>
                      <div className = "advDropDown">
                        <div className = "filter1">
                          <Select
                            defaultValue = {defaultOption}
                            onChange={this.changeCat}
                            options = {dropdownOptions}
                          />
                        </div>
                        <div className = "filter2">
                          <Select
                            isMulti
                            options={aokOptions}
                            className = "basic-multi-select"
                            classNamePrefix = "select"

                          />
                        </div>
                        <div className = "filter2">
                          <Select
                            isMulti
                            options={moiOptions}
                            className = "basic-multi-select"
                            classNamePrefix = "select"
                          />
                        </div>
                      </div>
                    </div>
                    <div className = 'BottomRow'>
                      {this.state.resultOut.map((c, i) => {
                        if (this.state.query.length > 0) {
                          if (this.state.searchCat === 'classname' || this.state.searchCat === 'classid') {
                            return <button className = "SearchClass" key={i} onClick={() => this.props.changeClass(c.id)}> {c.dept}{c.num} - {c.name}</button>
                          }
                          else {
                            return <button className = "SearchProf" key={i} onClick={() => this.props.changeProf(c.id)}> {c.name} </button>
                          }
                        }
                      })}
                    </div>
                </div>
            </div>
        );
    }
}

export default AdvSearch;

/*
MAIN - FIGURE OUT HOW TO GET PROF ID AUTOMATICALLY
1) need to make backend real
2) need to link everything

*/
