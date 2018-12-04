import React from 'react';
import firebase from 'firebase';

const firebaseConfig = {
    apiKey: "AIzaSyDfXgvgX2_eyPam6O3eenzLTJHrwHc2tdc",
    authDomain: "sqlproject-b318c.firebaseapp.com",
    databaseURL: "https://sqlproject-b318c.firebaseio.com",
    projectId: "sqlproject-b318c",
    storageBucket: "sqlproject-b318c.appspot.com",
    messagingSenderId: "612693141535"
};


const app = firebase.initializeApp(firebaseConfig);

export default class Login extends React.Component {
    state = { email: '', password: '' };

    handleLogin = () => {
    const { email, password } = this.state;
    app
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then(async user => {
    if (user) {
        this.props.login()
        alert("You logged in successfully")
    }
})
.catch(e => {
    alert(e.message);
    console.log(e)
});
};

handleSignup = () => {
    const { email, password } = this.state;
    app
        .auth()
        .createUserWithEmailAndPassword(email, password)
        .then(async user => {
        if (user) {
            this.props.login()
            alert("You signed up successfully")
        }
    })
.catch(e => {
    alert(e.message);
    console.log(e);
});
};

render = () => {
    const { email, password } = this.state;
    return (
    <div>
        <label>Email:
        <input type="text" value={this.state.email} onChange={e => this.setState({email: e.target.value})} />
        </label>
        <label>Password:
        <input type="text" value={this.state.password} onChange={e => this.setState({password: e.target.value})} />
        </label>
        <button onClick={this.handleLogin}>Log in</button>
        <button onClick={this.handleSignup}>Sign up</button>
    </div>
    );
};
}

