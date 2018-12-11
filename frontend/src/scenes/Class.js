import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';

class Class extends Component {
    constructor() {
        super();
        this.state = {
            currClass: [],
            classComms: [],
        }

    }

    componentDidMount() {
        this.getClassInfo()
    }

    getClassInfo() {
        axios.get('http://localhost:5000/get-class-info?class_id=' + 1) //this.props.currClass
            .then(res => {
                this.setState({
                  currClass: res.data,
                  classComms: res.data.comments,
                })
            })
            .catch(e => console.log(e))
    }

    upVote(id) {
      axios.post('http://localhost:5000/reviews/upvote?review_id=' + id)
          .then(res => console.log(res))
    }

    downVote(id) {
      axios.post('http://localhost:5000/reviews/downvote?review_id=' + id)
          .then(res => console.log(res))
    }

    render() {
        const currClass = this.state.currClass;
        const classComms = this.state.classComms;

        return (
            <div className="Overall">
                {this.props.id}
                <div className = "topRow">
                    <div className = "topLeft">
                        <h1> {currClass.dept}{currClass.num}: </h1>
                        <h1> {currClass.name} </h1>
                    </div>
                    <div className = "topRight">
                        <div className = "scores">
                            <h2> Overall:
                                <StarRatings
                                    rating={currClass.overall}
                                    starDimension="40px"
                                    starSpacing="3px"
                                    starRatedColor="#FF8C00"
                                />
                            </h2>
                            <h2> Difficulty:
                                <StarRatings
                                    rating={currClass.difficulty}
                                    starDimension="40px"
                                    starSpacing="3px"
                                    starRatedColor="#FF8C00"
                                />
                            </h2>
                        </div>
                        <div className = "otherClasses">
                            <h2> Next Semester Professor: </h2>
                            <div className = "classInfo">
                                {currClass.nextSemProf && Object.keys(currClass.nextSemProf).map((c, i) => {
                                  if (c) {
                                    return <p onClick={() => this.props.changeProf(c.id)}> {c}: {currClass.nextSemProf[c]} </p>
                                  }
                                })}
                            </div>
                            <h2> Previous Professors: </h2>
                            <div className = "classInfo">
                                {currClass.profs && currClass.profs.map((c, i) => {
                                  if (c && i<3) {
                                    return <button className = "classOffers" onClick={() => this.props.changeProf(c.id)}> {c.name} </button>
                                  }
                                })}
                            </div>
                        </div>
                    </div>
                </div>
                <h2 className = 'TSR'> Top Student Reviews: </h2>
                    {classComms && classComms.map((c, i) => {
                      if (c) {
                        return <div className = "botRow">
                            <div className = "reviewInfo">
                                <h4> {c.date} </h4>
                                <h3> Overall: {c.overall} </h3>
                                <h3> Difficulty: {c.difficulty} </h3>
                            </div>
                            <div className = "reviewTarget">
                                <h4> Prof: {c.prof} </h4>
                                <h4> Semester Taken: {c.semester} </h4>
                                <h4> Grade Received: {c.grade} </h4>
                            </div>
                            <div className = "reviewContent">
                                <h4> {c.comment} </h4>
                                <button className = "upvotes" onClick={() => this.upVote(c.id)}> &#x1f44d;{c.up} </button>
                                <button className = "downvotes" onClick={() => this.downVote(c.id)}> &#x1f44e;{c.down} </button>
                            </div>
                        </div>
                      }
                  })}
            </div>
        );
    }
}

export default Class;


/*
MAIN - FIGURE OUT HOW TO GET PROF ID AUTOMATICALLY
1) need to add Up/Downvote Functionality
2) need to make backend real
3) need to link everything
*/
