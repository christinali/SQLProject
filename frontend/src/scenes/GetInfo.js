import React, { Component } from 'react';
import axios from 'axios';

class GetInfo extends React.Component {
    constructor() {
        super();
        this.state = {
            id: null, //whatever the user login id is
            currClass: null,
            currProf: null,
            Treqs: null,
            Majors: null
        }
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

    render() {
        const currClass = this.state.currClass;
        const currProf = this.state.currProf;
        const Treqs = this.state.Treqs;
        const Majors = this.state.Majors;
        return (
            <div>
                <div>
                  <button onClick={this.props.logout}>Log Out</button>
                </div>
                <label>id:
                    <input type="text" value={this.state.email} onChange={e => this.setState({id: e.target.value})} />
                </label>
                <button onClick={() => this.getTReqs()}>Get Treqs</button>
                <button onClick={() => this.getClass()}>Get Class</button>
                <button onClick={() => this.getProf()}>Get Prof</button>

                <div className = 'Top3Recs'>
                    <h2> Top 3 Recommended Classes: </h2>
                    <div className = 'TReqsAll'style={{display: 'flex', flexDirection: 'row'}}>
                        {Treqs && <div className = 'TReqsComp'>
                            <h1> {Treqs[0].dept}{Treqs[0].num} - {Treqs[0].name} </h1>
                            <h2> Overall: {Treqs[0].overall} </h2>
                            <h2> Difficulty: {Treqs[0].difficulty} </h2>
                            <h4> Treqs Satisfied: {Treqs[1].satisfiesNeeded} </h4>
                        </div>}

                        {Treqs && <div className = 'TReqsComp'>
                            <h1> {Treqs[1].dept}{Treqs[1].num} - {Treqs[1].name} </h1>
                            <h2> Overall: {Treqs[1].overall} </h2>
                            <h2> Difficulty: {Treqs[1].difficulty} </h2>
                            <h4> Treqs Satisfied: {Treqs[1].satisfiesNeeded} </h4>
                        </div>}

                        {Treqs && <div className = 'TReqsComp'>
                            <h1> {Treqs[2].dept}{Treqs[2].num} - {Treqs[2].name} </h1>
                            <h2> Overall: {Treqs[2].overall} </h2>
                            <h2> Difficulty: {Treqs[2].difficulty} </h2>
                            <h4> Treqs Satisfied: {Treqs[2].satisfiesNeeded} </h4>
                        </div>}
                    </div>
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
                </div>
            </div>
        );
    }
}

export default GetInfo;
