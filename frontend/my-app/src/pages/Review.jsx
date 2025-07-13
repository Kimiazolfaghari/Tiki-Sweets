import React, { useState } from 'react';
import { ArrowLeft } from 'lucide-react';
import '../styles/Review.css';

const FeedbackForm = () => {
  const [currentRating, setCurrentRating] = useState(5);
  const [feedbackText, setFeedbackText] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [hoveredRating, setHoveredRating] = useState(0);

  const ratingTexts = ['', 'Poor', 'Fair', 'Good', 'Very Good', 'Excellent'];

  const handleStarClick = (rating) => {
    setCurrentRating(rating);
  };

  const handleStarHover = (rating) => {
    setHoveredRating(rating);
  };

  const handleStarLeave = () => {
    setHoveredRating(0);
  };

  const handleTextChange = (e) => {
    setFeedbackText(e.target.value);
  };

  const submitFeedback = async () => {
    if (feedbackText.trim() === '') {
      alert('Please enter your feedback before submitting.');
      return;
    }

    setIsSubmitting(true);

    // Simulate API call
    setTimeout(() => {
      alert(`Thank you for your feedback!\nRating: ${currentRating} stars\nFeedback: ${feedbackText}`);
      setIsSubmitting(false);
      setFeedbackText('');
    }, 1000);
  };

  const goBack = () => {
    if (window.history.length > 1) {
      window.history.back();
    } else {
      console.log('No previous page to go back to.');
    }
  };

  const displayRating = hoveredRating || currentRating;

  return (
    <div className="feedback-container">
      <button className="back-button" onClick={goBack}>
        <ArrowLeft size={20} />
      </button>

      <div className="feedback-card">
        <h2 className="feedback-title">Share your feedback</h2>
        <p className="feedback-subtitle">
          Rating for this product: {ratingTexts[currentRating]}
        </p>
        
        <div className="feedback-rating-container">
          <div 
            className="feedback-stars"
            onMouseLeave={handleStarLeave}
          >
            {[1, 2, 3, 4, 5].map((star) => (
              <span
                key={star}
                className={`feedback-star ${displayRating >= star ? 'active' : ''}`}
                onClick={() => handleStarClick(star)}
                onMouseEnter={() => handleStarHover(star)}
              >
                ★
              </span>
            ))}
          </div>
        </div>

        <div className="textarea-container">
          <textarea 
            className="feedback-textarea" 
            placeholder="Enter your text..."
            value={feedbackText}
            onChange={handleTextChange}
            rows="4"
          />
        </div>

        <button 
          className="submit-button" 
          onClick={submitFeedback}
          disabled={isSubmitting}
        >
          {isSubmitting ? 'Submitting...' : 'Submit Review'}
        </button>
      </div>
    </div>
  );
};

export default FeedbackForm;
