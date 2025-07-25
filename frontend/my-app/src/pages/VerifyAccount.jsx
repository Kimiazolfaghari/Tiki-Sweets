import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import ErrorMessage from '../components/ErrorMessage';
import '../styles/verifyAccount.css';

const VerifyAccount = () => {
  const navigate = useNavigate();
  const [otp, setOtp] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const storedEmail = localStorage.getItem('emailForOTP');
    if (storedEmail) {
      setEmail(storedEmail);
    } else {
      setError('Email not found. Redirecting to registration...');
      setTimeout(() => navigate('/register'), 3000);
    }
  }, [navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!otp || otp.length !== 4) {
      setError('Please enter a valid 4-digit verification code.');
      return;
    }

    try {
      setLoading(true);

      const response = await fetch('http://127.0.0.1:8000/users/verify-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, otp }),
      });

      if (!response.ok) {
        const err = await response.json();
        const message = Array.isArray(err.detail)
          ? err.detail.map(e => e.msg).join(', ')
          : err.detail || 'Verification failed';
        throw new Error(message);
      }

      localStorage.removeItem('emailForOTP');
      navigate('/login');
    } catch (err) {
      console.error('OTP Verification Error:', err);
      setError(err.message || 'Failed to verify account');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="verify-container w-100">
      <button onClick={() => navigate(-1)} className="back-button">
        <ArrowLeft size={20} color="#41342A" />
      </button>

      <div className="verify-card shadow">
        <h2 className="text-center fw-bold mb-2">Verify Your Account</h2>
        <p className="text-center text-muted mb-4">
          Please enter the verification code sent to your email.
        </p>

        <form onSubmit={handleSubmit}>
          <InputField
            type="text"
            name="otp"
            placeholder="Verification Code"
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
          />
          {error && <ErrorMessage message={error} />}
          <SubmitButton
            label={loading ? 'Verifying...' : 'Verify'}
            disabled={loading}
          />
        </form>
      </div>
    </div>
  );
};

export default VerifyAccount;
