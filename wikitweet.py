#!/usr/bin/python
import wiki
#import twit

print "Content-type:text/html\r\n\r\n"

#This function combines the results from wikipedia and twitter and sorts them then returns the list
def combo_search(query):
	#calls search from wiki.py - returns search object
	wiki_list = wiki.wiki_search_list(query)

	#calls search from twit.py - returns list of tweets
	#tweet_list = twit.tweet_search(query)

	#Add wikipedia and twitter results to final list.
	final_list = wiki_list
	#final_list.extend(tweet_list)

	final_list.sort()

	return final_list