import React from 'react';
import { Plus, Edit, Eye, Trash2, Package, Star } from 'lucide-react';

const AdminProducts = ({ products }) => {
  return (
    <div>
      <div className="content-header">
        <h1 className="page-title">Product Management</h1>
        <button className="btn-primary">
          <Plus style={{ width: '1.25rem', height: '1.25rem' }} />
          <span>Add Product</span>
        </button>
      </div>
      
      <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>#</th>
              <th>Image</th>
              <th>Product Name</th>
              <th>Price</th>
              <th>Rating</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product, index) => (
              <tr key={product.id}>
                <td>{index + 1}</td>
                <td>
                  <div style={{ 
                    width: '3rem', 
                    height: '3rem', 
                    background: '#fff7ed', 
                    borderRadius: '0.5rem',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    <Package style={{ width: '1.5rem', height: '1.5rem', color: '#ea580c' }} />
                  </div>
                </td>
                <td style={{ fontWeight: '500' }}>{product.name}</td>
                <td>${product.price}</td>
                <td>
                  <div className="rating">
                    <Star style={{ width: '1rem', height: '1rem', color: '#fbbf24', fill: '#fbbf24' }} />
                    <span>{product.rating}</span>
                  </div>
                </td>
                <td>
                  <div className="action-buttons">
                    <button className="action-btn edit">
                      <Edit style={{ width: '1rem', height: '1rem' }} />
                    </button>
                    <button className="action-btn view">
                      <Eye style={{ width: '1rem', height: '1rem' }} />
                    </button>
                    <button className="action-btn delete">
                      <Trash2 style={{ width: '1rem', height: '1rem' }} />
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

export default AdminProducts;