import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import firebase from 'firebase';
import StarRatings from 'react-star-ratings';
import Select from 'react-select';

var firebaseConfig = {
    apiKey: "AIzaSyDfXgvgX2_eyPam6O3eenzLTJHrwHc2tdc",
    authDomain: "sqlproject-b318c.firebaseapp.com",
    databaseURL: "https://sqlproject-b318c.firebaseio.com",
    projectId: "sqlproject-b318c",
    storageBucket: "sqlproject-b318c.appspot.com",
    messagingSenderId: "612693141535"
};


const app = firebase.initializeApp(firebaseConfig);

class App extends Component {
    constructor() {
        super();
        this.state = {
            className: '',
            difficulty: 0,
            quality: 0,
            sem: null,
            code: null,
        }
        this.object = {};
    }

    changeRating( newRating, name ) {
        this.setState({
            [name]: newRating
        });
        this.object[name] = newRating;
    }

    submit() {
        this.submitToFirebase();
        this.setState({
            className: '',
            difficulty: 0,
            quality: 0,
            sem: null,
        })
        this.object = {};
    }

    submitToFirebase() {
        app
            .database()
            .ref(`data/`)
            .push(this.object);
    }

    handleInputChange(e) {
        this.setState({
            sem: e.value,
        });
        this.object.sem = e.value;
    }

    handleCodeChange(e) {
        this.setState({
            code: e.value,
        });
        this.object.code = e.value;
    }

    updateClass(e) {
        this.object.class = e.target.value;
        this.setState({className: e.target.value})
    }

    render() {
        let codes = "Arabic,ARABIC\n" +
            "Art History,ARTHIST\n" +
            "Biochemistry,BIOCHEM\n" +
            "Biology,BIOLOGY\n" +
            "Biomedical Engineering,BME\n" +
            "Civil and Environmental Egr,CEE\n" +
            "Cell Biology,CELLBIO\n" +
            "Chemistry,CHEM\n" +
            "Child Policy,CHILDPOL\n" +
            "Chinese,CHINESE\n" +
            "Classical Studies,CLST\n" +
            "Cell and Molecular Biology,CMB\n" +
            "Computer Science,COMPSCI\n" +
            "Cultural Anthropology,CULANTH\n" +
            "Documentary Studies,DOCST\n" +
            "Drama,DRAMA\n" +
            "Dutch,DUTCH\n" +
            "Electrical &amp; Computer Egr,ECE\n" +
            "Economics,ECON\n" +
            "Education,EDUC\n" +
            "Engineering,EGR\n" +
            "Energy,ENERGY\n" +
            "English,ENGLISH\n" +
            "Environment,ENVIRON\n" +
            "Earth and Ocean Sciences,EOS\n" +
            "Study of Ethics,ETHICS\n" +
            "Evolutionary Anthropology,EVANTH\n" +
            "Finance,FINANCE\n" +
            "French,FRENCH\n" +
            "German,GERMAN\n" +
            "Global Health,GLHLTH\n" +
            "Greek,GREEK\n" +
            "Graduate Studies,GS\n" +
            "Gender Sexuality &amp; Feminist St,GSF\n" +
            "Hebrew,HEBREW\n" +
            "Hindi,HINDI\n" +
            "History,HISTORY\n" +
            "Health Policy,HTHPOL\n" +
            "Hungarian,HUNGARN\n" +
            "Internatl Comparative Studies,ICS\n" +
            "Interdisciplinary,IND\n" +
            "Italian,ITALIAN\n" +
            "Jewish Studies,JEWISHST\n" +
            "Japanese,JPN\n" +
            "Korean,KOREAN\n" +
            "Latin American Studies,LATAMER\n" +
            "Latin,LATIN\n" +
            "Linguistics,LINGUIST\n" +
            "Literature,LIT\n" +
            "Liberal Studies,LS\n" +
            "Management,MANAGEMT\n" +
            "Marketing,MARKETNG\n" +
            "Master of Arts in Teaching,MAT\n" +
            "Mathematics,MATH\n" +
            "Mechanical Engr/Materials Sci,ME\n" +
            "Economics,MGRECON\n" +
            "MPS,MPS\n" +
            "Music,MUSIC\n" +
            "Neurology,NEURO\n" +
            "Neurobiology,NEUROBIO\n" +
            "Neuroscience,NEUROSCI\n" +
            "Philosophy,PHIL\n" +
            "Physician Assistant Program,PHYASST\n" +
            "Physical Education,PHYSEDU\n" +
            "Physics,PHYSICS\n" +
            "Policy Journalism and Media St,PJMS\n" +
            "Practice-Oriented Education,POE\n" +
            "Polish,POLISH\n" +
            "Political Science,POLSCI\n" +
            "Portuguese,PORTUGUE\n" +
            "Philosophy, Politics, and Econ,PPE\n" +
            "Psychiatry,PSC\n" +
            "Psychology,PSY\n" +
            "Public Policy,PUBPOL\n" +
            "Religion,RELIGION\n" +
            "Research,RESEARCH\n" +
            "Human Rights,RIGHTS\n" +
            "Romanian,ROMANIAN\n" +
            "Romance Languages,ROMLANG\n" +
            "Romance Studies,ROMST\n" +
            "Radiation Oncology,RON\n" +
            "Russian,RUSSIAN\n" +
            "Social Entrepreneurship,SOCENT\n" +
            "Sociology,SOCIOL\n" +
            "Spanish,SPANISH\n" +
            "Statistical Science,STA\n" +
            "Theater Studies,THEATRST\n" +
            "Thesis,THESIS\n" +
            "Visual Studies,VISUALST\n" +
            "Writing,WRITING";
        codes = codes.split("\n");
        codes = codes.map(sem => {
            sem = sem.split(",")[1];
            return {label: sem, value: sem};
        });
        const semesters = ["Freshman Fall", "Freshman Spring",
            "Sophomore Fall", "Sophomore Spring",
            "Junior Fall", "Junior Spring",
            "Senior Fall", "Senior Spring"
        ];
        const options = semesters.map(sem => {
            return {label: sem, value: sem};
        });
        return (
            <div className="App">
                <h5>Class Department</h5>
                <Select
                    selectedValue={this.state.code}
                    name="colors"
                    options={codes}
                    className="basic-multi-select"
                    classNamePrefix="select"
                    onChange={e => this.handleCodeChange(e)}
                />
                <h5>Class Number</h5>
                <textarea value={this.state.className} onChange={e => this.updateClass(e)} />

                <h5>When did you take this class?</h5>

                <Select
                    selectedValue={this.state.sem}
                    name="colors"
                    options={options}
                    className="basic-multi-select"
                    classNamePrefix="select"
                    onChange={e => this.handleInputChange(e)}
                />
                <h5>Rate your difficulty</h5>
                <StarRatings
                    rating={this.state.difficulty}
                    starRatedColor="blue"
                    changeRating={rating => this.changeRating(rating, "difficulty")}
                    numberOfStars={5}
                    name='rating'
                />
                <br/>
                <h5>Rate the quality of the class</h5>
                <StarRatings
                    rating={this.state.quality}
                    starRatedColor="blue"
                    changeRating={rating => this.changeRating(rating, "quality")}
                    numberOfStars={5}
                    name='rating'
                />
                <br/> <br/>
                <button onClick={() => this.submit()} style={{width: 100, height: 50}}>Submit</button>
            </div>
        );
    }
}

export default App;
