// src/context/AuthContext.jsx
import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); 

  // خواندن توکن از localStorage در شروع برنامه
  useEffect(() => {
    const token = localStorage.getItem('token');
    const email = localStorage.getItem('email');
    if (token && email) {
      setUser({ token, email });
    }
  }, []);

  // ذخیره توکن و ایمیل پس از لاگین موفق
  const login = ({ token, email, isAdmin }) => {
    localStorage.setItem('token', token);
    localStorage.setItem('email', email);
    localStorage.setItem('isAdmin', isAdmin); 
    setUser({ token, email, isAdmin }); 
  };


  // حذف اطلاعات در logout
  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('email');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
