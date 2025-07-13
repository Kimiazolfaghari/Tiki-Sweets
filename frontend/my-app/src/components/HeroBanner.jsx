import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // ← اضافه کن
import '../styles/HeroBanner.css';
import ActionButton from './ActionButton';

const HeroBanner = ({
  title = "Your Sweet Dream",
  subtitle = "Our Recipe",
  description = "Indulge in our freshly baked cakes, crafted with care, and designed to make every celebration.",
  buttonText = "View More",
  imageSrc = "/img/png/stand.png",
  imageAlt = "Beautiful cupcake stand with decorated cupcakes",
  onButtonClick,
  className = ""
}) => {
  const [isVisible, setIsVisible] = useState(false);
  const [imageLoaded, setImageLoaded] = useState(false);
  const navigate = useNavigate(); // ← استفاده از ناویگیت

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsVisible(true);
    }, 100);
    return () => clearTimeout(timer);
  }, []);

  const handleButtonClick = () => {
    if (onButtonClick) {
      onButtonClick();
    } else {
      navigate('/products/Cakes'); // ← هدایت به صفحه کیک‌ها
    }
  };

  const handleImageLoad = () => {
    setImageLoaded(true);
  };

  const handleImageError = (e) => {
    e.target.src = 'https://via.placeholder.com/450x400/f5ede5/d4a574?text=Sweet+Cupcakes';
    e.target.alt = 'Cupcake placeholder image';
  };

  return (
    <section className={`hero-banner ${className}`} role="banner">
      <div className="hero-container">
        <div className="hero-image-section">
          <div className="cupcake-stand">
            <img
              src={imageSrc}
              alt={imageAlt}
              onLoad={handleImageLoad}
              onError={handleImageError}
              loading="lazy"
              style={{
                opacity: imageLoaded ? 1 : 0,
                transition: 'opacity 0.5s ease'
              }}
            />
            <div className="image-decoration decoration-1" aria-hidden="true"></div>
            <div className="image-decoration decoration-2" aria-hidden="true"></div>
          </div>
        </div>

        <div className="hero-content">
          <h1 className="hero-title">{title}</h1>
          <h2 className="hero-subtitle">{subtitle}</h2>
          <p className="hero-description">{description}</p>
          <ActionButton
            text={buttonText}
            onClick={handleButtonClick}
            variant="default"
          />
        </div>
      </div>
    </section>
  );
};

export default HeroBanner;
