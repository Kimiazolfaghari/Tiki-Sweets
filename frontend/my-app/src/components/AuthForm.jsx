import React from 'react';

const AuthForm = ({ children, title }) => {
  return (
    <div className="container d-flex justify-content-center align-items-center min-vh-100 bg-light">
      <div className="card p-4 shadow-lg" style={{ maxWidth: '400px', width: '100%' }}>
        <h3 className="text-center mb-2">{title}</h3>
        {children}
      </div>
    </div>
  );
};

export default AuthForm;
