import React from 'react';
import HeroMain from './HeroMain';
import HeroFeatures from './HeroFeatures';
import '../styles/HeroSection.css';

const HeroSection = () => {
  return (
    <>
      <section className="hero-section">
        <HeroMain />
      </section>
      <section className="features-section">
        <HeroFeatures />
      </section>
    </>
  );
};

export default HeroSection;