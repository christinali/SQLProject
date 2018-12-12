// Import libraries for making a component
import React from 'react';
import {Navbar, Nav, NavItem, NavDropdown, MenuItem} from 'react-bootstrap';


// Make a component
const navbar = {background: '#f2efe8'};
const Header = (props) => {


	return (
		<Navbar style={navbar} collapseOnSelect>
  <Navbar.Header>
    <Navbar.Brand>
      <a href="#brand">{props.headerText}</a>
    </Navbar.Brand>
    <Navbar.Toggle />
  </Navbar.Header>
  <Navbar.Collapse>

    <Nav pullLeft>
			{props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.homePage}>
				Home
			</NavItem>: <NavItem eventKey={1} href="#" onClick={props.homePage}>
				About Us
			</NavItem>}
			{props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.advanceSearchPage}>
				Advanced Search
			</NavItem>: <NavItem eventKey={1} href="#" onClick={props.advanceSearchPage}>
				About Us
			</NavItem>}
			{props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.fullRecPage}>
				Full Recommendations
			</NavItem>: <NavItem eventKey={1} href="#" onClick={props.fullRecPage}>
				About Us
			</NavItem>}
		</Nav>
		<Nav pullRight>
      {props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.logout}>
        Log Out
      </NavItem>: <NavItem eventKey={1} href="#" onClick={props.logout}>
        About Us
      </NavItem>}
    </Nav>
  </Navbar.Collapse>
</Navbar>


	);
};



// Make the component available to other parts of the app
export default Header;
