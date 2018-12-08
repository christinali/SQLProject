import React from 'react';
import BasicInput from './BasicInput';
import ClassInput from './ClassInput';



export default class Input extends React.Component {

  state = {
    step: 1,
    fieldValues : {
      fname : '',
      lname: '',
      gradyear: '',
      major: '',
      classes: []
    }
  }
  saveValues = (fields) => {
    this.setState({
      step: this.state.step + 1,
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
                    saveValues={this.saveValues}
                    previousStep={this.previousStep}
                    submitRegistration={this.submitRegistration}
                  />;
          default:
            return null;
        }
      })()}
      </div>
    );
  }
}
