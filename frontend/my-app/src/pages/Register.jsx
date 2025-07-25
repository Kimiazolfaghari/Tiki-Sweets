import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import ErrorMessage from '../components/ErrorMessage';
import '../styles/register.css';

const Register = () => {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    firstName: '',
    lastName: '',
    password: '',
    phone: '',
    email: '',
  });

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/users/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          full_name: `${form.firstName} ${form.lastName}`,
          email: form.email,
          password: form.password,
          phone: form.phone,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Registration failed');
      }

      // ✅ ذخیره ایمیل برای استفاده در صفحه Verify
      localStorage.setItem('emailForOTP', form.email);

      setLoading(false);
      navigate('/verify');

    } catch (err) {
      setLoading(false);
      setError(err.message || 'Registration error');
    }
  };

  return (
    <div className="register-container w-100">
      <button onClick={() => navigate(-1)} className="back-button" type="button">
        <ArrowLeft size={20} color="#41342A" />
      </button>

      <div className="register-card shadow">
        <h2 className="text-center fw-bold mb-2">Account Sign Up</h2>
        <p className="text-center text-muted mb-4">Create Account</p>

        <form onSubmit={handleSubmit}>
          <InputField
            name="firstName"
            placeholder="First Name"
            value={form.firstName}
            onChange={handleChange}
          />
          <InputField
            name="lastName"
            placeholder="Last Name"
            value={form.lastName}
            onChange={handleChange}
          />
          <InputField
            type="tel"
            name="phone"
            placeholder="Phone Number"
            value={form.phone}
            onChange={handleChange}
          />
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

          {error && <ErrorMessage message={error} />}
          <SubmitButton label={loading ? 'Registering...' : 'Sign Up'} disabled={loading} />
        </form>

        <p className="text-center mt-3 small">
          Already Have An Account?{' '}
          <a href="/login" className="login-link">Log In</a>
        </p>
      </div>
    </div>
  );
};

export default Register;
