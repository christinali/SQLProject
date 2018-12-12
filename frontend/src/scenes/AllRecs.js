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
        axios.get('http://localhost:5000/get-recommended-treqs?email=' + email) //replace with email
            .then(res => {
                this.setState({
                  Treqs: res.data,
                })
            })
            .catch(e => console.log(e))
    }

    getMajors(email) {
        axios.get('http://localhost:5000/get-recommended-major?email=' + email) //replace with email
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
                    <h1> Trinity Recs (Top 15) </h1>
                    <div className = 'stopOverflow'>
                        {Treqs && Treqs.map((c, i) => {
                          if (c && i<15) {
                            return <div className = 'recResults'>
                              <button className = "classTitle" onClick={() => this.props.changeClass(c.id)}> ({i+1}) {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null} </button>
                              <br/>
                              <h3> Overall:
                                {c.overall != 0 ?
                                  <StarRatings
                                      rating={c.overall}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                              </h3>
                              <h3> Difficulty:
                                {c.difficulty != 0 ?
                                  <StarRatings
                                      rating={c.difficulty}
                                      starDimension="22px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet! </h3> }
                              </h3>
                              <h4> Treqs Satisfied: {this.splitTreqs(c.satisfiesNeeded)} </h4>
                              </div>
                          }
                        })}
                    </div>
                </div>
                <div className = 'RightCol'>
                    <h1> Major Recs (Top 15) </h1>
                    <div className = 'stopOverflow'>
                        {Majors && Majors.map((c, i) => {
                          if (c && i < 15) {
                            return <div className = 'recResults'>
                              <button className = "classTitle" onClick={() => this.props.changeClass(c.id)}> ({i+1}) {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null} </button>
                              <br/>
                              <h3> Overall:
                                  {c.overall != 0 ?
                                    <StarRatings
                                        rating={c.overall}
                                        starDimension="22px"
                                        starSpacing="3px"
                                        starRatedColor="#FF8C00"
                                    /> : <h4> No rating yet! </h4> }
                              </h3>
                              <h3> Difficulty:
                                  {c.difficulty != 0 ?
                                    <StarRatings
                                        rating={c.difficulty}
                                        starDimension="22px"
                                        starSpacing="3px"
                                        starRatedColor="#FF8C00"
                                    /> : <h4> No rating yet! </h4> }
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
