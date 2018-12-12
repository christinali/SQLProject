// Import libraries for making a component
import React from 'react';
import {Navbar, Nav, NavItem, NavDropdown, MenuItem, OverlayTrigger, Popover, Button} from 'react-bootstrap';


// Make a component
const navbar = {background: '#f2efe8'};
const popoverBottom = (
  <Popover id="popover-positioned-bottom" title="Who are we?">
    We are a team of students enrolled in CS316: Databases at Duke University,
		and this is our final project. Many of us were frustrated with ambiguities
		and uncertainties	in enrolling for courses, so we designed this bookbagging
		recommender application with students in mind. We hope you find it useful!
  </Popover>
);
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
			</NavItem>: ''}
			{props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.me}>
				Me
			</NavItem>: ''}
			{props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.advanceSearchPage}>
				Advanced Search
			</NavItem>: ''}
			{props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.fullRecPage}>
				Full Recommendations
			</NavItem>: ''}
		</Nav>
		<Nav pullRight>
      {props.loggedin ? <NavItem eventKey={1} href="#" onClick={props.logout}>
        Log Out
      </NavItem>: <NavItem><OverlayTrigger trigger="click" placement="bottom" overlay={popoverBottom}>
      <Button>About Us</Button>
    </OverlayTrigger></NavItem>}
    </Nav>
  </Navbar.Collapse>
</Navbar>


	);
};



// Make the component available to other parts of the app
export default Header;
