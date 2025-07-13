import React from 'react';
import '../styles/Footer.css';

const Footer = () => {
  return (
    <footer id="footer" className="footer">
      <div className="footer-container">
        {/* Logo and Social Media Section */}
        <div className="footer-top-section">
          <div className="footer-logo-section">
            <div className="footer-logo">
              <img src="/img/logo/logo-withoutbg.png" alt="Tiki Sweets Logo" className="logo-image" />
            </div>
          </div>

          <div className="footer-social">
            <p className="social-title">Follow US</p>
            <div className="social-icons">
              <a href="#" className="social-icon">
                <img src="/img/icons/linkedin.png" alt="linkedin" />
              </a>
              <a href="#" className="social-icon">
                <img src="/img/icons/facebook.png" alt="facebook" />
              </a>
              <a href="#" className="social-icon">
                <img src="/img/icons/x.png" alt="x" />
              </a>
              <a href="#" className="social-icon">
                <img src="/img/icons/instagram.png" alt="Instagram" />
              </a>
              <a href="#" className="social-icon">
                <img src="/img/icons/youtube.png" alt="youtube" />
              </a>
            </div>
          </div>
        </div>

        {/* Contact Info */}
        <div className="footer-contact">
          <div className="contact-item">
            <div className="contact-icon">
              <img src="/img/icons/user1.png" alt="user" />
            </div>
            <h3 className="contact-title">Contact With Us</h3>
            <p className="contact-email">TikiSweetsSupport@gmail.com</p>
          </div>

          <div className="contact-item">
            <div className="contact-icon">
              <img src="/img/icons/email.png" alt="email" />
            </div>
            <h3 className="contact-title">Get In Touch</h3>
            <p className="contact-email">Tikisweets@gmail.com</p>
          </div>

          <div className="contact-item">
            <div className="contact-icon">
              <img src="/img/icons/handshake.png" alt="handshake" />
            </div>
            <h3 className="contact-title">Work With Us</h3>
            <p className="contact-email">TikiSweetsCareer@gmail.com</p>
          </div>
        </div>

        {/* Navigation Links */}
        <div className="footer-nav">
          <a href="#" className="nav-link">About us</a>
          <a href="#" className="nav-link">Careers</a>
          <a href="#" className="nav-link">Our Story</a>
          <a href="#" className="nav-link">Contact Us</a>
        </div>

        {/* Copyright */}
        <div className="footer-copyright">
          <p className="copyright-text">© Copyright 2023. All rights reserved</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
