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
    username: '',
    password: '',
    phone: '',
    email: '',
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Registered form data:', form);
  };

  return (
    <div className="register-container w-100">
      {/* فلش برگشت دایره‌ای */}
      <button
        onClick={() => navigate(-1)}
        className="back-button"
      >
        <ArrowLeft size={20} color="#41342A" />
      </button>

      <div className="register-card shadow">
        <h2 className="text-center fw-bold">Account Sign Up</h2>
        <p className="text-center text-muted mb-4">Create Account</p>

        <form onSubmit={handleSubmit}>
          <InputField name="firstName" placeholder="First Name" value={form.firstName} onChange={handleChange} />
          <InputField name="lastName" placeholder="Last Name" value={form.lastName} onChange={handleChange} />
          <InputField name="username" placeholder="Username" value={form.username} onChange={handleChange} />
          <InputField type="password" name="password" placeholder="Password" value={form.password} onChange={handleChange} />
          <InputField type="tel" name="phone" placeholder="Phone Number" value={form.phone} onChange={handleChange} />
          <InputField type="email" name="email" placeholder="Email Address" value={form.email} onChange={handleChange} />

          <SubmitButton label="Sign Up" />
        </form>

        <p className="text-center mt-3 small">
          Already Have An Account? <a href="/login" className="login-link">Log In</a>
        </p>
      </div>
    </div>
  );
};

export default Register;
