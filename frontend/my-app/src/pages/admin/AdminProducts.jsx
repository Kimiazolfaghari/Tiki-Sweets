import React, { useEffect, useState } from 'react';
import productsData from '../../Products.json'; // path to JSON file

const AdminProducts = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Load only the "Cakes" category — can be dynamic later
    setProducts(productsData.Cakes || []);
  }, []);

  return (
    <div>
      <h2 style={{ marginBottom: '1rem' }}>Manage Products (Cakes)</h2>

      <button
        style={{
          padding: '0.5rem 1rem',
          backgroundColor: '#28a745',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          marginBottom: '1rem',
        }}
        onClick={() => alert('Add Product Form')}
      >
        Add New Product
      </button>

      <table
        style={{
          width: '100%',
          borderCollapse: 'collapse',
          backgroundColor: '#fff',
        }}
      >
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={thStyle}>#</th>
            <th style={thStyle}>Image</th>
            <th style={thStyle}>Product Name</th>
            <th style={thStyle}>Price ($)</th>
            <th style={thStyle}>Rating</th>
            <th style={thStyle}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product, index) => (
            <tr key={product.id} style={{ textAlign: 'center' }}>
              <td style={tdStyle}>{index + 1}</td>
              <td style={tdStyle}>
                <img src={product.image} alt={product.name} width="60" />
              </td>
              <td style={tdStyle}>{product.name}</td>
              <td style={tdStyle}>{product.price.toLocaleString()}</td>
              <td style={tdStyle}>{product.rating}</td>
              <td style={tdStyle}>
                <button
                  onClick={() => alert(`Edit ${product.name}`)}
                  style={{ marginRight: '0.5rem' }}
                >
                  ✏️
                </button>
                <button
                  onClick={() => alert(`Delete ${product.name}`)}
                  style={{ color: 'red' }}
                >
                  🗑
                </button>
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

export default AdminProducts;
