import streamlit as st
import pandas as pd
from scrape_reddit import scrape_reddit_posts
from scrape_twitter import scrape_tweets
from sentiment import analyze_sentiment
from data_processor import extract_and_aggregate

st.set_page_config(page_title="Live Meme Stock Tracker", page_icon="🚀")
st.title("🚀 Live Meme Stock Swing Predictor")

st.markdown("Scraping **Reddit** and **Twitter** for trending meme stock mentions...")

# Step 1: Scrape posts
reddit_posts = scrape_reddit_posts()
twitter_posts = scrape_tweets()

# Step 2: Combine and analyze sentiment
all_posts = reddit_posts + twitter_posts
scored_posts = analyze_sentiment(all_posts)

# Step 3: Extract tickers and aggregate
summary_df = extract_and_aggregate(scored_posts)

# Step 4: Filter and display
price_filter = st.slider("Max Stock Price", 1, 200, 50)
filtered = summary_df[summary_df["Current Price"] <= price_filter]
st.subheader("📈 Top Meme Stock Candidates")
st.dataframe(filtered.sort_values("Total Mentions", ascending=False).reset_index(drop=True))