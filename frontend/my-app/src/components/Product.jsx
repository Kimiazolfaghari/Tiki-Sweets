import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import productsData from '../Products.json';
import ActionButton from './ActionButton';
import '../styles/Product.css';

const ProductDetails = () => {
  const { category, id } = useParams();
  const navigate = useNavigate();
  const [quantity, setQuantity] = useState(1);

  const productList = productsData[category];
  const product = productList?.find(p => p.id === parseInt(id));

  if (!product) {
    return <div className="product-not-found">Product not found</div>;
  }

  const handleQuantityChange = (change) => {
    setQuantity(Math.max(1, quantity + change));
  };

  const handleAddToCart = () => {
    alert(`Added ${quantity} ${product.name}(s) to cart!`);
  };

  const handleAddReview = () => {
    navigate("/Review");
  };

  return (
    <div className="product-container-page">
      <div className="product-card-page">
        <div className="product-main-page">
          <div className="product-image-section-page">
            <div className="product-image-container-page">
              <img
                src={product.image}
                alt={product.name}
                className="product-image-page"
              />
            </div>
            <div className="product-category-page">
              <span>{category}</span>
            </div>
          </div>

          <div className="product-info-page">
            <div className="product-header-page">
              <h1 className="product-title-page">{product.name}</h1>
              <p className="product-description-page">
                Enjoy our delicious {product.name} with rating {product.rating}★ and perfect price!
              </p>
            </div>

            <div className="product-rating-page">
              <div className="stars-page">
                {[...Array(5)].map((_, index) => (
                  <svg
                    key={index}
                    className="star-icon"
                    viewBox="0 0 24 24"
                    fill={index < Math.round(product.rating) ? "#fbbf24" : "#e5e7eb"}
                    width="16"
                    height="16"
                  >
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                  </svg>
                ))}
              </div>
            </div>

            <div className="product-details-page">
              <div className="price-section-page">
                <span className="price-label-page">PRICE</span>
                <span className="price-value-page">${product.price}</span>
              </div>

              <div className="quantity-section-page">
                <span className="quantity-label-page">QUANTITY</span>
                <div className="quantity-controls-page">
                  <button onClick={() => handleQuantityChange(-1)} className="quantity-btn-page">−</button>
                  <span className="quantity-display-page">{quantity}</span>
                  <button onClick={() => handleQuantityChange(1)} className="quantity-btn-page">+</button>
                </div>
              </div>
            </div>

            <ActionButton
              text="Add to Cart"
              onClick={handleAddToCart}
              variant="default"
              className="add-to-cart-btn-page"
            />
          </div>
        </div>

        <div className="reviews-section-page">
          <h2 className="reviews-title-page">Reviews</h2>
          <div className="reviews-list-page">
            {["Sarah Johnson", "Michael Chen"].map((name, index) => (
              <div className="review-item-page" key={index}>
                <div className="review-header-page">
                  <div
                    className="reviewer-avatar-page"
                    style={{
                      background: index % 2 === 0
                        ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
                        : 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
                    }}
                  >
                    {name[0]}
                  </div>
                  <div className="reviewer-info-page">
                    <h3 className="reviewer-name-page">{name}</h3>
                    <div className="review-stars-page">
                      {[...Array(4)].map((_, idx) => (
                        <svg
                          key={idx}
                          className="star-icon"
                          viewBox="0 0 24 24"
                          fill={idx < 4 ? "#fbbf24" : "#e5e7eb"}
                          width="16"
                          height="16"
                        >
                          <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                        </svg>
                      ))}
                    </div>
                  </div>
                </div>
                <p className="review-text-page">
                  “Absolutely delicious! Highly recommended.”
                </p>
              </div>
            ))}
          </div>

          <ActionButton
            text="Add Your Review"
            onClick={handleAddReview}
            variant="outline"
            className="add-review-btn-page"
          />
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;
