import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import '../styles/CakeSlider.css';

import ActionButton from './ActionButton';

// تعریف اطلاعات اسلایدها
const cakes = [
  { image: '/img/slider1/02.jpg', label: 'Birthday Cakes', category: 'Cakes' },
  { image: '/img/slider1/03.jpg', label: 'Cupcakes', category: 'CupCakes' },
  { image: '/img/slider1/04.jpg', label: 'Sliced Cakes', category: 'SlicedCake' },
  { image: '/img/slider1/05.jpg', label: 'Donuts', category: 'Donut' },
  { image: '/img/slider1/06.jpg', label: 'Cheesecakes', category: 'CheeseCakes' },
  { image: '/img/slider1/01.jpg', label: 'Desserts', category: 'Desserts' },
];

const CakeSlider = () => {
  const navigate = useNavigate();

  const handleViewMore = (category) => {
    if (category) {
      navigate(`/products/${category}`);
    } else {
      console.warn('Category not found for this item.');
    }
  };

  return (
    <section className="cake-slider-section">
      <Swiper
        modules={[Navigation]}
        navigation
        loop={true}
        centeredSlides={true}
        slidesPerView={3}
        spaceBetween={10}
        className="cake-swiper"
      >
        {cakes.map((cake, index) => (
          <SwiperSlide key={index}>
            <div className="cake-slide">
              <img src={cake.image} alt={cake.label} />
              <div className="cake-info">
                <div className="cake-label">{cake.label}</div>
                <ActionButton
                  text="View More"
                  onClick={() => handleViewMore(cake.category)}
                />
              </div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </section>
  );
};

export default CakeSlider;
