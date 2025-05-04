import React, { useEffect, useState } from 'react';
import api from '../../api/api';
import './OrderList.css';

const OrderList = () => {
  const [orders, setOrders] = useState([]);

  const fetchOrders = async () => {
    try {
      const res = await api.get('/getOrders');
      setOrders(res.data.data);
    } catch (err) {
      console.error('Error fetching orders', err);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  const deleteOrder = async (id) => {
    try {
      await api.post('/deleteOrder', { order_id: id });
      fetchOrders();
    } catch (err) {
      console.error('Error deleting order', err);
    }
  };

  return (
    <div className="order-list">
      <h2>Order List</h2>
      <ul>
        {orders.map(o => (
          <li key={o.order_id} className="order-item">
            {o.customer_name} - ${o.total}
            <button onClick={() => deleteOrder(o.order_id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default OrderList;