# Fake_news_detection using Deep Learning

This repository contains the implementation of four different deep learning models to address the challenge of fake news detection. We have experimented with LSTM, Bi-LSTM, CNN, and BERT models, utilizing K-fold cross-validation to ensure the robustness and reliability of our results.

## Project Overview

Fake news detection is a critical task in the era of widespread digital information, where false news can spread rapidly. Our project aims to leverage deep learning techniques to automatically detect and classify news articles as "real" or "fake."

## Models Implemented

- **LSTM (Long Short-Term Memory)**: A type of recurrent neural network (RNN) suitable for sequence prediction problems.
- **Bi-LSTM (Bidirectional LSTM)**: Extends the traditional LSTMs by running inputs in two ways, one from past to future and one from future to past which is useful to capture context from both sides.
- **CNN (Convolutional Neural Network)**: Generally used for image detection, in this project, we use CNN for text classification to identify patterns in sentence structures that typically indicate fake news.
- **BERT (Bidirectional Encoder Representations from Transformers)**: A transformer-based machine learning technique developed by Google and designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.

## Dataset

The dataset utilized in this project comprises two CSV files sourced from GossipCop, categorized into fake and real news samples. The files are used to train and test the deep learning models to distinguish between fake and real news articles:
 - `gossipcop_fake.csv` - Samples related to fake news collected from GossipCop
  - `gossipcop_real.csv` - Samples related to real news collected from GossipCop
Detailed descriptions of how these files are preprocessed and utilized in the models are provided in the Jupyter notebooks within this repository.

## Requirements

To run this project, you will need Python 3.x and the following libraries:
- numpy
- pandas
- tensorflow
- keras
- sklearn
- transformers

Install the required packages using:
```bash
pip install -r requirements.txt
```
## Front-end and Back-end Implementation

Frontend is created using React-js
Backend is created using Flask 
## Usage

Detailed instructions on how to train and evaluate each model are provided in the Jupyter notebooks within this repository. To get started, clone this repository and run the Jupyter notebooks.
For easier run: Edit the .bat file and replace the path for the app.py and similarly do the same for app.js.
Save and Double-click the .bat file

## Results

Each model's performance metrics, such as accuracy and loss, are summarized in the `Results` section. These results are based on the K-fold cross-validation approach to ensure model effectiveness across different subsets of the dataset.
