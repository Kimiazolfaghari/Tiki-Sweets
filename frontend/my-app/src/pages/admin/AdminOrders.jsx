import React from 'react';
import { Eye, Edit } from 'lucide-react';

const AdminOrders = ({ orders }) => {
  return (
    <div>
      <div className="content-header">
        <h1 className="page-title">Order Management</h1>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <select className="form-input" style={{ width: 'auto' }}>
            <option>All Status</option>
            <option>Processing</option>
            <option>Delivered</option>
            <option>Cancelled</option>
          </select>
        </div>
      </div>
      
      <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>Order ID</th>
              <th>Customer</th>
              <th>Total</th>
              <th>Status</th>
              <th>Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((order) => (
              <tr key={order.id}>
                <td style={{ fontWeight: '500' }}>#{order.id}</td>
                <td>{order.customer}</td>
                <td style={{ fontWeight: '600' }}>${order.total}</td>
                <td>
                  <span className={`status-badge status-${order.status.toLowerCase()}`}>
                    {order.status}
                  </span>
                </td>
                <td>{order.date}</td>
                <td>
                  <div className="action-buttons">
                    <button className="action-btn view">
                      <Eye style={{ width: '1rem', height: '1rem' }} />
                    </button>
                    <button className="action-btn edit">
                      <Edit style={{ width: '1rem', height: '1rem' }} />
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AdminOrders;