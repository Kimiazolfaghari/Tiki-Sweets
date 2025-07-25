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

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/users/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: form.email,
          password: form.password,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Login failed');
      }

      const data = await response.json();

      // ذخیره توکن در context و optional: localStorage
      login({
        token: data.access_token,
        email: form.email,
        isAdmin: data.is_admin || false,
      });

      // انتقال به مسیر مناسب
      navigate(data.is_admin ? '/admin' : '/');
    } catch (err) {
      console.error(err);
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
