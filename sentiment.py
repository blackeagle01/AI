import tweepy
import textblob

consumer_key='8CiTfiJlD5BEbyXGKddnU0lt1'
consumer_secret='hUJjCgJiadw3Vetp0LCbHmp9PW8mQvXFRjoeBiwaFM0pQc9R5E'

access_token='487685621-RbBa20ZhW40u9dEnaUkCs51GG5NIls6HQ4oS7WSy'
access_token_secret='aELLPYa9ix0OaDRABK4xHehctN8RIvLudIfEJtJOZPftR'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

public_tweets=api.search('science')

for tweets in public_tweets:
	print(tweets.text)
