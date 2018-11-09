import React, { Component } from 'react';
import { UserCard } from 'react-ui-cards';
import StarRatings from 'react-star-ratings';
import Plot from 'react-plotly.js';
import christina from '../christina.jpg';

class Class extends Component {
    render() {
        let graph1 = (
            <Plot
                data={[
                    {type: 'bar', x: ["Compsci 202", "Compsci 203", "Compsci 301"], y: [67, 100, 42]},
                ]}
                layout={ {paper_bgcolor: 'rgba(0,0,0,0)',
                    plot_bgcolor: 'rgba(0,0,0,0)',  width: 420, height: 350} }

            />
        );
        return (
            <div>
                <div style={{marginLeft: '3%', marginTop: '0.1%', alignContent: 'center'}}>
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
                <div style={{zIndex: 34, position: 'fixed', top: '10%', left: '44%'}}>
                    {graph1}

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
                </div>
            </div>
        );
    }
}

export default Class;
