import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Register from './pages/Register';
import Login from './pages/Login';
import VerifyAccount from './pages/VerifyAccount';

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Register />} />
      <Route path="/register" element={<Register />} /> {/* این خط اضافه شده */}
      <Route path="/login" element={<Login />} />
      <Route path="/verify" element={<VerifyAccount />} />
    </Routes>
  );
};

export default AppRouter;
