import React from 'react';
import '../styles/ProductCard.css';

const ProductCard = ({ product, onBuyClick }) => {
  // تابع برای نمایش ستاره‌ها
  const renderStars = (rating) => {
    const stars = [];
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;
    
    // ستاره‌های پر
    for (let i = 0; i < fullStars; i++) {
      stars.push(<span key={i} className="star">★</span>);
    }
    
    // نیم ستاره
    if (hasHalfStar) {
      stars.push(<span key="half" className="star half">☆</span>);
    }
    
    // ستاره‌های خالی
    const emptyStars = 5 - Math.ceil(rating);
    for (let i = 0; i < emptyStars; i++) {
      stars.push(<span key={`empty-${i}`} className="star empty">☆</span>);
    }
    
    return stars;
  };

  return (
    <div className="product-card">
      <div className="product-image">
        <img src={product.image} alt={product.name} />
      </div>
      
      <div className="product-card-info">
        <h3 className="product-title">{product.name}</h3>
        <p className="product-price">${product.price}</p>
        
        <div className="product-rating">
          {renderStars(product.rating)}
        </div>
        
        <button 
          className="action-button action-button--default"
          onClick={() => onBuyClick(product)}
        >
          Buy Now 🛒
        </button>
      </div>
    </div>
  );
};

export default ProductCard;