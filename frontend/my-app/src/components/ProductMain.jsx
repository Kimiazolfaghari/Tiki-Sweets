import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ProductCard from './ProductCard';
import '../styles/ProductMain.css';
import productsData from '../Products.json';

const ProductMain = () => {
  const { category } = useParams();
  const navigate = useNavigate();
  const [activeCategory, setActiveCategory] = useState(category || "Cakes");
  const [activePage, setActivePage] = useState(1);
  const [products, setProducts] = useState(productsData);
  const productsPerPage = 9;

  const categories = ['Cakes', 'CupCakes', 'SlicedCake', 'Donut', 'CheeseCakes', 'Desserts'];

  useEffect(() => {
    setActiveCategory(category || 'Cakes');
    setActivePage(1);
  }, [category]);

  const handleCategoryClick = (newCategory) => {
    setActiveCategory(newCategory);
    setActivePage(1);
  };

  const handlePageChange = (pageNumber) => {
    setActivePage(pageNumber);
  };

  const handleProductClick = (product) => {
    navigate(`/product/${activeCategory}/${product.id}`);
  };

  const categoryProducts = products[activeCategory] || [];
  const indexOfLastProduct = activePage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
  const currentProducts = categoryProducts.slice(indexOfFirstProduct, indexOfLastProduct);

  return (
    <section className="product-main">
      <div className="container">
        <div className="category-menu">
          {categories.map((cat, index) => (
            <span
              key={index}
              className={`category-item ${activeCategory === cat ? 'active' : ''}`}
              onClick={() => handleCategoryClick(cat)}
            >
              {cat}
            </span>
          ))}
        </div>

        <div className="products-grid">
          {currentProducts.map(product => (
            <ProductCard
              key={product.id}
              product={product}
              onBuyClick={() => handleProductClick(product)}
            />
          ))}
        </div>

        <div className="pagination-dots">
          {[1, 2, 3].map(page => (
            <span
              key={page}
              className={`dot ${activePage === page ? 'active' : ''}`}
              onClick={() => handlePageChange(page)}
            >
              {page}
            </span>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ProductMain;
