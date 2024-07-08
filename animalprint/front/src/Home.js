import React from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';

const Home = () => {
  const navigate = useNavigate();

  const handleHelpClick = () => {
    alert("This application allows you to upload an image and analyze its content.");
  };

  const handleStartClick = () => {
    navigate('/upload');
  };

  return (
    <div className="home-container">
      <button className="help-button" onClick={handleHelpClick}>Help</button>
      <button className="start-button" onClick={handleStartClick}>Start</button>
    </div>
  );
};

export default Home;