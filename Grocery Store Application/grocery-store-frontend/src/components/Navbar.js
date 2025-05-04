import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => (
  <nav className="navbar">
    <Link to="/">Products</Link>
    <Link to="/orders">Orders</Link>
    <Link to="/uoms">UOMs</Link>
  </nav>
);

export default Navbar;