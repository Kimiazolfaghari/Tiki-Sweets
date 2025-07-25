import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const ScrollToTop = () => {
  const { pathname } = useLocation();

  useEffect(() => {
    // فوری اسکرول کن
    window.scrollTo(0, 0);
    
    // اگر صفحه هنوز لود نشده، کمی صبر کن
    const handleScroll = () => {
      window.scrollTo(0, 0);
      document.documentElement.scrollTop = 0;
      document.body.scrollTop = 0;
    };

    // اجرای فوری
    handleScroll();
    
    // اجرای با تاخیر کوتاه
    const timer = setTimeout(handleScroll, 0);
    
    return () => clearTimeout(timer);
  }, [pathname]);

  return null;
};

export default ScrollToTop;