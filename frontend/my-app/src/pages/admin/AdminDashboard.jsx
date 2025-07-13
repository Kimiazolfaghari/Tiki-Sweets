import React, { useState } from 'react';
import { 
  BarChart3, 
  Package, 
  Users, 
  ShoppingCart, 
  Settings
} from 'lucide-react';
import AdminProducts from './AdminProducts';
import AdminUsers from './AdminUsers';
import AdminOrders from './AdminOrders';
import './AdminDashboard.css';

const AdminDashboard = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  
  const [products] = useState([
    { id: 1, name: 'Chocolate Cake', price: 45, rating: 4.8, category: 'Cakes' },
    { id: 2, name: 'Vanilla Cupcake', price: 15, rating: 4.6, category: 'Cupcakes' },
    { id: 3, name: 'Strawberry Tart', price: 28, rating: 4.9, category: 'Tarts' },
  ]);
  
  const [users] = useState([
    { id: 1, name: 'Mehdi Rezaei', email: 'mehdi@example.com', role: 'user', joinDate: '2024-01-15' },
    { id: 2, name: 'Elham Sharifi', email: 'elham@example.com', role: 'admin', joinDate: '2023-12-20' },
    { id: 3, name: 'Sara Mohammadi', email: 'sara@example.com', role: 'user', joinDate: '2024-02-10' },
  ]);
  
  const [orders] = useState([
    { id: 1001, customer: 'Mehdi Rezaei', total: 250, status: 'Processing', date: '2024-07-14' },
    { id: 1002, customer: 'Elham Sharifi', total: 470, status: 'Delivered', date: '2024-07-13' },
    { id: 1003, customer: 'Sara Mohammadi', total: 320, status: 'Cancelled', date: '2024-07-12' },
  ]);

  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: BarChart3 },
    { id: 'products', label: 'Products', icon: Package },
    { id: 'users', label: 'Users', icon: Users },
    { id: 'orders', label: 'Orders', icon: ShoppingCart },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  const dashboardStats = [
    { title: 'Total Products', value: products.length, icon: Package, color: 'linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)' },
    { title: 'Total Users', value: users.length, icon: Users, color: 'linear-gradient(135deg, #10b981 0%, #059669 100%)' },
    { title: 'Total Orders', value: orders.length, icon: ShoppingCart, color: 'linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)' },
    { title: 'Revenue', value: '$1,040', icon: Package, color: 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)' },
  ];

  const renderDashboard = () => (
    <div>
      <div className="content-header">
        <h1 className="page-title">Dashboard Overview</h1>
        <div style={{ fontSize: '0.875rem', color: '#6b7280' }}>Welcome back, Admin!</div>
      </div>
      
      <div className="stats-grid">
        {dashboardStats.map((stat, index) => (
          <div key={index} className="stat-card">
            <div className="stat-content">
              <div className="stat-info">
                <h3>{stat.title}</h3>
                <p>{stat.value}</p>
              </div>
              <div className="stat-icon" style={{ background: stat.color }}>
                <stat.icon style={{ width: '1.5rem', height: '1.5rem', color: 'white' }} />
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="recent-items">
        <div className="recent-card">
          <h3>Recent Orders</h3>
          <div>
            {orders.slice(0, 3).map(order => (
              <div key={order.id} className="recent-item">
                <div>
                  <p style={{ fontWeight: '500', color: '#1f2937' }}>#{order.id}</p>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>{order.customer}</p>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <p style={{ fontWeight: '600', color: '#1f2937' }}>${order.total}</p>
                  <span className={`status-badge status-${order.status.toLowerCase()}`}>
                    {order.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="recent-card">
          <h3>Top Products</h3>
          <div>
            {products.slice(0, 3).map(product => (
              <div key={product.id} className="recent-item">
                <div className="product-info">
                  <div className="product-icon">
                    <Package style={{ width: '1.25rem', height: '1.25rem' }} />
                  </div>
                  <div>
                    <p style={{ fontWeight: '500', color: '#1f2937' }}>{product.name}</p>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>{product.category}</p>
                  </div>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <p style={{ fontWeight: '600', color: '#1f2937' }}>${product.price}</p>
                  <div className="rating">
                    <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>★ {product.rating}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );

  const renderSettings = () => (
    <div>
      <h1 className="page-title">Settings</h1>
      
      <div className="settings-grid">
        <div className="settings-card">
          <h3>General Settings</h3>
          <div>
            <div className="form-group">
              <label className="form-label">Site Name</label>
              <input type="text" className="form-input" defaultValue="Sweet Bakery" />
            </div>
            <div className="form-group">
              <label className="form-label">Contact Email</label>
              <input type="email" className="form-input" defaultValue="admin@sweetbakery.com" />
            </div>
            <button className="btn-primary">Save Changes</button>
          </div>
        </div>

        <div className="settings-card">
          <h3>Security Settings</h3>
          <div>
            <div className="form-group">
              <label className="form-label">Current Password</label>
              <input type="password" className="form-input" />
            </div>
            <div className="form-group">
              <label className="form-label">New Password</label>
              <input type="password" className="form-input" />
            </div>
            <button className="btn-primary">Update Password</button>
          </div>
        </div>
      </div>
    </div>
  );

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return renderDashboard();
      case 'products':
        return <AdminProducts products={products} />;
      case 'users':
        return <AdminUsers users={users} />;
      case 'orders':
        return <AdminOrders orders={orders} />;
      case 'settings':
        return renderSettings();
      default:
        return renderDashboard();
    }
  };

  return (
    <div className="admin-dashboard">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="sidebar-header">
          <h2 className="sidebar-title">ADMIN PANEL</h2>
          <nav className="nav-items">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`nav-item ${activeTab === item.id ? 'active' : ''}`}
              >
                <item.icon style={{ width: '1.25rem', height: '1.25rem' }} />
                <span>{item.label}</span>
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <div className="main-content">
        {renderContent()}
      </div>
    </div>
  );
};

export default AdminDashboard;