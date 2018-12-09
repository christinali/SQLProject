import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';


class GetInfo extends React.Component {
    constructor() {
        super();
        this.state = {
            id: null, //whatever the user login id is
            currClass: null,
            currProf: null,
            Treqs: null,
            Majors: null,
            allClasses: [],
            allProfs: [],
            query: null,
            resultOut: [],
            searchCat: 'classname'
        }

        this.getAllClasses();
        this.getAllProfs();
    }

    getClass() {
        axios.get('http://localhost:5000/get-class-info?class_id=' + this.state.id)
            .then(res => {
                console.log(res.data);
                this.setState({currClass: res.data});
            })
            .catch(e => console.log(e))
    }

    getProf() {
        axios.get('http://localhost:5000/get-prof-info?prof_id=' + this.state.id)
            .then(res => {
                console.log(res.data);
                this.setState({currProf: res.data});
            })
            .catch(e => console.log(e))
    }

    getTReqs() {
        axios.get('http://localhost:5000/get-recommended-treqs?user_id=' + this.state.id)
            .then(res => {
                console.log(res.data);
                this.setState({
                  Treqs: res.data,
                })
            })
            .catch(e => console.log(e))
    }

    getMajors() {
        axios.get('http://localhost:5000/get-recommended-major?user_id=' + this.state.id)
            .then(res => {
                console.log(res.data);
                this.setState({
                  Majors: res.data,
                })
            })
            .catch(e => console.log(e))
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
        axios.get('http://localhost:5000/get-all-professors')
          .then(res => {
            this.setState({
              allProfs: res.data,
            })
          })
          .catch(e => console.log(e))
    }

    splitTreqs(array) {
      var res = "";
      for (var i = 0; i < array.length; i++) {
        res = res + " " + array[i];
      }
      return res;
    }

    peruse(result) {
        if (this.state.searchCat === 'classname') {
          let resultCopy = this.state.allClasses;
          resultCopy = this.state.allClasses.filter(c => {
            return c.name.toLowerCase().startsWith(result.target.value.toLowerCase());
          })
          this.setState({
            query: result.target.value,
            resultOut: resultCopy,
          })
        }
        else if (this.state.searchCat === 'prof') {
          let resultCopy = this.state.allProfs;
          resultCopy = this.state.allProfs.filter(c => {
            return c.name.toLowerCase().startsWith(result.target.value.toLowerCase());
          })
          this.setState({
            query: result.target.value,
            resultOut: resultCopy,
          })
        }
        else if (this.state.searchCat === 'classid') {
          let resultCopy = this.state.allProfs;
          resultCopy = this.state.allProfs.filter(c => {
            return c.name.toLowerCase().startsWith(result.target.value.toLowerCase());
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
          searchCat: newValue.value
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
        const Treqs = this.state.Treqs;
        const Majors = this.state.Majors;

        const dropdownOptions = [
          { value: 'classid', label: 'Class ID' },
          { value: 'classname', label: 'Class Name' },
          { value: 'prof', label: 'Professor' }
        ];

        const defaultOption = [
          {value: 'classid', label: 'Class ID' }
        ]

        return (
            <div className = 'Overall'>
                <div>
                  <button onClick={this.props.logout}>Log Out</button>
                </div>
                <label>id:
                    <input type="text" value={this.state.email} onChange={e => this.setState({id: e.target.value})} />
                </label>
                <button onClick={() => this.getTReqs()}>Get Trecs</button>
                <button onClick={() => this.getMajors()}>Get Majors</button>
                <button onClick={() => this.getTReqs()}>Get Trecs</button>
                <button onClick={() => this.getMajors()}>Get Majors</button>

                <div className = 'Top3Recs'>
                    <h2> Top Treq Classes: </h2>
                    <div className = 'ReqsAll'style={{display: 'flex', flexDirection: 'row'}}>
                        {Treqs && Treqs[0] && <div className = 'ReqsComp'>
                            <h1> {Treqs[0].dept}{Treqs[0].num} - {Treqs[0].name} </h1>
                            <h2> Overall: {Treqs[0].overall} </h2>
                            <h2> Difficulty: {Treqs[0].difficulty} </h2>
                            <h4> Treqs Satisfied: {this.splitTreqs(Treqs[0].satisfiesNeeded)} </h4>
                        </div>}

                        {Treqs && Treqs[1] && <div className = 'ReqsComp'>
                            <h1> {Treqs[1].dept}{Treqs[1].num} - {Treqs[1].name} </h1>
                            <h2> Overall: {Treqs[1].overall} </h2>
                            <h2> Difficulty: {Treqs[1].difficulty} </h2>
                            <h4> Treqs Satisfied: {this.splitTreqs(Treqs[1].satisfiesNeeded)} </h4>
                        </div>}

                        {Treqs && Treqs[2] && <div className = 'ReqsComp'>
                            <h1> {Treqs[2].dept}{Treqs[2].num} - {Treqs[2].name} </h1>
                            <h2> Overall: {Treqs[2].overall} </h2>
                            <h2> Difficulty: {Treqs[2].difficulty} </h2>
                            <h4> Treqs Satisfied: {this.splitTreqs(Treqs[2].satisfiesNeeded)} </h4>
                        </div>}
                    </div>
                </div>
                <div className = 'Searcher'>
                  <h2> Search: </h2>
                  <div className = 'TopRow'>
                      <form>
                        <textarea
                          type="text"
                          placeholder = 'Enter search here...'
                          value = {this.state.query}
                          onChange = {result => this.peruse(result)}
                        />
                      </form>
                      <div className = "dropDown">
                          <Select
                            isClearable
                            onChange={this.changeCat}
                            options = {dropdownOptions}
                            placeholder = 'Search Category...'
                          />
                      </div>
                    </div>
                    <div className = 'BottomRow'>
                      {this.state.resultOut.map((c, i) => {
                        if (this.state.query.length > 0) {
                          return <p key={i}>{c.name}</p>
                        }
                      })}
                    </div>
                </div>
                <div className = 'Top3Recs'>
                    <h2> Top Major Classes: </h2>
                    <div className = 'ReqsAll'style={{display: 'flex', flexDirection: 'row'}}>
                        {Majors && Majors[0] && <div className = 'ReqsComp'>
                            <h1> {Majors[0].dept}{Majors[0].num} - {Treqs[0].name} </h1>
                            <h2> Overall: {Majors[0].overall} </h2>
                            <h2> Difficulty: {Majors[0].difficulty} </h2>
                        </div>}

                        {Majors && Majors[1] && <div className = 'ReqsComp'>
                            <h1> {Majors[1].dept}{Majors[1].num} - {Majors[1].name} </h1>
                            <h2> Overall: {Majors[1].overall} </h2>
                            <h2> Difficulty: {Majors[1].difficulty} </h2>
                        </div>}

                        {Majors && Majors[2] && <div className = 'ReqsComp'>
                            <h1> {Majors[2].dept}{Majors[2].num} - {Majors[2].name} </h1>
                            <h2> Overall: {Majors[2].overall} </h2>
                            <h2> Difficulty: {Majors[2].difficulty} </h2>
                        </div>}
                    </div>
                </div>
            </div>
        );
    }
}

export default GetInfo;

/*
{currClass && <div>
    <h1>Class Info:</h1>
    {Object.keys(currClass).map(key => {
        if (key === "nextSemProf") {
            return <div>
                <h4>{key}</h4>
                <ul>
                {Object.keys(currClass[key]).map(secondkey => {
                    return <li>{secondkey} = {currClass[key][secondkey]}</li>
                })}
                </ul>
            </div>
        }
        else if (key === "comments" || key === "profs") {
            const arr = currClass[key];
            return <ol>
                {arr.map(a => {
                    return <li>
                        {Object.keys(a).map(secondkey => {
                            return <p>{secondkey} = {a[secondkey]}</p>
                    })}
                    </li>
                })}
            </ol>
        } else {
            return <h5>{key} = {currClass[key]}</h5>
        }
    })}
</div>}
{currProf && <div>
    <h1>Prof Info</h1>
    {Object.keys(currProf).map(key => {
        if (key === "nextSemClasses" || key === "topComments") {
            const arr = currProf[key];
            return <ol>
                {arr.map(a => {
                    return <li>
                        {Object.keys(a).map(secondkey => {
                            return <p>{secondkey} = {a[secondkey]}</p>
                        })}
                    </li>
                })}
            </ol>
        } else {
            return <h5>{key} = {currProf[key]}</h5>
        }
    })}
</div>}
*/
