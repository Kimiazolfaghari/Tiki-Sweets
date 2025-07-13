import React from 'react';

const CakeCard = ({ image, label }) => {
  return (
    <div className="cake-card">
      <img src={image} alt={label} />
      <div className="cake-label">{label}</div>
      <button className="view-more">View More →</button>
    </div>
  );
};

export default CakeCard;
