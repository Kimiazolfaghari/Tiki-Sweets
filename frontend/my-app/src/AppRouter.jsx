import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';

// صفحات اصلی
import Register from './pages/Register';
import Login from './pages/Login';
import VerifyAccount from './pages/VerifyAccount';
import Home from './pages/Home';
import CustomCake from './pages/CustomCake';
import ProductListing from './pages/ProductListing';
import Cart from './pages/CartPage';
import Profile from './pages/ProfilePage';
import Footer from './components/Footer';
import Address from './pages/Address';
import Review from './pages/Review';
import OrderTracking from './pages/OrderTracking';
import PaymentForm from './pages/PaymentForm';
import ProductDetails from './pages/ProductDetails';

// صفحات ادمین
import AdminDashboard from './pages/admin/AdminDashboard';
import AdminRoute from './routes/AdminRoute';

const AppRouter = () => {
  return (
    <>
      <ScrollToTop />
      <Routes>
        {/* مسیرهای عمومی */}
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/verify" element={<VerifyAccount />} />
        <Route path="/customcake" element={<CustomCake />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/footer" element={<Footer />} />
        <Route path="/address" element={<Address />} />
        <Route path="/review" element={<Review />} />
        <Route path="/ordertracking" element={<OrderTracking />} />
        <Route path="/paymentform" element={<PaymentForm />} />
        <Route path="/productlisting" element={<ProductListing />} />
        <Route path="/products/:category" element={<ProductListing />} />
        <Route path="/product/:category/:id" element={<ProductDetails />} />

        {/* مسیر ادمین محافظت‌شده */}
        <Route
          path="/admin"
          element={
            <AdminRoute>
              <AdminDashboard />
            </AdminRoute>
          }
        />
      </Routes>
    </>
  );
};

export default AppRouter;
