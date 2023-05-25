import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def scrape_attitudes():
    '''
        Tried to access Twitter's API to scrape public data.

    '''
    # Twitter API credentials
    api_key = API_KEY
    api_secret_key = API_SECRET_KEY
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_TOKEN_SECRET

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Search for tweets related to climate change
    query = '("climate change" OR "global warming" OR "environmental crisis" OR "carbon emissions")'

    tweets = api.search_tweets(q=query, tweet_mode='extended', count=100)

    attitudes_data = []

    for tweet in tweets:
        attitude = {
            'id': tweet.id,
            'text': tweet.full_text,
            'user': tweet.user.screen_name,
            'created_at': tweet.created_at,
            'retweets': tweet.retweet_count,
            'favorites': tweet.favorite_count,
            'hashtags': [h['text'] for h in tweet.entities['hashtags']],
            'mentions': [m['screen_name'] for m in tweet.entities['user_mentions']]
            # Add more metadata fields as per your requirement
        }
        attitudes_data.append(attitude)

    return attitudes_data


data = scrape_attitudes()
