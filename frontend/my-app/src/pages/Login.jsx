import React from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  return (
    <div className="card shadow p-4">
      <h2 className="mb-3">ورود</h2>
      <form>
        <input type="text" placeholder="نام کاربری یا ایمیل" className="form-control mb-3" />
        <input type="password" placeholder="رمز عبور" className="form-control mb-3" />
        <button className="btn btn-success w-100">ورود</button>
      </form>
      <p className="text-center mt-3">
        حساب نداری؟ <Link to="/">ثبت‌نام</Link>
      </p>
    </div>
  );
};

export default Login;
