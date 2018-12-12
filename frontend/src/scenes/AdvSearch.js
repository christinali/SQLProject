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
            allMajors: [], //load at start
            minOvr: '-1',
            maxDiff: '6',
            query: '',
            resultOut: [],
            searchCat: 'classname', //default to searching by class name
            searchDept: '',
            searchTreqs: ''
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
      res.push({value: '', label: ''});
      if (array) {
          for (var i = 0; i < array.length; i++) {
            var temp = {value : array[i].toLowerCase(), label : array[i].toUpperCase()};
            res.push(temp);
          }
      }
      return res;
    }

    peruse(result) {
        if (this.state.searchCat === 'classname') {
            let resultCopy = this.state.allClasses;
            resultCopy = this.state.allClasses.filter(c => {
              if (this.state.searchDept != '') {
                return (c.name.toLowerCase().includes(result.toLowerCase()) && (c.dept.toLowerCase() === this.state.searchDept.toLowerCase())
                  && (parseFloat(c.overall) >= parseFloat(this.state.minOvr)) && (parseFloat(c.difficulty) <= parseFloat(this.state.maxDiff)));
              }
              else {
                return (c.name.toLowerCase().includes(result.toLowerCase()) && (parseFloat(c.overall) >= parseFloat(this.state.minOvr)) && (parseFloat(c.difficulty) <= parseFloat(this.state.maxDiff)));
              }
            })
            this.setState({
              query: result,
              resultOut: resultCopy,
            })
        }
        else if (this.state.searchCat === 'prof') {
            let resultCopy = this.state.allProfs;
            resultCopy = this.state.allProfs.filter(c => {
              return (c.name.toLowerCase().includes(result.toLowerCase()) && (parseFloat(c.overall) >= parseFloat(this.state.minOvr)) && (parseFloat(c.difficulty) <= parseFloat(this.state.maxDiff)));
            })
            this.setState({
              query: result,
              resultOut: resultCopy,
            })
        }
        else if (this.state.searchCat === 'classid') {
            let resultCopy = this.state.allClasses;
            resultCopy = this.state.allClasses.filter(c => {
              if (c.dept && c.num) {
                let temp = c.dept.toLowerCase() + c.num;
                if (this.state.searchDept != '') {
                  return (temp.includes(result.toLowerCase()) && (c.dept.toLowerCase() === this.state.searchDept.toLowerCase())&& (parseFloat(c.overall) >= parseFloat(this.state.minOvr)) && (parseFloat(c.difficulty) <= parseFloat(this.state.maxDiff)));
                }
                else {
                  return (temp.includes(result.toLowerCase())&& (parseFloat(c.overall) >= parseFloat(this.state.minOvr)) && (parseFloat(c.difficulty) <= parseFloat(this.state.maxDiff)));
                }
              }
            })
            this.setState({
              query: result,
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

    changeDept = (newValue: any) => {
        if (newValue) {
            this.setState ({
              searchDept: newValue.value,
            }, () => this.peruse(this.state.query))
        }
        else {
            this.setState ({
              searchDept: ''
            })
        }
    }

    changeOvr = (newValue: any) => {
      if (newValue) {
          this.setState ({
            minOvr: newValue.value,
          }, () => this.peruse(this.state.query))
      }
      else {
          this.setState ({
            minOvr: -1
          })
      }
    }

    changeDiff = (newValue: any) => {
      if (newValue) {
          this.setState ({
            maxDiff: newValue.value,
          }, () => this.peruse(this.state.query))
      }
      else {
          this.setState ({
            maxDiff: 6
          })
      }
    }

    render() {
        const currClass = this.state.currClass;
        const currProf = this.state.currProf;

        var majorList = this.state.allMajors;
        const deptOptions = this.makeMajorOptions(majorList);

        const ovrOptions = [
          { value: '0', label: '> 0' },
          { value: '0.5', label: '> 0.5' },
          { value: '1', label: '> 1' },
          { value: '1.5', label: '> 1.5'},
          { value: '2', label: '> 2' },
          { value: '2.5', label: '> 2.5' },
          { value: '3', label: '> 3' },
          { value: '3.5', label: '> 3.5'},
          { value: '4', label: '> 4' },
          { value: '4.5', label: '> 4.5' }
        ];

        const diffOptions = [
          { value: '5', label: '< 5'},
          { value: '4.5', label: '< 4.5' },
          { value: '4', label: '< 4' },
          { value: '3.5', label: '< 3.5' },
          { value: '3', label: '< 3'},
          { value: '2.5', label: '< 2.5' },
          { value: '2', label: '< 2'},
          { value: '1.5', label: '< 1.5' },
          { value: '1', label: '< 1' },
          { value: '0.5', label: '< 0.5' }
        ];

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

        const defaultPrimary = [
          {value: 'classname', label: 'Class Name' }
        ]

        return (
            <div className = 'Overall'>
                <div className = 'Advanced'>
                  <h2> Advanced Search: </h2>
                  <div className = 'topRow'>
                      <form>
                        <textarea
                          type="text"
                          placeholder = 'Enter search here...'
                          value = {this.state.query}
                          onChange = {result => this.peruse(result.target.value)}
                        />
                      </form>
                      <div className = "advDropDown">
                        <div className = "filter1">
                          <Select
                            defaultValue = {defaultPrimary}
                            onChange={this.changeCat}
                            options = {dropdownOptions}
                          />
                        </div>
                        <div className = "filter1">
                          <Select
                            onChange={this.changeDept}
                            options={deptOptions}
                            placeholder = "Department"
                          />
                        </div>
                        <div className = "filter2">
                          <Select
                            isMulti
                            options={aokOptions}
                            className = "basic-multi-select"
                            classNamePrefix = "select"
                            placeholder = "Areas of Knowledge"
                          />
                        </div>
                        <div className = "filter2">
                          <Select
                            isMulti
                            options={moiOptions}
                            className = "basic-multi-select"
                            classNamePrefix = "select"
                            placeholder = "Modes of Inquiry"
                          />
                        </div>
                        <div className = "filter1">
                          <Select
                            options={ovrOptions}
                            placeholder = "Min Overall"
                            onChange = {this.changeOvr}
                          />
                        </div>
                        <div className = "filter1">
                          <Select
                            options={diffOptions}
                            placeholder = "Max Difficulty"
                            onChange = {this.changeDiff}
                          />
                        </div>
                      </div>
                    </div>
                    <div className = 'BottomRow'>
                      {this.state.resultOut.map((c, i) => {
                        if (this.state.query.length > 0) {
                          if (this.state.searchCat === 'classname' || this.state.searchCat === 'classid') {
                            return <button className = "SearchClass" key={i} onClick={() => this.props.changeClass(c.id)}> {c.dept}{c.num} - {c.name}; overall: {c.overall} diff: {c.difficulty}</button>
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
