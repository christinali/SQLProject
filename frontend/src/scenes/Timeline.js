import React, { Component } from 'react';
import { UserCard } from 'react-ui-cards';
import Plot from 'react-plotly.js';
import StarRatings from 'react-star-ratings';
import Checkbox from 'rc-checkbox';


class Timeline extends Component {
    render() {
        let graph1 = (
            <Plot
                data={[
                    {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
                ]}
                layout={ {paper_bgcolor: 'rgba(0,0,0,0)',
                    plot_bgcolor: 'rgba(0,0,0,0)', width: 320, height: 240, title: 'A Fancy Plot'} }

            />
        );
        let graph2 = (
            <Plot
                data={[
                    {
                        x: [1, 2, 3],
                        y: [2, 6, 3],
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: {color: 'red'},
                    },
                    {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
                ]}
                layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
            />
        );
        let graph3 = (
            <Plot
                data={[
                    {
                        x: [1, 2, 3],
                        y: [2, 6, 3],
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: {color: 'red'},
                    },
                    {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
                ]}
                layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
            />
        );
        let graph4 = (
            <Plot
                data={[
                    {
                        x: [1, 2, 3],
                        y: [2, 6, 3],
                        type: 'scatter',
                        mode: 'lines+points',
                        marker: {color: 'red'},
                    },
                    {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
                ]}
                layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
            />
        );
        return (
            <div className="App">
                <div style={{zIndex: 34, position: 'fixed', top: '76%', left: '9%'}}>
                <StarRatings
                    rating={4.7}
                    starRatedColor="green"
                    numberOfStars={5}
                    name='rating'
                    starDimension={30}
                />
                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '76%', left: '31%'}}>
                    <StarRatings
                        rating={3.5}
                        starRatedColor="#FF8C00"
                        numberOfStars={5}
                        name='rating'
                        starDimension={30}
                    />
                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '76%', left: '53%'}}>
                    <StarRatings
                        rating={2.7}
                        starRatedColor="#FF8C00"
                        numberOfStars={5}
                        name='rating'
                        starDimension={30}
                    />
                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '76%', left: '75.5%'}}>
                    <StarRatings
                        rating={2.3}
                        starRatedColor="red"
                        numberOfStars={5}
                        name='rating'
                        starDimension={30}
                    />
                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '82%', left: '23%'}}>
                    <Checkbox style={{zoom: 2}}
                              name="my-checkbox"
                              onChange={() => console.log("Change")}
                              disabled={false}
                    />

                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '82%', left: '45%'}}>
                    <Checkbox style={{zoom: 2}}
                              name="my-checkbox"
                              defaultChecked
                              onChange={() => console.log("Change")}
                              disabled={false}
                    />

                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '82%', left: '67.5%'}}>
                    <Checkbox style={{zoom: 2}}
                              name="my-checkbox"
                              onChange={() => console.log("Change")}
                              disabled={false}
                    />

                </div>
                <div style={{zIndex: 34, position: 'fixed', top: '82%', left: '89%'}}>
                    <Checkbox style={{zoom: 2}}
                              name="my-checkbox"
                              onChange={() => console.log("Change")}
                              disabled={false}
                    />

                </div>
                <header className="App-header">
                    <div>
                        <h2>Classes taken</h2>
                        <div id="container">
                            <div class="box1">
                                <h4>Fall 2016</h4>
                                <p>Compsci 101</p>
                            </div>
                            <div class="box2">
                                <h4>Spring 2017</h4>
                                <p>Compsci 210</p>
                            </div>
                            <div class="box3">
                                <h4>Fall 2017</h4>
                                <p>Compsci 230</p>
                            </div>
                            <div class="box4">
                                <h4>Fall 2018</h4>
                                <p>Compsci 316</p>
                            </div>
                            <span class="stretch"></span>
                        </div>
                    </div>
                    <div class="taken">
                        <h2>Recommended for Spring 2019</h2>
                    </div>
                    <div class="card-container">
                        <UserCard
                            style={{width: '25%'}}
                            header='https://i.imgur.com/w5tX1Pn.jpg'
                            name='Compsci 250'
                        positionName='Tyler Bletch'
                        stats={[
                            {
                                name: 'Students taken Junior Spring',
                                value: 210
                            },
                            {
                                name: 'stars',
                                value: 4.7
                            }
                        ]}
                        />
                        <UserCard
                            style={{width: '25%'}}
                            header='https://i.imgur.com/w5tX1Pn.jpg'
                            name='Compsci 330'
                            positionName='Bruce Donald'
                            stats={[
                                {
                                    name: 'Students taken Junior Spring',
                                    value: 160
                                },
                                {
                                    name: 'stars',
                                    value: 3.5
                                }
                            ]}
                        />
                        <UserCard
                            style={{width: '25%'}}
                            header='https://i.imgur.com/w5tX1Pn.jpg'
                            name='Compsci 308'
                            positionName='Robert Duvall'
                            stats={[
                                {
                                    name: 'Students taken Junior Spring',
                                    value: 130
                                },
                                {
                                    name: 'stars',
                                    value: 2.7
                                }
                            ]}
                        />
                        <UserCard
                            style={{width: '25%'}}
                            header='https://i.imgur.com/w5tX1Pn.jpg'
                            name='Compsci 350'
                            positionName='Tyler Bletch'
                            stats={[
                                {
                                    name: 'Students taken Junior Spring',
                                    value: 40
                                },
                                {
                                    name: 'stars',
                                    value: 2.3
                                }
                            ]}
                        />
                    </div>
                </header>
            </div>
        );
    }
}

export default Timeline;
