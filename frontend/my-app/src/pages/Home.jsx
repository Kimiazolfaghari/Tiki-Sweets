import React from 'react';
import Header from '../components/Header.jsx';
import HeroSection from '../components/HeroSection.jsx';
import CakeSlider from '../components/CakeSlider.jsx';
import HeroBanner from '../components/HeroBanner.jsx';
import CustomOrderSection from '../components/CustomOrderSection';
import PromoSection from '../components/PromoSection';
import FeaturedProducts from '../components/FeaturedProducts.jsx'
import Footer from '../components/Footer.jsx'
const Home = () => {
  return (
    <>
      <Header />
      <main>
        <HeroSection />
        <CakeSlider />
        <HeroBanner />
        <CustomOrderSection />
        <PromoSection />
        <FeaturedProducts />
        <Footer />


      </main>
    </>
  );
};

export default Home;
