import React from 'react';
import AppRouter from './AppRouter';
import ScrollToTop from './components/ScrollToTop'; // اضافه شده

const App = () => {
  return (
    <div className="w-100 p-0 m-0">
      <ScrollToTop /> {/* این باید اینجا باشه */}
      <AppRouter />
    </div>
  );
};

export default App;
