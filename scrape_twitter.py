import snscrape.modules.twitter as sntwitter

def scrape_tweets(limit=50):
    results = []
    query = "($GME OR AMC OR BBBY OR TSLA OR AAPL) lang:en"
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        results.append({"source": "twitter", "title": tweet.content})
    return results