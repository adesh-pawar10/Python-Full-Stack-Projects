import React from 'react';
import ProductForm from '../components/Products/ProductForm';
import ProductList from '../components/Products/ProductList';
import './ProductsPage.css';

const ProductsPage = () => (
  <div className="page-container">
    <h1>Products</h1>
    <ProductForm />
    <ProductList />
  </div>
);

export default ProductsPage;
