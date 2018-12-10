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
/*<div style={{marginLeft: '3%', marginTop: '0.1%', alignContent: 'center'}}>
    <UserCard
        cardClass='float'
        header='https://i.imgur.com/w5tX1Pn.jpg'
        avatar={christina}
        name='Christina Li'
        positionName='Computer Science'
        stats={[
            {
                name: 'classes',
                value: 2
            },
            {
                name: 'rating',
                value: 3.74
            }
        ]}
    />
</div>
<div style={{position: 'fixed', zIndex: 36, top: '68.3%', left: '70%'}}>
    <StarRatings
                 rating={1}
                 starRatedColor="red"
                 numberOfStars={5}
                 name='rating'
                 starDimension={20}
    />
</div>
<div style={{zIndex: 35, width: '44%', position: 'fixed', top: '57%', left: '53%',
    textAlign: 'center'}}>
    <h4>Top Review</h4>
    <div style={{lineHeight: 0.8, marginBottom: '10%'}}>
        <p style={{width: '30%', fontWeight: 'bold'}}>Salil Mitra</p>
        <p style={{width: '30%'}}>Compsci 79</p>
    </div>
    <p style={{fontSize: 15}}>If I could, I would give her a 0/5. Horrible class. You're expected to learn everything by your own in your own time. If you really want to learn computer science, you might as well learn by yourself because Christina sure won't teach you</p>

</div>
<div style={{zIndex: 34, position: 'fixed', top: '5%', left: '50%'}}>
    <StarRatings
        rating={3.7}
        starRatedColor="#FF8C00"
        numberOfStars={5}
        name='rating'
        starDimension={50}
    />
</div>
<div>
    <div style={{display: 'flex', lineHeight: 1}}>
        <p style={{marginRight: '1%', marginLeft: '0.5%', width: '14%'}}>Fall 2018:</p>
        <p style={{marginRight: '1%', color: 'blue', textDecoration: 'underline'}}>Compsci 215</p>
        <p style={{color: 'blue', textDecoration: 'underline'}}>Compsci 331</p>
    </div>
    <div style={{display: 'flex', lineHeight: 1}}>
        <p style={{marginRight: '1%', marginLeft: '0.5%', width: '14%'}}>Spring 2018:</p>
        <p style={{color: 'blue', textDecoration: 'underline'}}>Compsci 621</p>
    </div>
    <div style={{display: 'flex', lineHeight: 1}}>
        <p style={{marginRight: '1%', marginLeft: '0.5%', width: '14%'}}>Fall 2017:</p>
        <p style={{marginRight: '1%', color: 'blue', textDecoration: 'underline'}}>Compsci 102</p>
        <p style={{color: 'blue', textDecoration: 'underline'}}>Compsci 312</p>
    </div>
    <div style={{display: 'flex', lineHeight: 1}}>
        <p style={{marginRight: '1%', marginLeft: '0.5%', width: '14%'}}>Fall 2016:</p>
        <p style={{marginRight: '1%', color: 'blue', textDecoration: 'underline'}}>Compsci 104</p>
        <p style={{color: 'blue', textDecoration: 'underline'}}>Compsci 106</p>
    </div>
    <div style={{display: 'flex', lineHeight: 1}}>
        <p style={{marginRight: '1%', marginLeft: '0.5%', width: '14%'}}>Spring 2016:</p>
        <div style={{display: 'flex', flexWrap: 'wrap', width: '40%'}}>
            <p style={{marginRight: '1.5%', color: 'blue', textDecoration: 'underline'}}>Compsci 202</p>
            <p style={{marginRight: '1%', color: 'blue', textDecoration: 'underline'}}>Compsci 203</p>
            <p style={{color: 'blue', textDecoration: 'underline'}}>Compsci 301</p>
        </div>
    </div>
</div>*/
