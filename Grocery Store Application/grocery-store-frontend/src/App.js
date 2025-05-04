import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import ProductsPage from './pages/ProductsPage';
import OrdersPage from './pages/OrdersPage';
import UOMsPage from './pages/UOMsPage';
import './styles/global.css';

const App = () => (
  <Router>
    <Navbar />
    <Routes>
      <Route path="/" element={<ProductsPage />} />
      <Route path="/orders" element={<OrdersPage />} />
      <Route path="/uoms" element={<UOMsPage />} />
    </Routes>
  </Router>
);

export default App;
