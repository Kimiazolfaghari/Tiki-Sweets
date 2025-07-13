import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import '../styles/address.css';

const Address = () => {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    city: '',
    street: '',
    alley: '',
    postalCode: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Address form data:', form);
    // You can handle submission logic here
  };

  return (
    <div className="address-container w-100">
      {/* Back Arrow Button */}
      <button
        onClick={() => navigate(-1)}
        className="back-button"
      >
        <ArrowLeft size={20} color="#41342A" />
      </button>

      <div className="address-card shadow">
        <h2 className="text-center fw-bold">Address</h2>
        <p className="text-center text-muted mb-4">Please enter your address</p>

        <form onSubmit={handleSubmit}>
          <InputField
            type="text"
            name="city"
            placeholder="City"
            value={form.city}
            onChange={handleChange}
          />
          <InputField
            type="text"
            name="street"
            placeholder="Street"
            value={form.street}
            onChange={handleChange}
          />
          <InputField
            type="text"
            name="alley"
            placeholder="Alley"
            value={form.alley}
            onChange={handleChange}
          />
          <InputField
            type="text"
            name="postalCode"
            placeholder="Postal Code"
            value={form.postalCode}
            onChange={handleChange}
          />

          <SubmitButton label="Continue" />
        </form>
      </div>
    </div>
  );
};

export default Address;
