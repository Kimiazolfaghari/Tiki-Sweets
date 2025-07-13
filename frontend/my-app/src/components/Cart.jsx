import React, { useState } from 'react';
import { ArrowLeft, Minus, Plus } from 'lucide-react';
import { useNavigate } from 'react-router-dom'; // اضافه کردن useNavigate
import '../styles/Cart.css';

const DessertCart = () => {
  const navigate = useNavigate(); // استفاده از useNavigate
  const [cartItems, setCartItems] = useState([
    {
      id: 1,
      name: 'Berry Delight Dessert',
      price: 12,
      quantity: 1,
      image: '/img/desserts/17.jpg'
    },
    {
      id: 2,
      name: 'Caramel Cheesecake', 
      price: 10,
      quantity: 1,
      image: '/img/cheesecakes/02.jpg'
    },
    {
      id: 3,
      name: 'Vanilla Cupcake',
      price: 8.5,
      quantity: 1,
      image: '/img/cupcakes/02.jpg'
    }
  ]);

  const updateQuantity = (id, change) => {
    setCartItems(items =>
      items.map(item =>
        item.id === id
          ? { ...item, quantity: Math.max(0, item.quantity + change) }
          : item
      ).filter(item => item.quantity > 0)
    );
  };

  const removeItem = (id) => {
    setCartItems(items => items.filter(item => item.id !== id));
  };

  const subtotal = cartItems.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  return (
    <div className="cart-container">
      {/* Header */}
      <div className="cart-header">
        <button className="back-button" onClick={() => navigate('/')}> {/* دکمه برگشت */}
          <ArrowLeft size={20} />
        </button>
        
        <h1 className="cart-title">
          Cart 🛒
        </h1>
        
        <div className="header-spacer"></div>
      </div>

      {/* Cart Items */}
      <div className="cart-items">
        {cartItems.map((item, index) => (
          <div key={item.id} className={`cart-item ${index < cartItems.length - 1 ? 'with-border' : ''}`}>
            {/* Product Image */}
            <div className="item-image">
              <img 
                src={item.image}
                alt={item.name}
              />
            </div>

            {/* Product Info */}
            <div className="item-info">
              <h3 className="item-name">
                {item.name}
              </h3>
              <p className="item-price">
                ${item.price}
              </p>
            </div>

            {/* Quantity Controls */}
            <div className="quantity-controls">
              <button
                onClick={() => updateQuantity(item.id, -1)}
                className="quantity-button"
              >
                <Minus size={14} />
              </button>
              
              <span className="quantity-display">
                {item.quantity}
              </span>
              
              <button
                onClick={() => updateQuantity(item.id, 1)}
                className="quantity-button"
              >
                <Plus size={14} />
              </button>
            </div>

            {/* Delete Button */}
            <button
              onClick={() => removeItem(item.id)}
              className="delete-button"
            >
              Delete
            </button>
          </div>
        ))}
      </div>

      {/* Subtotal */}
      <div className="cart-subtotal">
        <div className="subtotal-row">
          <span className="subtotal-label">Subtotal :</span>
          <span className="subtotal-amount">${subtotal.toFixed(1)}</span>
        </div>
      </div>

      {/* Checkout Button */}
      <div className="checkout-section">
        <button className="checkout-button">
          Checkout
        </button>
      </div>
    </div>
  );
};

export default DessertCart;
