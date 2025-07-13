import React, { useEffect, useState } from 'react';

const mockUsers = [
  { id: 1, name: 'Mehdi Rezaei', email: 'mehdi@example.com', role: 'user' },
  { id: 2, name: 'Elham Sharifi', email: 'elham@example.com', role: 'admin' },
  { id: 3, name: 'Sara Mohammadi', email: 'sara@example.com', role: 'user' },
];

const AdminUsers = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    setUsers(mockUsers);
  }, []);

  return (
    <div>
      <h2 style={{ marginBottom: '1rem' }}>User Management</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', backgroundColor: '#fff' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={thStyle}>#</th>
            <th style={thStyle}>Name</th>
            <th style={thStyle}>Email</th>
            <th style={thStyle}>Role</th>
            <th style={thStyle}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user, index) => (
            <tr key={user.id} style={{ textAlign: 'center' }}>
              <td style={tdStyle}>{index + 1}</td>
              <td style={tdStyle}>{user.name}</td>
              <td style={tdStyle}>{user.email}</td>
              <td style={tdStyle}>{user.role}</td>
              <td style={tdStyle}>
                <button onClick={() => alert(`Edit ${user.name}`)}>✏️</button>
                <button onClick={() => alert(`Delete ${user.name}`)} style={{ color: 'red' }}>
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

export default AdminUsers;
