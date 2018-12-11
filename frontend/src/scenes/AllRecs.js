import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';


class AllRecs extends React.Component {
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
    }

    componentDidMount() {
        this.setState({
            email : this.props.email,
        })
        this.getTReqs(this.props.email);
        this.getMajors(this.props.email);
    }

    getTReqs(email) {
        axios.get('http://localhost:5000/get-recommended-treqs?user_email=' + email) //replace with email
            .then(res => {
                this.setState({
                  Treqs: res.data,
                })
            })
            .catch(e => console.log(e))
    }

    getMajors(email) {
        axios.get('http://localhost:5000/get-recommended-major?user_email=' + email) //replace with email
            .then(res => {
                this.setState({
                  Majors: res.data,
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

    render() {
        const currClass = this.state.currClass;
        const currProf = this.state.currProf;
        const Treqs = this.state.Treqs;
        const Majors = this.state.Majors;

        return (
            <div className = 'big'>
                <div className = 'LeftCol'>
                    <h1> Trinity Recs (Top 10) </h1>
                    <div className = 'stopOverflow'>
                        {Treqs && Treqs.map((c, i) => {
                          if (c && i<10) {
                            return <div className = 'recResults'>
                              <button className = "classTitle" onClick={() => this.props.changeClass(c.id)}> ({i+1}) {c.dept}{c.num} - {c.name} </button>
                              <br/>
                              <h3> Overall:
                                  <StarRatings
                                      rating={c.overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  />
                              </h3>
                              <h3> Difficulty:
                                  <StarRatings
                                      rating={c.difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  />
                              </h3>
                              <h4> Treqs Satisfied: {this.splitTreqs(c.satisfiesNeeded)} </h4>
                              </div>
                          }
                        })}
                    </div>
                </div>
                <div className = 'RightCol'>
                    <h1> Major Recs (Top 10) </h1>
                    <div className = 'stopOverflow'>
                        {Majors && Majors.map((c, i) => {
                          if (c && i<10) {
                            return <div className = 'recResults'>
                              <button className = "classTitle" onClick={() => this.props.changeClass(c.id)}> ({i+1}) {c.dept}{c.num} - {c.name} </button>
                              <br/>
                              <h3> Overall:
                                  <StarRatings
                                      rating={c.overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  />
                              </h3>
                              <h3> Difficulty:
                                  <StarRatings
                                      rating={c.difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  />
                              </h3>
                              <h4> Treqs Satisfied: {this.splitTreqs(c.satisfiesNeeded)} </h4>
                              </div>
                          }
                        })}
                    </div>
                </div>
            </div>
        );
    }
}

export default AllRecs;

/*
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


/*
MAIN - FIGURE OUT HOW TO GET PROF ID AUTOMATICALLY
1) need to make backend real
2) need to link everything

*/
