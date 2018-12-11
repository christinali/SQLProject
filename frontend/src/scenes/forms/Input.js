import React from 'react';
import BasicInput from './BasicInput';
import ClassInput from './ClassInput';
import ContactInfo from './ContactInfo';



export default class Input extends React.Component {

  state = {
    step: 2,
    fieldValues : {
      fname : '',
      lname: '',
      gradyear: '',
      major: '',
      classes: [],
      email: '',
      password: '',
      user_id: ''
    }
  }
  saveValues = (fields) => {
    this.setState({
      step: this.state.step + 1,
      fieldValues: fields
    })
  }
  addClass = (fields) => {
    this.setState({
      step: this.state.step,
      fieldValues: fields
    })
  }
  previousStep = () => {
    this.setState({
      step: this.state.step - 1,
      fieldValues: this.state.fieldValues
    })
  }
  render() {
    return (
      <div>
      {(()=> {
        switch(this.state.step) {
          case 0:
            return <ContactInfo
                      fieldValues={this.state.fieldValues}
                      nextStep={this.nextStep}
                      saveValues={this.saveValues}
                      exit={this.props.exitToLogin}
                      app={this.props.app}
                    />;
          case 1:
            return <BasicInput
                      fieldValues={this.state.fieldValues}
                      nextStep={this.nextStep}
                      saveValues={this.saveValues}
                      exit={this.props.exitToLogin}
                    />;
          case 2:
            return <ClassInput
                    fieldValues={this.state.fieldValues}
                    saveValues={this.addClass}
                    previousStep={this.previousStep}
                    submitRegistration={this.submitRegistration}
                    exit={this.props.exitToLogin}
                  />;
          default:
            return null;
        }
      })()}
      </div>
    );
  }
}
