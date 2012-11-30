import tweepy

def best_movies():
    public_tweets = tweepy.api.search('saw movie best OR amazing OR great +exclude:retweets')
    return [tweet.text for tweet in public_tweets]

