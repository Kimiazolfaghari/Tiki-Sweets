import React, { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Header.css';

const Header = () => {
  const navigate = useNavigate();
  const [searchActive, setSearchActive] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [userMenuActive, setUserMenuActive] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const userMenuRef = useRef(null);

  const handleSearchClick = () => {
    setSearchActive(prev => !prev);
  };

  const handleSearch = () => {
    console.log('Searching for:', searchTerm);
    setSearchActive(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') handleSearch();
  };

  const handleCartClick = () => {
    navigate('/cart');
  };

  const handleUserClick = () => {
    setUserMenuActive(prev => !prev);
  };

  const handleLogin = () => {
    navigate('/login');
    setUserMenuActive(false);
  };

  const handleSignUp = () => {
    navigate('/register');
    setUserMenuActive(false);
  };

  const handleProfile = () => {
    navigate('/profile');
    setUserMenuActive(false);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    console.log('User logged out');
    setUserMenuActive(false);
  };

  // Close user dropdown on outside click
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (userMenuRef.current && !userMenuRef.current.contains(event.target)) {
        setUserMenuActive(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const scrollToFooter = () => {
    const footer = document.getElementById('footer');
    if (footer) {
      footer.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className="header">
      <div className="logo">
        <img src="/img/logo/logo-withoutbg.png" alt="Tiki Sweets" />
      </div>

      <nav className="nav-links">
        <a href="/">Home</a>
        <a href="/productlisting">Products</a>
        <a href="/CustomCake">Custom Order</a>
        <a href="#" onClick={(e) => { e.preventDefault(); scrollToFooter(); }}>About</a>
        <a href="#" onClick={(e) => { e.preventDefault(); scrollToFooter(); }}>Contact</a>
      </nav>

      <div className="header-icons">
        <img
          src="../img/icons/search.png"
          alt="Search"
          className="icon"
          onClick={handleSearchClick}
        />
        <img
          src="../img/icons/cart.png"
          alt="Cart"
          className="icon"
          onClick={handleCartClick}
        />
        <div className="user-menu-container" ref={userMenuRef}>
          <img
            src="../img/icons/user.png"
            alt="User"
            className="icon"
            onClick={handleUserClick}
          />
          {userMenuActive && (
            <div className="user-dropdown">
              <button onClick={handleLogin} className="dropdown-item">Login</button>
              <button onClick={handleSignUp} className="dropdown-item">Sign Up</button>
              <button onClick={handleProfile} className="dropdown-item">Profile</button>
            </div>
          )}
        </div>
      </div>

      {searchActive && (
        <div className="search-bar">
          <div className="search-container">
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Search products..."
              className="search-input"
            />
            <button onClick={handleSearch} className="search-button">
              <svg className="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="11" cy="11" r="8" />
                <path d="m21 21-4.35-4.35" />
              </svg>
            </button>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;
