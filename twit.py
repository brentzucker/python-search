#!/usr/bin/python
import tweepy

print "Content-type:text/html\r\n\r\n"

#returns tweets that match sepcified query 

#Authentication details
consumer_key = 'CZqpg8KRh3Y7aWCXf9tj6N9D3'
consumer_secret = 'fOkmAxKf7QcIHnUDzN5CPgvPONtqVpDfbtdL5YGab37BQGfmoP'
access_token = '17464727-cD9R5EdeBteo55MDq2wW0E1eUlXv3FzhswpZ0uMrx'
access_token_secret = '1vsT3ceCiCDMSAiZHpn2bJsRTRALJdFHukZcgok8oaVuq'

#Create authenication token using our details
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Get API handler
api = tweepy.API(auth)

#Loops through search_results printing each element
#for tweet in search_results:
#	print tweet.text

def tweet_search(query):
	#Stores search results in list
	search_results = api.search(query)

	results = []
	for result in search_results:
		results.append(result.text)

	return results