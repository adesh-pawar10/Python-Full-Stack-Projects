import React, { useEffect, useState } from 'react';
import api from '../../api/api';
import './ProductList.css';

const ProductList = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const res = await api.get('/getProducts');
      setProducts(res.data.data);
    } catch (err) {
      console.error('Error fetching products', err);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const deleteProduct = async (id) => {
    try {
      await api.post('/deleteProduct', { product_id: id });
      fetchProducts();
    } catch (err) {
      console.error('Error deleting product', err);
    }
  };

  return (
    <div className="product-list">
      <h2>Products</h2>
      <ul>
        {products.map(p => (
          <li key={p.product_id} className="product-item">
            {p.name} - ${p.price_per_unit}
            <button onClick={() => deleteProduct(p.product_id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;