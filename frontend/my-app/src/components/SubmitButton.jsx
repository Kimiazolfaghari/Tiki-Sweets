import React from 'react';

const SubmitButton = ({ label }) => {
  return (
    <button type="submit" className="btn register-btn w-100">
      {label}
    </button>
  );
};

export default SubmitButton;
