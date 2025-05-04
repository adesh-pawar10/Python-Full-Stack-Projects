import React from 'react';
import UOMForm from '../components/UOMs/UOMForm';
import UOMList from '../components/UOMs/UOMList';
import './UOMsPage.css';

const UOMsPage = () => (
  <div className="page-container">
    <h1>UOMs</h1>
    <UOMForm />
    <UOMList />
  </div>
);

export default UOMsPage;
