import React, { Component } from 'react';
import axios from 'axios';

class Me extends Component {
    constructor() {
        super();
        this.state = {
            testing: []
        }
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
