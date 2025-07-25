import React, { useState } from 'react';
import {useNavigate} from "react-router-dom";
import ActionButton from './ActionButton';
import '../styles/CakeDesigner.css';

const CakeDesigner = () => {
  const navigate = useNavigate();


  const [selectedOptions, setSelectedOptions] = useState({
    spongeFlavor: '',
    fillingType: '',
    creamFlavor: '',
    shape: '',
    coveringType: '',
    layers: '',
    dimensions: '',
    weight: '',
    colorTheme: '',
    deliveryDate: '',
    messageOnCake: ''
  });

  const handleOptionSelect = (category, value) => {
    setSelectedOptions(prev => ({
      ...prev,
      [category]: value
    }));
  };

  const handleContinue = () => {
    console.log('Selected options:', selectedOptions);
    navigate('/PaymentForm');
  };

  const OptionButton = ({ category, value, children }) => (
    <button
      className={`option-btn ${selectedOptions[category] === value ? 'selected' : ''}`}
      onClick={() => handleOptionSelect(category, value)}
    >
      {children}
    </button>
  );

  return (
    <div className="cake-designer">
      <div className="container">
        {/* Header */}
        <div className="header-design">
          <h1 className="title">Design your dream cake!</h1>
          <div className="cake-illustration">
            <img 
              src="/img/design.png" 
              alt="Dream Cake Illustration" 
              className="cake-image"
            />
          </div>
          <p className="subtitle">You're the designer!</p>
        </div>

        {/* Sponge Flavor */}
        <div className="section">
          <h3 className="section-title">Sponge Flavor</h3>
          <div className="options-grid">
            <OptionButton category="spongeFlavor" value="vanilla">Vanilla</OptionButton>
            <OptionButton category="spongeFlavor" value="chocolate">Chocolate</OptionButton>
            <OptionButton category="spongeFlavor" value="redVelvet">Red Velvet</OptionButton>
            <OptionButton category="spongeFlavor" value="coffee">Coffee</OptionButton>
            <OptionButton category="spongeFlavor" value="lemon">Lemon</OptionButton>
            <OptionButton category="spongeFlavor" value="marble">Marble</OptionButton>
            <OptionButton category="spongeFlavor" value="matcha">Matcha</OptionButton>
            <OptionButton category="spongeFlavor" value="carrot">Carrot</OptionButton>
          </div>
        </div>

        {/* Filling Type */}
        <div className="section">
          <h3 className="section-title">Filling Type</h3>
          <div className="options-grid">
            <OptionButton category="fillingType" value="chocolateGanache">Chocolate Ganache</OptionButton>
            <OptionButton category="fillingType" value="strawberryJam">Strawberry Jam</OptionButton>
            <OptionButton category="fillingType" value="nutella">Nutella</OptionButton>
            <OptionButton category="fillingType" value="whippedCream">Whipped Cream</OptionButton>
            <OptionButton category="fillingType" value="lemonCurd">Lemon Curd</OptionButton>
            <OptionButton category="fillingType" value="oreoCrumble">Oreo Crumble</OptionButton>
            <OptionButton category="fillingType" value="freshFruits">Fresh Fruits</OptionButton>
            <OptionButton category="fillingType" value="noFilling">No Filling</OptionButton>
          </div>
        </div>

        {/* Cream Flavor */}
        <div className="section">
          <h3 className="section-title">Cream Flavor</h3>
          <div className="options-grid">
            <OptionButton category="creamFlavor" value="vanillaButtercream">Vanilla Buttercream</OptionButton>
            <OptionButton category="creamFlavor" value="chocolateButtercream">Chocolate Buttercream</OptionButton>
            <OptionButton category="creamFlavor" value="creamCheese">Cream Cheese</OptionButton>
            <OptionButton category="creamFlavor" value="mocha">Mocha</OptionButton>
            <OptionButton category="creamFlavor" value="hazelnut">Hazelnut</OptionButton>
            <OptionButton category="creamFlavor" value="coconut">Coconut</OptionButton>
            <OptionButton category="creamFlavor" value="pistachio">Pistachio</OptionButton>
          </div>
        </div>

        {/* Shape */}
        <div className="section">
          <h3 className="section-title">Shape</h3>
          <div className="options-grid">
            <OptionButton category="shape" value="round">Round</OptionButton>
            <OptionButton category="shape" value="square">Square</OptionButton>
            <OptionButton category="shape" value="heart">Heart</OptionButton>
            <OptionButton category="shape" value="numberShape">Number Shape</OptionButton>
          </div>
        </div>

        {/* Covering Type */}
        <div className="section">
          <h3 className="section-title">Covering Type</h3>
          <div className="options-grid">
            <OptionButton category="coveringType" value="buttercream">Buttercream</OptionButton>
            <OptionButton category="coveringType" value="fondant">Fondant</OptionButton>
            <OptionButton category="coveringType" value="dripGlaze">Drip Glaze</OptionButton>
            <OptionButton category="coveringType" value="whippedCream">Whipped Cream</OptionButton>
          </div>
        </div>

        {/* Form Fields */}
        <div className="form-grid">
          <div className="form-section">
            <h3 className="section-title">Layers</h3>
            <input
              type="number"
              className="form-input"
              placeholder="Number of layers"
              min="1"
              max="5"
              value={selectedOptions.layers}
              onChange={(e) => handleOptionSelect('layers', e.target.value)}
            />
          </div>

          <div className="form-section">
            <h3 className="section-title">Dimensions</h3>
            <input
              type="text"
              className="form-input"
              placeholder="e.g., 8 inch diameter"
              value={selectedOptions.dimensions}
              onChange={(e) => handleOptionSelect('dimensions', e.target.value)}
            />
          </div>

          <div className="form-section">
            <h3 className="section-title">Weight</h3>
            <input
              type="text"
              className="form-input"
              placeholder="e.g., 2 kg"
              value={selectedOptions.weight}
              onChange={(e) => handleOptionSelect('weight', e.target.value)}
            />
          </div>

          <div className="form-section">
            <h3 className="section-title">Color Theme</h3>
            <input
              type="text"
              className="form-input"
              placeholder="e.g., Pink & Gold"
              value={selectedOptions.colorTheme}
              onChange={(e) => handleOptionSelect('colorTheme', e.target.value)}
            />
          </div>

          <div className="form-section">
            <h3 className="section-title">Delivery Date</h3>
            <input
              type="date"
              className="form-input"
              value={selectedOptions.deliveryDate}
              onChange={(e) => handleOptionSelect('deliveryDate', e.target.value)}
            />
          </div>

          <div className="form-section">
            <h3 className="section-title">Message on Cake</h3>
            <input
              type="text"
              className="form-input"
              placeholder="e.g., Happy Birthday!"
              value={selectedOptions.messageOnCake}
              onChange={(e) => handleOptionSelect('messageOnCake', e.target.value)}
            />
          </div>
        </div>

        {/* Continue Button */}
        <div className="continue-section">
          <ActionButton
            text="Continue"
            onClick={handleContinue}
            variant="default"
            className="continue-btn"
          />
        </div>
      </div>
    </div>
  );
};

export default CakeDesigner;