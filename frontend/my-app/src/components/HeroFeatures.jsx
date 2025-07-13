import React from 'react';

const features = [
  {
    icon: "../img/icons/chef-hat.png",
    title: "Handmade With Love",
    description: "Baked fresh after every order, with premium ingredients."
  },
  {
    icon: "../img/icons/secure-payment.png",
    title: "Secure Payment",
    description: "Pay confidently with encrypted and trusted methods."
  },
  {
    icon: "../img/icons/custom-cake.png",
    title: "Custom your Cakes",
    description: "Custom cakes designed to match your happiest moments."
  }
];

const HeroFeatures = () => {
  return (
    <div className="hero-features">
      {features.map((feature, idx) => (
        <div key={idx} className="feature-card">
          <img src={feature.icon} alt={feature.title} className="feature-icon" />
          <h4>{feature.title}</h4>
          <p>{feature.description}</p>
        </div>
      ))}
    </div>
  );
};

export default HeroFeatures;
