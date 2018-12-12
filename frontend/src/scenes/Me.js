import React, { Component } from 'react';
import axios from 'axios';

class Me extends Component {
    constructor() {
        super();
        this.state = {
            data: []
        }
    }

    getInfo(email) {
        axios.get('http://localhost:5000/get-user-classes?email=' + this.props.email) //replace with this.props.currProf
            .then(res => {
                this.setState({
                  data: res.data,
                })
            })
            .catch(e => console.log(e))
    }

    componentDidMount() {
    }

    render() {

        return (
            <div className="Overall">
              <p>Me</p>
              <p>{this.props.email}</p>
            </div>
        );
    }
}

export default Me;
