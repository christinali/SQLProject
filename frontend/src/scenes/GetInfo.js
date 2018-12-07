import React, { Component } from 'react';
import axios from 'axios';

class GetInfo extends Component {
    constructor() {
        super();
        this.state = {
            id: null,
            currClass: null,
            currProf: null,
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

    render() {
        const currClass = this.state.currClass;
        const currProf = this.state.currProf;
        return (
            <div>
                <label>id:
                    <input type="text" value={this.state.email} onChange={e => this.setState({id: e.target.value})} />
                </label>
                <button onClick={() => this.getClass()}>Get Class</button>
                <button onClick={() => this.getProf()}>Get Prof</button>
                <div style={{display: 'flex', flexDirection: 'row'}}>
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
