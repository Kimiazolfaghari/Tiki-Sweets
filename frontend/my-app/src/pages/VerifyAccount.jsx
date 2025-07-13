import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import ErrorMessage from '../components/ErrorMessage';
import '../styles/verifyAccount.css';

const VerifyAccount = () => {
  const navigate = useNavigate();
  const [otp, setOtp] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!otp || otp.length < 4) {
      setError('Please enter a valid verification code.');
      return;
    }
    console.log('🔐 OTP Code:', otp);
    setError('');
    // TODO: Send code to backend
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

          <SubmitButton label="Verify" />
        </form>
      </div>
    </div>
  );
};

export default VerifyAccount;
