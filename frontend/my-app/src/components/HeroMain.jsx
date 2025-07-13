import React, { useEffect, useState } from 'react';

const HeroMain = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      setIsVisible(true);
    }, 500); // Delay the appearance by 500ms
  }, []);

  return (
    <div className={`hero-main ${isVisible ? 'fade-in' : ''}`}>
      <div className="hero-text">
        <h2>Sweet Moments</h2>
        <h3>Baked with Love</h3>
        <p>
          Experience the joy of perfectly baked cakes, made with love and crafted to bring a smile to every celebration.
        </p>
      </div>
      <div className="hero-image">
        <img src="../img/png/HeaderCake.png" alt="Delicious Cake" />
      </div>
    </div>
  );
};

export default HeroMain;
