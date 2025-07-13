import React, { useState } from 'react';
import { ArrowLeft, Package, Truck, CheckCircle, Clock } from 'lucide-react';
import '../styles/OrderTracking.css';

const OrderTracking = () => {
  const [orderData] = useState({
    orderId: '3354654654526',
    orderDate: 'Apr 4, 2025',
    estimatedDelivery: 'Apr 4 2025',
    items: [
      { 
        name: 'Berry Delight Dessert', 
        price: 12, 
        quantity: 1, 
        image: '/img/desserts/17.jpg' // آدرس عکس از حافظه محلی
      },
      { 
        name: 'Caramel Cheesecake', 
        price: 10, 
        quantity: 1, 
        image: '/img/cheesecakes/02.jpg' // آدرس عکس از حافظه محلی
      },
      { 
        name: 'Vanilla Cupcake', 
        price: 8.5, 
        quantity: 1, 
        image: '/img/cupcakes/02.jpg' // آدرس عکس از حافظه محلی
      }
    ],
    delivery: {
      address: '647 Jewess Bridge Apt',
      city: 'T74 London, UK',
      phone: '474-769-3919'
    },
    total: 40.5,
    status: 'confirmed'
  });

  const [currentStep, setCurrentStep] = useState(2);

  const steps = [
    { id: 1, label: 'Order Confirmed', icon: CheckCircle, date: 'Fri, 4 th Apr' },
    { id: 2, label: 'Out For Delivery', icon: Truck, date: 'Fri, 4 th Apr' },
    { id: 3, label: 'Delivered', icon: Package, date: 'Expected by: Fri 4th' }
  ];

  const goBack = () => {
    if (window.history.length > 1) {
      window.history.back();
    } else {
      console.log('No previous page to go back to.');
    }
  };

  const getStepStatus = (stepId) => {
    if (stepId < currentStep) return 'completed';
    if (stepId === currentStep) return 'active';
    return 'pending';
  };

  return (
    <div className="tracking-container">
      <button className="back-button" onClick={goBack}>
        <ArrowLeft size={20} />
      </button>

      <div className="tracking-content">
        <div className="order-card">
          <div className="order-header">
            <h1 className="order-id">Order ID: {orderData.orderId}</h1>
            <div className="order-details">
              <span>Order date: {orderData.orderDate}</span>
              <span>Estimated delivery: {orderData.estimatedDelivery}</span>
            </div>
            <div className="status-badge">Order Confirmed</div>
          </div>

          <div className="tracking-steps">
            {steps.map((step) => {
              const status = getStepStatus(step.id);
              const IconComponent = step.icon;
              
              return (
                <div key={step.id} className={`step ${status}`}>
                  <div className="step-icon">
                    <IconComponent size={20} />
                  </div>
                  <div className="step-content">
                    <div className="step-label">{step.label}</div>
                    <div className="step-date">{step.date}</div>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="items-section">
            <h3 className="section-title">Order Items</h3>
            {orderData.items.map((item, index) => (
              <div key={index} className="item">
                <div className="item-info">
                  <div className="item-image">
                    <img 
                      src={item.image} 
                      alt={item.name}
                      onError={(e) => {
                        e.target.style.display = 'none';
                        e.target.nextSibling.style.display = 'block';
                      }}
                    />
                    <div className="image-fallback" style={{display: 'none'}}>
                      🍰
                    </div>
                  </div>
                  <div className="item-details">
                    <div className="item-name">{item.name}</div>
                    <div className="item-quantity">Quantity: {item.quantity}</div>
                  </div>
                </div>
                <div className="item-price">${item.price}</div>
              </div>
            ))}
          </div>

          <div className="delivery-section">
            <h3 className="section-title">Delivery Address</h3>
            <div className="delivery-address">
              <div className="address-line">{orderData.delivery.address}</div>
              <div className="address-line">{orderData.delivery.city}</div>
              <div className="address-line">{orderData.delivery.phone}</div>
            </div>
          </div>

          <div className="total-section">
            <div className="total-row">
              <span>Discount</span>
              <span>$0</span>
            </div>
            <div className="total-row">
              <span>Delivery</span>
              <span>$10</span>
            </div>
            <div className="total-row final">
              <span>Total</span>
              <span>${orderData.total}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default OrderTracking;