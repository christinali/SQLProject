import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';

class Prof extends Component {
    constructor() {
        super();
        this.state = {
            currID: 0,
            currProf: [],
            profComms: [],
        }
    }

    componentDidMount() {
        this.setState({
            currID: this.props.currProf,
        })
        this.getProfInfo(this.props.currProf)
    }

    getProfInfo(currID) {
        console.log(this.props.id);
        axios.get('http://localhost:5000/get-prof-info?prof_id=' + currID) //replace with this.props.currProf
            .then(res => {
                this.setState({
                  currProf: res.data,
                  profComms: res.data.comments,
                })
            })
            .catch(e => console.log(e))
    }

    upVote(id) {
      axios.post('http://localhost:5000/reviews/upvote?review_id=' + id)
          .then(res => console.log(res))
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
                              {currProf.overall != 0 ?
                                <StarRatings
                                    rating={currProf.overall}
                                    starDimension="40px"
                                    starSpacing="3px"
                                    starRatedColor="#FF8C00"
                                /> : <h3> No rating yet! </h3> }
                            </h2>
                            <h2> Difficulty:
                              {currProf.difficulty != 0 ?
                                <StarRatings
                                    rating={currProf.difficulty}
                                    starDimension="40px"
                                    starSpacing="3px"
                                    starRatedColor="#FF8C00"
                                /> : <h3> No rating yet! </h3> }
                            </h2>
                        </div>
                        <div className = "otherClasses">
                            <h2> Classes Taught Next Semester: </h2>
                            <div className = "classInfo">
                                {currProf.nextSemClasses && currProf.nextSemClasses.length === 0 && <h3> Not teaching next semester </h3>}
                                {currProf.nextSemClasses && currProf.nextSemClasses.map((c, i) => {
                                  if (c) {
                                    return <button className = "classOffers" key={i} onClick={() => this.props.changeClass(c.class_id)}> {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null}</button>
                                  }
                                })}
                            </div>
                            <h2> Previously Taught Classes: </h2>
                            <div className = "classInfo">
                                {currProf.classes && currProf.classes.length === 0 && <h3> No previously taught classes </h3>}
                                {currProf.classes && currProf.classes.map((c, i) => {
                                  if (c && i<3) {
                                    return <button className = "classOffers" key={i} onClick={() => this.props.changeClass(c.class_id)}> {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null}</button>
                                  }
                                })}
                            </div>
                        </div>
                    </div>
                </div>
                <h2 className = 'TSR'> <strong>Top Student Reviews: </strong></h2>
                    {profComms && profComms.map((c, i) => {
                      if (c && i < 3) {
                        if (i % 2) {
                          return <div className = "botRow">
                              <div className = "reviewInfo">
                                  <h3> <strong>Overall: </strong>{c.overall} </h3>
                                  <h3> <strong>Difficulty: </strong>{c.difficulty} </h3>
                              </div>
                              <div className = "reviewTarget">
                                  <h4> <strong>Class: </strong> <button className="revProf" onClick={() => this.props.changeClass(c.class_id)}> {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null} </button> </h4>
                                  <h4> <strong>Semester Taken: </strong>{c.semester} </h4>
                              </div>
                              <div className = "reviewContent">
                                  <h4> {c.text} </h4>
                                  <button className = "upvotes" onClick={() => this.upVote(c.id)}> &#x1f44d;{c.up} </button>
                                  <button className = "downvotes"> &#x1f44e;{c.down} </button>
                              </div>
                          </div>
                      }
                      else {
                        return <div className = "botRow2">
                            <div className = "reviewInfo">
                                <h3> <strong>Overall: </strong> {c.overall} </h3>
                                <h3> <strong>Difficulty: </strong> {c.difficulty} </h3>
                            </div>
                            <div className = "reviewTarget">
                                <h4> <strong>Class: </strong> <button className="revProf" onClick={() => this.props.changeClass(c.class_id)}> {c.dept}{c.num} - {c.name != null ? String(c.name).replace("\\u0026", "&") : null} </button> </h4>
                                <h4> <strong>Semester Taken: </strong>{c.semester} </h4>
                            </div>
                            <div className = "reviewContent">
                                <h4> {c.text} </h4>
                                <button className = "upvotes" onClick={() => this.upVote(c.id)}> &#x1f44d;{c.up} </button>
                                <button className = "downvotes"> &#x1f44e;{c.down} </button>
                            </div>
                        </div>
                        }
                      }
                  })}
                  {profComms.length === 0 ? <h3 className = 'noReviews'> Sorry! Seems like there are no reviews of this professor yet. </h3>
                    : <button className = "seeAll"> See all reviews... </button>
                  }
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
