import React from 'react';

const InputField = ({ type = 'text', placeholder, name, value, onChange }) => {
  return (
    <input
      type={type}
      name={name}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className="form-control mb-3 custom-input"
    />
  );
};

export default InputField;
