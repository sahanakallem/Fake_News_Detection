import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Make sure your CSS file is imported

function TitlePredictor() {
    const [title, setTitle] = useState('');
    const [prediction, setPrediction] = useState('');
    const [animateResult, setAnimateResult] = useState(false);

    const onTitleChange = (event) => {
        setTitle(event.target.value);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        setAnimateResult(false); // Reset animation state
        try {
            const response = await axios.post('http://localhost:5000/predict', { title });
            setPrediction(response.data.prediction);
            setAnimateResult(true); // Trigger animation
        } catch (error) {
            console.error('Error making prediction:', error);
        }
    };

    return (
        <div className="prediction-container">
            <header>
                <h1 className="header-title">Fake News Prediction</h1>
            </header>
            <form onSubmit={onSubmit}>
                <input
                    type="text"
                    value={title}
                    onChange={onTitleChange}
                    placeholder="Enter the news title..."
                />
                <button type="submit">Predict</button>
            </form>
            <div className={`result ${animateResult ? 'result-animation' : ''}`}>
                {prediction ? `The news is ${prediction}` : 'Awaiting prediction...'}
            </div>
        </div>
    );
}

export default TitlePredictor;
