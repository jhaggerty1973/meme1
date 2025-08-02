# Meme Stock Swing Predictor v2 (Beta)

This version integrates Reddit + Twitter sentiment and mention volume to identify trending meme stocks.

## Features
- Filters stocks by real-time buzz (Reddit and Twitter)
- Ranks top meme stocks by total mentions and sentiment
- Optional price filter for swing trading under $X

## Coming Soon
- Real-time scraping from Reddit and Twitter
- Sentiment NLP using VADER or FinBERT
- News and SEC filing parsing
- ML model for swing trade prediction

## To Run

```bash
pip install -r requirements.txt
streamlit run app.py
```