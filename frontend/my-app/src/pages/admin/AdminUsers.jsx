import React from 'react';
import { Plus, Edit, Trash2 } from 'lucide-react';

const AdminUsers = ({ users }) => {
  return (
    <div>
      <div className="content-header">
        <h1 className="page-title">User Management</h1>
        <button className="btn-primary">
          <Plus style={{ width: '1.25rem', height: '1.25rem' }} />
          <span>Add User</span>
        </button>
      </div>
      
      <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Email</th>
              <th>Role</th>
              <th>Join Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, index) => (
              <tr key={user.id}>
                <td>{index + 1}</td>
                <td style={{ fontWeight: '500' }}>{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <span className={`role-badge ${user.role === 'admin' ? 'role-admin' : 'role-user'}`}>
                    {user.role}
                  </span>
                </td>
                <td>{user.joinDate}</td>
                <td>
                  <div className="action-buttons">
                    <button className="action-btn edit">
                      <Edit style={{ width: '1rem', height: '1rem' }} />
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

export default AdminUsers;