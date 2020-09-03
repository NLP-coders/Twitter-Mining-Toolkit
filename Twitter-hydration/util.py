
import tweepy
class TweepyHeplers:

    @staticmethod
    def lookup_tweets(tweet_IDs, api):
        tweet_IDs = ["1221583632713879552", "1221583632713879552"] 
        full_tweets = []
        tweet_count = len(tweet_IDs)
        print( "Number of tweets to lookup for: %d "  % (tweet_count))
        try:
            full_tweets.extend( api.statuses_lookup(id_=tweet_IDs))
        except tweepy.TweepError as e:
            print(e)
            print( e.api_code)
            return [status._json for status in full_tweets]
            
        return [status._json for status in full_tweets]