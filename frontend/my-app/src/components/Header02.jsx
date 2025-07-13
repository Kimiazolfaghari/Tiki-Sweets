import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'; // اضافه کردن useNavigate
import '../styles/Header02.css';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const navigate = useNavigate();

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  const navigateToCart = () => {
    navigate("/cart");
  };

  return (
    <>
      <header className="header">
        <div className="menu-icon" onClick={toggleMenu}>
          <img src="/img/icons/menu.png" alt="Menu Icon" />
        </div>
        <div className="logo">
          <img src="/img/logo/logo-withoutbg.png" alt="Tiki Sweets" />
        </div>
        <div className="cart-icon" onClick={navigateToCart}>
          <img src="/img/icons/shopping-basket.png" alt="Cart Icon" />
        </div>
      </header>

      <div 
        className={`menu-overlay ${isMenuOpen ? 'menu-overlay-open' : ''}`}
        onClick={closeMenu}
      />

      <div className={`mobile-menu ${isMenuOpen ? 'mobile-menu-open' : ''}`}>
        <div className="close-button-container">
          <button className="close-button" onClick={closeMenu}>×</button>
        </div>

        <nav className="menu-nav">
          <ul className="menu-list">
            <li className="menu-item">
              <Link to="/home" className="menu-link" onClick={closeMenu}>Home</Link>
            </li>
            <li className="menu-item">
              <Link to="/ProductListing" className="menu-link" onClick={closeMenu}>Product</Link>
            </li>
            <li className="menu-item">
              <Link to="/customcake" className="menu-link" onClick={closeMenu}>Custom Order</Link>
            </li>
            <li className="menu-item">
              <Link to="/Home" className="menu-link" onClick={closeMenu}>About</Link>
            </li>
            <li className="menu-item">
              <Link to="/Home" className="menu-link" onClick={closeMenu}>Contact</Link>
            </li>
          </ul>
        </nav>
      </div>
    </>
  );
};

export default Header;
