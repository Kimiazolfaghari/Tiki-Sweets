import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import './AdminDashboard.css';

const AdminDashboard = () => {
  return (
    <div className="admin-container">
      <aside className="admin-sidebar">
        <h2>Admin Dashboard</h2>
        <nav>
          <NavLink to="/admin/products" className={navLinkClass}>
            Manage Products
          </NavLink>
          <NavLink to="/admin/users" className={navLinkClass}>
            Users
          </NavLink>
          <NavLink to="/admin/orders" className={navLinkClass}>
            Orders
          </NavLink>
        </nav>
      </aside>

      <main className="admin-content">
        <Outlet />
      </main>
    </div>
  );
};

// NavLink active/inactive class handling
const navLinkClass = ({ isActive }) =>
  isActive ? 'active' : '';

export default AdminDashboard;
