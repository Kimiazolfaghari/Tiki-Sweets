import React from 'react';
import { useNavigate } from 'react-router-dom'; // ← برای هدایت
import '../styles/PromoSection.css';
import ActionButton from './ActionButton.jsx';
import promoImage from '../../img/promo.png';

const PromoSection = () => {
  const navigate = useNavigate();

  const handleOrderNow = () => {
    navigate('/products/Cakes');
  };

  return (
    <div className="promo-container">
      <div className="promo-text">
        <h2>Sweeten Your First Purchase with 10% OFF!</h2>
        <p>
          Use code <strong>WELCOME10</strong> at checkout and enjoy your treats!
        </p>
        <button 
          className="action-button action-button--default"
          onClick={handleOrderNow}
        >
          Order Now 🛒
        </button>
      </div>
      <div className="promo-image">
        <img
          src={promoImage}
          alt="Delicious strawberry cake with 10% discount"
        />
      </div>
    </div>
  );
};

export default PromoSection;
