import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import '../styles/login.css';
import { useAuth } from '../context/AuthContext';

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [form, setForm] = useState({
    email: '',
    password: '',
    rememberMe: false,
  });

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({ ...form, [name]: type === 'checkbox' ? checked : value });
  };

  const decodeToken = (token) => {
    try {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split('')
          .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
          .join('')
      );
      return JSON.parse(jsonPayload);
    } catch (error) {
      console.error("❌ Failed to decode token:", error);
      return null;
    }
  };

  const loginRequest = async (url) => {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: form.email,
        password: form.password,
      }),
    });

    const text = await res.text();
    let data;
    try {
      data = JSON.parse(text);
    } catch (err) {
      throw new Error("Invalid response format from server");
    }

    if (!res.ok) {
      throw new Error(data.detail || 'Login failed');
    }

    return data;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      let data;
      let isAdmin = false;

      // First try normal user login
      try {
        data = await loginRequest('http://127.0.0.1:8000/users/login');
      } catch (userErr) {
        console.warn("🔁 User login failed, trying admin...");
        data = await loginRequest('http://127.0.0.1:8000/admin/login');
        isAdmin = true;
      }

      const decoded = decodeToken(data.access_token);
      console.log("✅ Decoded Token:", decoded);

      if (!decoded) throw new Error("Could not decode token");

      // Use role from token (if available) instead of fallback
      isAdmin = decoded?.role?.toLowerCase() === 'admin';


      login({
        token: data.access_token,
        email: form.email,
        isAdmin,
      });

      navigate(isAdmin ? '/admin' : '/');
    } catch (err) {
      console.error("❌ Login error:", err);
      setError(err.message || 'Login error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container w-100">
      <button onClick={() => navigate(-1)} className="back-button">
        <ArrowLeft size={20} color="#41342A" />
      </button>

      <div className="login-card shadow">
        <h2 className="text-center fw-bold">Account Login</h2>
        <p className="text-center text-muted mb-4">Welcome back</p>

        <form onSubmit={handleSubmit}>
          <InputField
            type="email"
            name="email"
            placeholder="Email Address"
            value={form.email}
            onChange={handleChange}
          />
          <InputField
            type="password"
            name="password"
            placeholder="Password"
            value={form.password}
            onChange={handleChange}
          />

          <div className="d-flex justify-content-between align-items-center mb-3 small text-muted">
            <label className="d-flex align-items-center gap-2">
              <input
                type="checkbox"
                name="rememberMe"
                checked={form.rememberMe}
                onChange={handleChange}
              />
              Remember Me
            </label>
            <a href="#" className="forgot-link">Forgot Password?</a>
          </div>

          {error && <div className="text-danger text-center mb-2">{error}</div>}

          <SubmitButton label={loading ? 'Logging in...' : 'Log In'} disabled={loading} />
        </form>

        <p className="text-center mt-3 small">
          Don't have an account?{' '}
          <button
            type="button"
            onClick={() => navigate('/register')}
            className="login-link bg-transparent border-0 p-0"
          >
            Sign Up
          </button>
        </p>
      </div>
    </div>
  );
};

export default Login;
