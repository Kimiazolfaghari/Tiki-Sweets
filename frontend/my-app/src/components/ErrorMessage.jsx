import React from 'react';

const ErrorMessage = ({ message }) => {
  if (!message) return null;
  return <div className="text-danger small mb-2">{message}</div>;
};

export default ErrorMessage;
