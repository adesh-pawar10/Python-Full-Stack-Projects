import React from 'react';
import OrderForm from '../components/Orders/OrderForm';
import OrderList from '../components/Orders/OrderList';
import './OrdersPage.css';

const OrdersPage = () => (
  <div className="page-container">
    <h1>Orders</h1>
    <OrderForm />
    <OrderList />
  </div>
);

export default OrdersPage;
