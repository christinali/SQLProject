import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';

class Prof extends Component {
    constructor() {
        super();
        this.state = {
            id: 1, //whatever the prof id is
            currProf: [],
            profComms: [],
        }

        this.getProfInfo();
    }

    componentDidMount() {
        this.getProfInfo()
    }

    getProfInfo(id) {
        axios.get('http://localhost:5000/get-prof-info?prof_id=' + 1) //replace with id
            .then(res => {
                this.setState({
                  currProf: res.data,
                  profComms: res.data.topComments,
                })
            })
            .catch(e => console.log(e))
    }

    render() {
        const currProf = this.state.currProf;
        const profComms = this.state.profComms;

        return (
            <div className="Overall">
                <div className = "topRow">
                    <div className = "topLeft">
                        <h1> {currProf.name} </h1>
                    </div>
                    <div className = "topRight">
                        <div className = "scores">
                            <h2> Overall:
                                <StarRatings
                                    rating={currProf.overall}
                                    starDimension="60px"
                                    starSpacing="3px"
                                    starRatedColor="#FF8C00"
                                />
                            </h2>
                            <h2> Difficulty:
                                <StarRatings
                                    rating={currProf.difficulty}
                                    starDimension="60px"
                                    starSpacing="3px"
                                    starRatedColor="#FF8C00"
                                />
                            </h2>
                        </div>
                        <div className = "otherClasses">
                            <h2> Classes Taught Next Semester: </h2>
                            <div className = "classInfo">
                                {currProf.nextSemClasses && currProf.nextSemClasses.map((c, i) => {
                                  if (c) {
                                    return <p key={i}>{i+1}) {c.dept}{c.classNum} - {c.name}</p>
                                  }
                                })}
                            </div>
                            <h2> Previously Taught Classes: </h2>
                            <div className = "classInfo">
                                {currProf.prevClasses && currProf.prevClasses.map((c, i) => {
                                  if (c && i<3) {
                                    return <p key={i}>{i+1}) {c.dept}{c.classNum} - {c.name}</p>
                                  }
                                })}
                            </div>
                        </div>
                    </div>
                </div>
                <h2 className = 'TSR'> Top Student Reviews: </h2>
                    {profComms && profComms.map((c, i) => {
                      if (c) {
                        return <div className = "botRow">
                            <div className = "reviewInfo">
                                <h4> {c.date} </h4>
                                <h3> Overall: {c.overall} </h3>
                                <h3> Difficulty: {c.difficulty} </h3>
                            </div>
                            <div className = "reviewTarget">
                                <h4> Class: {c.class[0].dept}{c.class[0].classNum} </h4>
                                <h4> Semester: {c.semester} </h4>
                                <h4> Grade Received: {c.grade} </h4>
                            </div>
                            <div className = "reviewContent">
                                <h4> {c.comment} </h4>
                            </div>
                        </div>
                      }
                  })}
            </div>
        );
    }
}

export default Prof;


/*
MAIN - FIGURE OUT HOW TO GET PROF ID AUTOMATICALLY
1) need to add Up/Downvote Functionality
2) need to make backend real
3) need to link everything
*/
