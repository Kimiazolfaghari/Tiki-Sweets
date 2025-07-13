import React, { useEffect, useState } from 'react';

const mockOrders = [
  { id: 1001, customer: 'Mehdi Rezaei', total: 250, status: 'Processing' },
  { id: 1002, customer: 'Elham Sharifi', total: 470, status: 'Delivered' },
  { id: 1003, customer: 'Sara Mohammadi', total: 320, status: 'Cancelled' },
];

const AdminOrders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    setOrders(mockOrders);
  }, []);

  return (
    <div>
      <h2 style={{ marginBottom: '1rem' }}>Order Management</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', backgroundColor: '#fff' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={thStyle}>Order ID</th>
            <th style={thStyle}>Customer</th>
            <th style={thStyle}>Total ($)</th>
            <th style={thStyle}>Status</th>
            <th style={thStyle}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {orders.map(order => (
            <tr key={order.id} style={{ textAlign: 'center' }}>
              <td style={tdStyle}>{order.id}</td>
              <td style={tdStyle}>{order.customer}</td>
              <td style={tdStyle}>{order.total}</td>
              <td style={tdStyle}>{order.status}</td>
              <td style={tdStyle}>
                <button onClick={() => alert(`View order ${order.id}`)}>🔍</button>
                <button onClick={() => alert(`Change status of ${order.id}`)}>⚙️</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const thStyle = {
  padding: '0.75rem',
  border: '1px solid #ddd',
};

const tdStyle = {
  padding: '0.5rem',
  border: '1px solid #ddd',
};

export default AdminOrders;
