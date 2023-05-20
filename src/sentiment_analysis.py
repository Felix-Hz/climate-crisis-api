from textblob import TextBlob

def perform_sentiment_analysis(attitudes_data):
    sentiment_results = []
    for attitude in attitudes_data:
        text = attitude['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        sentiment_results.append((text, sentiment))
    return sentiment_results
