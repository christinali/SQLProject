import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';


class GetInfo extends React.Component {
    constructor() {
        super();
        this.state = {
            id: null, //whatever the user login id is
            email: '', //replace with ''
            currClass: null,
            currProf: null,
            Treqs: null, //load with user ID
            Majors: null, //load with user ID
            allClasses: [], //load at start
            allProfs: [], //load at start
            query: '',
            resultOut: [],
            searchCat: 'classname' //default to searching by class name
        }

        this.getAllClasses();
        this.getAllProfs();
    }

    componentDidMount() {
        this.setState({
            email : this.props.email,
        })
        this.getTReqs(this.props.email);
        this.getMajors(this.props.email);
    }

    getTReqs(email) {
        axios.get('http://localhost:5000/get-recommended-treqs?email=' + this.props.email) //replace with email
            .then(res => {
                this.setState({
                  Treqs: res.data,
                })
            })
            .catch(e => console.log(e))
    }

    getMajors(email) {
        axios.get('http://localhost:5000/get-recommended-major?email=' + this.props.email) //replace with email
            .then(res => {
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
        axios.get('http://localhost:5000/get-all-profs')
          .then(res => {
            this.setState({
              allProfs: res.data,
            })
          })
          .catch(e => console.log(e))
    }

    splitTreqs(array) {
      var res = "";
      if (array) {
          for (var i = 0; i < array.length; i++) {
            res = res + " " + array[i].toUpperCase();
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
        const Treqs = this.state.Treqs;
        const Majors = this.state.Majors;

        const dropdownOptions = [
          { value: 'classid', label: 'Class ID' },
          { value: 'classname', label: 'Class Name' },
          { value: 'prof', label: 'Professor' }
        ];

        const defaultOption = [
          {value: 'classname', label: 'Class Name' }
        ]

        return (
            <div className = 'Overall'>

                <div className = 'Top3Recs'>
                    <div className = 'RecsTopRow'>
                        <h1> Top Treq Classes </h1>
                        <div className = 'RecsTopRowRemaining'> Remaining TReqs: 2 CCI, NS, FL </div>
                    </div>
                    <div className = 'ReqsAll'style={{display: 'flex', flexDirection: 'row'}}>
                        {Treqs && Treqs[0] && <div className = 'ReqsComp'>
                            <button className = "classTitle" onClick={() => this.props.changeClass(Treqs[0].id)}> {Treqs[0].dept}{Treqs[0].num} {Treqs[0].name != null ? String(Treqs[0].name).replace("\\u0026", "&") : null} </button>
                            <br/>
                            <h3> Overall:
                                {Treqs[0].overall != 0 ?
                                  <StarRatings
                                      rating={Treqs[0].overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h3> Difficulty:
                                {Treqs[0].difficulty != 0 ?
                                  <StarRatings
                                      rating={Treqs[0].difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h4> Treqs Satisfied: {this.splitTreqs(Treqs[0].satisfiesNeeded)} </h4>
                        </div>}

                        {Treqs && Treqs[1] && <div className = 'ReqsComp'>
                            <button className = "classTitle" onClick={() => this.props.changeClass(Treqs[1].id)}> {Treqs[1].dept}{Treqs[1].num} {Treqs[1].name != null ? String(Treqs[1].name).replace("\\u0026", "&") : null} </button>
                            <br/>
                            <h3> Overall:
                                {Treqs[1].overall != 0 ?
                                  <StarRatings
                                      rating={Treqs[1].overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h3> Difficulty:
                                {Treqs[1].difficulty != 0 ?
                                  <StarRatings
                                      rating={Treqs[1].difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h4> Treqs Satisfied: {this.splitTreqs(Treqs[1].satisfiesNeeded)} </h4>
                        </div>}

                        {Treqs && Treqs[2] && <div className = 'ReqsComp'>
                            <button className = "classTitle" onClick={() => this.props.changeClass(Treqs[2].id)}> {Treqs[2].dept}{Treqs[2].num} {Treqs[2].name != null ? String(Treqs[2].name).replace("\\u0026", "&") : null} </button>
                            <br/>
                            <h3> Overall:
                                {Treqs[2].overall != 0 ?
                                  <StarRatings
                                      rating={Treqs[2].overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h3> Difficulty:
                                {Treqs[2].difficulty != 0 ?
                                  <StarRatings
                                      rating={Treqs[2].difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h4> Treqs Satisfied: {this.splitTreqs(Treqs[2].satisfiesNeeded)} </h4>
                        </div>}
                    </div>
                    <div className = "RecsBotRow">
                        <button className = "MoreRecs" onClick={() => this.props.getMore(this.state.email)}> More Recommended Classes... </button>
                    </div>
                </div>
                <div className = 'Searcher'>
                  <div className = 'locker'>
                    <h2> Search: </h2>
                    <div className = 'TopRow'>
                      <form>
                        <textarea style={{resize:'none'}}
                          type="text"
                          placeholder = 'Enter search here...'
                          value = {this.state.query}
                          onChange = {result => this.peruse(result)}
                        />
                      </form>
                      <div className = "dropDown">
                          <Select
                            defaultValue = {defaultOption}
                            onChange={this.changeCat}
                            options = {dropdownOptions}
                          />
                      </div>
                    </div>
                    <div className = 'BottomRow'>
                      {this.state.resultOut.map((c, i) => {
                        if (this.state.query.length > 0) {
                          if (this.state.searchCat === 'classname' || this.state.searchCat === 'classid') {
                            return <button className = "SearchClass" key={i} onClick={() => this.props.changeClass(c.id)}> {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null}</button>
                          }
                          else {
                            return <button className = "SearchProf" key={i} onClick={() => this.props.changeProf(c.professor_id)}> {c.name} </button>
                          }
                        }
                      })}
                    </div>
                    <button className = "advSearch" onClick={() => this.props.advanceSearch()}> Advanced Search... </button>
                  </div>
                </div>
                <div className = 'Top3Recs'>
                    <h1> Top Major Classes </h1>
                    <div className = 'ReqsAll'style={{display: 'flex', flexDirection: 'row'}}>
                        {Majors && Majors[0] && <div className = 'ReqsComp'>
                            <button className = "classTitle" onClick={() => this.props.changeClass(Majors[0].id)}> {Majors[0].dept}{Majors[0].num} {Majors[0].name != null ? String(Majors[0].name).replace("\\u0026", "&") : null} </button>
                            <br/>
                            <h3> Overall:
                                {Majors[0].overall != 0 ?
                                  <StarRatings
                                      rating={Majors[0].overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h3> Difficulty:
                                {Majors[0].difficulty != 0 ?
                                  <StarRatings
                                      rating={Majors[0].difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h4> Treqs Satisfied: {this.splitTreqs(Majors[0].satisfiesNeeded)} </h4>
                        </div>}

                        {Majors && Majors[1] && <div className = 'ReqsComp'>
                            <button className = "classTitle" onClick={() => this.props.changeClass(Majors[1].id)}> {Majors[1].dept}{Majors[1].num} {Majors[1].name != null ? String(Majors[1].name).replace("\\u0026", "&") : null} </button>
                            <br/>
                            <h3> Overall:
                                {Majors[1].overall != 0 ?
                                  <StarRatings
                                      rating={Majors[1].overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h3> Difficulty:
                                {Majors[1].difficulty != 0 ?
                                  <StarRatings
                                      rating={Majors[1].difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h4> Treqs Satisfied: {this.splitTreqs(Majors[1].satisfiesNeeded)} </h4>
                        </div>}

                        {Majors && Majors[2] && <div className = 'ReqsComp'>
                            <button className = "classTitle" onClick={() => this.props.changeClass(Majors[2].id)}> {Majors[2].dept}{Majors[2].num} {Majors[2].name != null ? String(Majors[2].name).replace("\\u0026", "&") : null} </button>
                            <br/>
                            <h3> Overall:
                                {Majors[2].overall != 0 ?
                                  <StarRatings
                                      rating={Majors[2].overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h3> Difficulty:
                                {Majors[2].difficulty != 0 ?
                                  <StarRatings
                                      rating={Majors[2].difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                            </h3>
                            <h4> Treqs Satisfied: {this.splitTreqs(Majors[2].satisfiesNeeded)} </h4>
                        </div>}
                    </div>
                    <div className = "RecsBotRow">
                        <button className = "MoreRecs"> More Recommended Classes... </button>
                    </div>
                </div>
            </div>
        );
    }
}

export default GetInfo;
