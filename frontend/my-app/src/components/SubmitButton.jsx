import React from 'react';

const SubmitButton = ({ label }) => {
  return (
    <button type="submit" className="register-btn">
      {label}
    </button>
  );
};

export default SubmitButton;
