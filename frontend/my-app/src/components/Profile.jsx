import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, X } from 'lucide-react';
import '../styles/profile.css';

const ProfilePage = () => {
  const navigate = useNavigate();
  const [profile, setProfile] = useState({
    name: 'Jacob Jones',
    email: 'jacob.jones@gmail.com',
    phone: '(302) 555-0107',
    location: 'USA'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile({ ...profile, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Profile updated:', profile);
    // اینجا می‌توانید API call برای ذخیره اطلاعات اضافه کنید
  };

  return (
    <div className="profile-container">
      {/* فلش برگشت دایره‌ای */}
      <button
        onClick={() => navigate(-1)}
        className="back-button"
      >
        <ArrowLeft size={20} color="#41342A" />
      </button>

      <div className="profile-card">
        {/* دکمه بستن */}
        <button
          onClick={() => navigate(-1)}
          className="close-button"
        >
          <X size={18} />
        </button>

        {/* آواتار */}
        <img
          src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face"
          alt="Profile Avatar"
          className="profile-avatar"
        />

        <h2>{profile.name}</h2>

        <form onSubmit={handleSubmit}>
          <div className="profile-field">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              className="custom-input"
              value={profile.name}
              onChange={handleChange}
            />
          </div>

          <div className="profile-field">
            <label htmlFor="email">Email account</label>
            <input
              type="email"
              id="email"
              name="email"
              className="custom-input"
              value={profile.email}
              onChange={handleChange}
            />
          </div>

          <div className="profile-field">
            <label htmlFor="phone">Mobile number</label>
            <input
              type="tel"
              id="phone"
              name="phone"
              className="custom-input"
              value={profile.phone}
              onChange={handleChange}
            />
          </div>

          <div className="profile-field">
            <label htmlFor="location">Location</label>
            <input
              type="text"
              id="location"
              name="location"
              className="custom-input"
              value={profile.location}
              onChange={handleChange}
            />
          </div>

          <button type="submit" className="save-btn">
            Save Changes
          </button>
        </form>
      </div>
    </div>
  );
};

export default ProfilePage;