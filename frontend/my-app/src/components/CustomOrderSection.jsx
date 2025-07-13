import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/CustomOrderSection.css';
import ActionButton from './ActionButton';

const CustomOrderSection = () => {
  const navigate = useNavigate();

  const handleViewMore = () => {
    const section = document.querySelector('#featured-products');
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    } else {
      console.warn('Featured Products section not found.');
    }
  };

  const handleCustomNow = () => {
    navigate('/customcake');
  };

  return (
    <section className="custom-order-section">
      <div className="order-card">
        <img
          src="/img/Custom/custom1.jpg"
          alt="Bestsellers"
          className="order-image"
        />
        <div className="order-overlay">
          <h3>Featured Products</h3>
          <ActionButton 
            text="View More" 
            onClick={handleViewMore} 
            variant="default"
          />
        </div>
      </div>

      <div className="order-card">
        <img
          src="/img/Custom/custom2.jpg"
          alt="Place Custom Order"
          className="order-image"
        />
        <div className="order-overlay">
          <h3>Place Custom Order</h3>
          <ActionButton 
            text="Custom Now" 
            onClick={handleCustomNow} 
            variant="default"
          />
        </div>
      </div>
    </section>
  );
};

export default CustomOrderSection;
