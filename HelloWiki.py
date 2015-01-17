import urllib2
import json

max_results = 10
action = 'opensearch'
format = 'json'
url = 'http://en.wikipedia.org//w/api.php?action='+action+'&format='+format+'&limit='+str(max_results)+'&search='


user_search = raw_input("Search Wiki")

search_url = url

#Create the url for the search query
final_url = search_url + user_search.replace(' ', '%20')

#Create json object for the results on the query page
json_obj = urllib2.urlopen(final_url)

#Returns the JSON string as a python data structure (a list containing 3 lists (Page Title, Description, URL)
json_data = json.load(json_obj)

#Stores inner list of titles, descriptions, and urls in a results dictionary
results = {'title': json_data[1], 'description:': json_data[2], 'url':json_data[3]}

for result in results['title']:
	print result

