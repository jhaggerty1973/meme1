# Meme Stock Swing Predictor v3 (Live)

## Features
- ✅ Live scraping from Reddit (r/WallStreetBets)
- ✅ Live scraping from Twitter using snscrape
- ✅ Sentiment analysis using VADER
- ✅ Aggregation and filtering by stock symbol

## Setup
```
pip install -r requirements.txt
streamlit run app.py
```

## Notes
- Twitter scraping uses snscrape (no API key required)
- Reddit uses pushshift.io (public access)