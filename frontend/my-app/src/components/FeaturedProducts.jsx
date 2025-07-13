import React from 'react';
import { useNavigate } from 'react-router-dom';
import ProductCard from './ProductCard';
import productsData from '../Products.json';
import '../styles/FeaturedProducts.css';

const FeaturedProducts = () => {
  const navigate = useNavigate();

  const products = [
    { ...productsData.Cakes[0], category: "Cakes" },
    { ...productsData.CupCakes[1], category: "CupCakes" },
    { ...productsData.CheeseCakes[2], category: "CheeseCakes" },
    { ...productsData.Donut[0], category: "Donut" },
    { ...productsData.Desserts[0], category: "Desserts" },
    { ...productsData.SlicedCake[0], category: "SlicedCake" }
  ];

  const handleViewMore = (product) => {
    navigate(`/product/${product.category}/${product.id}`);
  };

  return (
    <section className="featured-products" id="featured-products">
      <h2 className="featured-title">Featured Products</h2>

      <div className="products-grid">
        {products.map(product => (
          <ProductCard
            key={`${product.category}-${product.id}`}
            product={product}
            onBuyClick={() => handleViewMore(product)}
          />
        ))}
      </div>
    </section>
  );
};

export default FeaturedProducts;
