
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meme Stock Swing Predictor", page_icon="🚀")
st.title("🚀 Meme Stock Swing Predictor")

st.markdown("""
This version scans **Reddit (r/WallStreetBets)** and **Twitter** to identify trending meme stocks based on:
- Mention frequency
- Combined sentiment score
- Price filter and swing trade prediction (coming soon)
""")

# Placeholder mentions (simulate Reddit + Twitter scanning)
combined_mentions = {
    "Ticker": ["GME", "AMC", "CVNA", "BBBY", "SPCE", "PLTR", "NOK", "TSLA", "AAPL", "RIVN"],
    "Reddit Mentions": [820, 740, 300, 280, 270, 260, 250, 210, 200, 190],
    "Twitter Mentions": [500, 460, 700, 300, 320, 400, 150, 800, 900, 450],
    "Total Mentions": [1320, 1200, 1000, 580, 590, 660, 400, 1010, 1100, 640],
    "Sentiment": [0.77, 0.72, 0.80, 0.66, 0.68, 0.74, 0.55, 0.59, 0.61, 0.69],
    "Current Price": [18.5, 9.0, 48.3, 0.85, 3.1, 22.4, 4.2, 250.0, 179.0, 19.2],
}

df = pd.DataFrame(combined_mentions)
df = df.sort_values(by="Total Mentions", ascending=False)

# Price filter
price_filter = st.slider("Filter by Maximum Price", min_value=1, max_value=100, value=25)
filtered_df = df[df["Current Price"] <= price_filter]

st.subheader("🔥 Top Meme Stocks by Total Mentions (Reddit + Twitter)")
st.dataframe(filtered_df.reset_index(drop=True))

st.markdown("⚠️ Real-time scraping in development. This version uses simulated data.")
