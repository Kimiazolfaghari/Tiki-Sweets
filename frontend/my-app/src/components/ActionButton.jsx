import React from 'react';
import '../styles/ActionButton.css';

const ActionButton = ({ 
  text, 
  onClick, 
  variant = 'default', 
  disabled = false,
  type = 'button',
  ariaLabel,
  className = '',
  ...props 
}) => {
  return (
    <button
      className={`action-button action-button--${variant} ${className}`}
      onClick={onClick}
      disabled={disabled}
      type={type}
      aria-label={ariaLabel || text}
      {...props}
    >
      {text}
      {/* آیکون فلش - اگر تصویر وجود ندارد از یونیکد استفاده کنید */}
      <img 
        src='/img/icons/right-arrow.png' 
        alt="" 
        className="button-arrow" 
        aria-hidden="true" 
      />
      {/* جایگزین برای تصویر اگر وجود ندارد: */}
      {/* <span className="button-arrow" aria-hidden="true">→</span> */}
    </button>
  );
};

export default ActionButton;

// نحوه استفاده:
/*
// حالت پیش‌فرض
<ActionButton text="View More" onClick={handleClick} />

// حالت‌های مختلف
<ActionButton text="View More" onClick={handleClick} variant="rounded" />
<ActionButton text="View More" onClick={handleClick} variant="light" />
<ActionButton text="View More" onClick={handleClick} variant="pill" />

// با props اضافی
<ActionButton 
  text="Submit" 
  onClick={handleSubmit} 
  variant="default"
  disabled={isLoading}
  type="submit"
  ariaLabel="Submit form"
/>
*/