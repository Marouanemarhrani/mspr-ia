import React, { useState } from 'react';
import './App.css';

const Upload = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleAnalyzeClick = () => {
    if (file) {
      // Simulate analysis
      setTimeout(() => {
        setResult('The image contains a cat.');
      }, 2000);
    }
  };

  return (
    <div className="upload-container">
      <input type="file" onChange={handleFileChange} />
      <button className="analyze-button" onClick={handleAnalyzeClick}>Analyze</button>
      {result && <p className="result-text">{result}</p>}
    </div>
  );
};

export default Upload;