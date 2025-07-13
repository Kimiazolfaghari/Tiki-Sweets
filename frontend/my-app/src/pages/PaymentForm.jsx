import React, { useState } from 'react';
import { ArrowLeft } from 'lucide-react';
import '../styles/PaymentForm.css';

const PaymentForm = () => {
  const [cardholderName, setCardholderName] = useState('PAULINA CHIMAKORE');
  const [cardNumber, setCardNumber] = useState('9870 3456 7890 6473');
  const [expiry, setExpiry] = useState('03 / 25');
  const [cvv, setCvv] = useState('6154');
  const [discountCode, setDiscountCode] = useState('WELCOME10');

  const goBack = () => {
    if (window.history.length > 1) {
      window.history.back();
    } else {
      console.log('No previous page to go back to.');
    }
  };

  return (
    <div className="payment-container">
      <div className="payment-card">
        <div className="payment-content">
          {/* Left Side - Payment Form */}
          <div className="payment-form-section">
            <div className="back-button-container">
              <button className="back-button" onClick={goBack}>
                <ArrowLeft className="back-icon" />
              </button>
            </div>
            
            <h1 className="payment-title">
              Let's Make Payment
            </h1>
            <p className="payment-description">
              To start your subscription, input your card details to make payment.<br />
              You will be redirected to your banks authorization page.
            </p>

            <div className="form-container">
              {/* Cardholder's Name */}
              <div className="form-group">
                <label className="form-label">
                  Cardholder's Name
                </label>
                <input
                  type="text"
                  value={cardholderName}
                  onChange={(e) => setCardholderName(e.target.value)}
                  className="form-input cardholder-input"
                />
              </div>

              {/* Card Number */}
              <div className="form-group">
                <label className="form-label">
                  Card Number
                </label>
                <div className="card-input-container">
                  <input
                    type="text"
                    value={cardNumber}
                    onChange={(e) => setCardNumber(e.target.value)}
                    placeholder="0000 0000 0000 0000"
                    className="form-input card-number-input"
                  />
                </div>
              </div>

              {/* Expiry and CVV */}
              <div className="form-row">
                <div className="form-group">
                  <label className="form-label">
                    Expiry
                  </label>
                  <input
                    type="text"
                    value={expiry}
                    onChange={(e) => setExpiry(e.target.value)}
                    placeholder="MM / YY"
                    className="form-input"
                  />
                </div>
                <div className="form-group">
                  <label className="form-label">
                    CVV2
                  </label>
                  <input
                    type="text"
                    value={cvv}
                    onChange={(e) => setCvv(e.target.value)}
                    placeholder="000"
                    className="form-input"
                  />
                </div>
              </div>

              {/* Discount Code */}
              <div className="form-group">
                <label className="form-label">
                  Discount Code
                </label>
                <div className="discount-container">
                  <input
                    type="text"
                    value={discountCode}
                    onChange={(e) => setDiscountCode(e.target.value)}
                    className="form-input discount-input"
                  />
                  <button className="apply-button">
                    Apply
                  </button>
                </div>
              </div>

              {/* Pay Button */}
              <button
                onClick={() => console.log('Payment submitted')}
                className="pay-button"
              >
                Pay
              </button>
            </div>
          </div>

          {/* Right Side - Order Summary */}
          <div className="order-summary">
            <div className="payment-amount">
              <p className="amount-label">You're paying,</p>
              <p className="amount-value">$40.5</p>
            </div>

            <div className="order-items">
              <div className="order-item">
                <div className="item-info">
                  <p className="item-name">Berry Delight Dessert</p>
                </div>
                <p className="item-price">$ 12</p>
              </div>

              <div className="order-item">
                <div className="item-info">
                  <p className="item-name">Caramel Cheesecake</p>
                </div>
                <p className="item-price">$ 10</p>
              </div>

              <div className="order-item">
                <div className="item-info">
                  <p className="item-name">Vanilla Cupcake</p>
                </div>
                <p className="item-price">$ 8.5</p>
              </div>
            </div>

            <div className="order-total">
              <div className="total-row">
                <p className="total-label">Tax</p>
                <p className="total-price">$ 10</p>
              </div>
              
              <div className="final-total">
                <p className="final-label">Total</p>
                <p className="final-price">$ 40.5</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PaymentForm;
