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
                  data: res.data.sort(this.compare),
                })
                console.log(res.data)
            })
            .catch(e => console.log(e))
    }

    componentDidMount() {
      this.getInfo()
    }

    compare(a,b) {
      if (a.semester < b.semester)
        return -1;
      if (a.semester > b.semester)
        return 1;
      return 0;
    }

    compareLength(b,a) {
      if (a.length < b.length)
        return -1;
      if (a.length > b.length)
        return 1;
      return 0;
    }
    render() {
      const order = ['semester', 'dept', 'class_num', 'name', 'id', 'difficulty', 'quality',
      'alp', 'ns', 'cci', 'ss', 'sts', 'cz', 'ei', 'fl', 'qs', 'r', 'w'];


        return (
            <div style={{margin: '1%'}}>
              <h3 style={{textAlign: 'center', margin: '5%'}}>{this.props.email}</h3>

              {this.state.data.length > 0 &&
                <table>
                  <tr>
                    {order.map(key => {
                      return <th>{key}</th>
                    })}
                  </tr>
                  {this.state.data.map(d => {
                    return <tr style={{height: 50}}>
                      {order.map(key => <td
                        style={key == 'semester' || key == 'name' ? {width: '10%'} : {width: '4%'}}>
                        {d[key] == '1' ? '1' : (d[key] == '0' ? '' : d[key])}</td>)}
                      </tr>
                  })}
                </table>}
                </div>
        );
    }
}

export default Me;
