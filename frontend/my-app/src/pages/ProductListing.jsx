// ProductListing.jsx
import React from 'react';
import Header from '../components/Header02';
import ProductMain from '../components/ProductMain';
import Footer from '../components/Footer';

const Cake = () => {
  return (
    <div className="ProductListing-page">
      <Header /> 
      <ProductMain /> 
      <Footer /> 
    </div>
  );
};

export default Cake;
