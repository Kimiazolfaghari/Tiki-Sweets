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

    if (!otp || otp.length !== 4 || isNaN(otp)) {
      setError('Please enter a valid 4-digit numeric verification code.');
      return;
    }

    if (!email) {
      setError('Email is missing. Please register again.');
      return;
    }

    try {
      setLoading(true);

      const response = await fetch('http://127.0.0.1:8000/users/verify-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, otp: otp.toString() }),
      });

      const data = await response.json();

      if (!response.ok) {
        const message = Array.isArray(data.detail)
          ? data.detail.map(e => `${e.loc?.join('.') || ''}: ${e.msg}`).join(', ')
          : data.detail || 'Verification failed';

        throw new Error(message);
      }

      localStorage.removeItem('emailForOTP');
      navigate('/'); // ⬅ بعد از موفقیت، انتقال به صفحه اصلی
    } catch (err) {
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
