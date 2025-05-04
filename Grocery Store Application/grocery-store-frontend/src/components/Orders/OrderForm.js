import React, { useState } from 'react';
import api from '../../api/api';
import './OrderForm.css';

const OrderForm = () => {
  const [form, setForm] = useState({ customer_name: '', total: '', datetime: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!form.customer_name || !form.total || !form.datetime) {
        alert('All fields are required');
        return;
      }
      await api.post('/insertOrder', form);
      setForm({ customer_name: '', total: '', datetime: '' });
    } catch (err) {
      console.error('Error inserting order', err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="order-form">
      <input placeholder="Customer Name" value={form.customer_name} onChange={e => setForm({ ...form, customer_name: e.target.value })} />
      <input placeholder="Total" type="number" value={form.total} onChange={e => setForm({ ...form, total: e.target.value })} />
      <input placeholder="Datetime" type="datetime-local" value={form.datetime} onChange={e => setForm({ ...form, datetime: e.target.value })} />
      <button type="submit">Add Order</button>
    </form>
  );
};

export default OrderForm;