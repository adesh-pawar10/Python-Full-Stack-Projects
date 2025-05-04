import React, { useState, useEffect } from 'react';
import api from '../../api/api';
import './ProductForm.css';

const ProductForm = () => {
  const [form, setForm] = useState({ name: '', uom_id: '', price_per_unit: '' });
  const [uoms, setUoms] = useState([]);

  useEffect(() => {
    api.get('/getUOMs').then(res => setUoms(res.data.data));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!form.name || !form.uom_id || !form.price_per_unit) {
        alert('Please fill all fields');
        return;
      }
      await api.post('/insertProduct', form);
      setForm({ name: '', uom_id: '', price_per_unit: '' });
    } catch (err) {
      console.error('Error inserting product', err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="product-form">
      <input value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} placeholder="Product name" />
      <input type="number" value={form.price_per_unit} onChange={e => setForm({ ...form, price_per_unit: e.target.value })} placeholder="Price" />
      <select value={form.uom_id} onChange={e => setForm({ ...form, uom_id: e.target.value })}>
        <option value="">Select UOM</option>
        {uoms.map(u => <option key={u.uom_id} value={u.uom_id}>{u.uom_name}</option>)}
      </select>
      <button type="submit">Add Product</button>
    </form>
  );
};

export default ProductForm;