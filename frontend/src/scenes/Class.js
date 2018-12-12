import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import StarRatings from 'react-star-ratings';

class Class extends Component {
    constructor() {
        super();
        this.state = {
            currID: 0,
            currClass: [],
            classComms: [],
        }

    }

    componentDidMount() {
        this.setState({
            currID: this.props.currClass,
        })
        this.getClassInfo(this.props.currClass)
    }

    getClassInfo(currID) {
        axios.get('http://localhost:5000/get-class-info?class_id=' + currID) //this.props.currClass
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

    reveal() {
      var x = document.getElementsByClassName("botRow2");
      var y = document.getElementById("seeAll");
      var z = document.getElementById("hideAll");
      var i;
      for (i = 0; i < x.length; i++) {
        if (x[i].style.display === "none") {
          x[i].style.display = "flex";
        }
      }
      if (y.style.display === "flex") {
        y.style.display = "none";
      }
      if (z.style.display === "none") {
        z.style.display = "flex";
      }
    }

    hide() {
      var x = document.getElementsByClassName("botRow2");
      var y = document.getElementById("seeAll");
      var z = document.getElementById("hideAll");
      var i;
      for (i = 0; i < x.length; i++) {
        if (x[i].style.display === "flex") {
          x[i].style.display = "none";
        }
      }
      if (y.style.display === "none") {
        y.style.display = "flex";
      }
      if (z.style.display === "flex") {
        z.style.display = "none";
      }
    }

    render() {
        const currClass = this.state.currClass;
        const classComms = this.state.classComms;

        return (
            <div className="Overall">
                <div className = "topRow">
                    <div className = "topLeft">
                        <h1> {currClass.dept}{currClass.class_num}: </h1>
                        <h1> {currClass.name != null ? String(currClass.name).replace("\\u0026", "&") : null} </h1>
                    </div>
                    <div className = "topRight">
                        <div className = "scores">
                            <h2> Overall:
                            {currClass.overall != 0 ?
                              <StarRatings
                                  rating={currClass.overall}
                                  starDimension="40px"
                                  starSpacing="3px"
                                  starRatedColor="#FF8C00"
                              /> : <h3> No rating yet </h3> }
                            </h2>
                            <h2> Difficulty:
                                {currClass.difficulty != 0 ?
                                  <StarRatings
                                      rating={currClass.difficulty}
                                      starDimension="40px"
                                      starSpacing="3px"
                                      starRatedColor="#FF8C00"
                                  /> : <h3> No rating yet </h3> }
                            </h2>
                        </div>
                        <div className = "otherClasses">
                            <h2> Next Semester Professor: </h2>
                            <div className = "profInfo">
                                {currClass.nextSemProfs && currClass.nextSemProfs.length === 0 && <h3> Not being taught next semester </h3>}
                                {currClass.nextSemProfs && currClass.nextSemProfs.map((c, i) => {
                                  if (c) {
                                    return <button className = "classOffers" onClick={() => this.props.changeProf(c.prof_id)}> {c.prof_name} </button>
                                  }
                                })}
                            </div>
                            <h2> Previous Professors: </h2>
                            <div className = "classInfo">
                                {currClass.profs && currClass.profs.length === 0 && <h3> No past professors </h3>}
                                {currClass.profs && currClass.profs.map((c, i) => {
                                  if (c && i<3) {
                                    return <button className = "classOffers" onClick={() => this.props.changeProf(c.prof_id)}> {c.prof_name} </button>
                                  }
                                })}
                            </div>
                        </div>
                    </div>
                </div>
                <h2 className = 'TSR'> Top Student Reviews: </h2>
                    {classComms && classComms.map((c, i) => {
                      if (c) {
                        if (i < 3) {
                          return <div className = "botRow">
                              <div className = "reviewInfo">
                                  <h3> <strong>Overall: </strong>
                                      {c.overall != 0 ?
                                        <StarRatings
                                            rating={c.overall}
                                            starDimension="22px"
                                            starSpacing="3px"
                                            starRatedColor="#FF8C00"
                                        /> : <h4> No rating yet </h4> }
                                  </h3>
                                  <h3> <strong>Difficulty: </strong>
                                      {c.difficulty != 0 ?
                                        <StarRatings
                                            rating={c.difficulty}
                                            starDimension="22px"
                                            starSpacing="3px"
                                            starRatedColor="#FF8C00"
                                        /> : <h4> No rating yet </h4> }
                                  </h3>
                              </div>
                              <div className = "reviewTarget">
                                  <h4>  <strong>Prof: </strong><button className = "revProf" onClick={() => this.props.changeProf(c.prof_id)}> {c.prof} </button> </h4>
                                  <h4> <strong>Semester Taken: </strong>{c.semester} </h4>
                              </div>
                              <div className = "reviewContent">
                                  <h4> {c.text} </h4>
                                  <button className = "upvotes" onClick={() => this.upVote(c.id)}> &#x1f44d;{c.up} </button>
                                  <button className = "downvotes" onClick={() => this.downVote(c.id)}> &#x1f44e;{c.down} </button>
                              </div>
                          </div>
                        }
                        else {
                          return <div className = "botRow2" style={{display:"none"}}>
                              <div className = "reviewInfo">
                                  <h3> <strong>Overall: </strong>
                                      {c.overall != 0 ?
                                        <StarRatings
                                            rating={c.overall}
                                            starDimension="22px"
                                            starSpacing="3px"
                                            starRatedColor="#FF8C00"
                                        /> : <h4> No rating yet </h4> }
                                  </h3>
                                  <h3> <strong>Difficulty: </strong>
                                      {c.difficulty != 0 ?
                                        <StarRatings
                                            rating={c.difficulty}
                                            starDimension="22px"
                                            starSpacing="3px"
                                            starRatedColor="#FF8C00"
                                        /> : <h4> No rating yet </h4> }
                                  </h3>
                              </div>
                              <div className = "reviewTarget">
                                  <h4>  <strong>Prof: </strong><button className = "revProf" onClick={() => this.props.changeProf(c.prof_id)}> {c.prof} </button> </h4>
                                  <h4> <strong>Semester Taken: </strong>{c.semester} </h4>
                              </div>
                              <div className = "reviewContent">
                                  <h4> {c.text} </h4>
                                  <button className = "upvotes" onClick={() => this.upVote(c.id)}> &#x1f44d;{c.up} </button>
                                  <button className = "downvotes" onClick={() => this.downVote(c.id)}> &#x1f44e;{c.down} </button>
                              </div>
                          </div>
                        }
                      }
                  })}
                  {classComms.length === 0 ? <h3 className = 'noReviews'> Sorry! Seems like there are no reviews of this class yet. </h3>
                    : <div>
                        <button className = "seeAll" id="seeAll" style = {{display:'flex'}} onClick={() => this.reveal()}> See all reviews... </button>
                        <button className = "seeAll" id="hideAll" style = {{display:'none'}} onClick={() => this.hide()}> Hide all reviews... </button>
                      </div>
                  }
            </div>
        );
    }
}

export default Class;
