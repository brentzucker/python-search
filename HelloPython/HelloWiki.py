import urllib2
import json

max_results = 10
action = 'opensearch'
format = 'json'
url = 'http://en.wikipedia.org//w/api.php?action='+action+'&format='+format+'&limit='+str(max_results)+'&search='

#Function returns a dictionary of results {title, description, url}
def wiki_search(query):
	search_url = url

	#Create the url for the search query
	final_url = search_url + query.replace(' ', '%20')

	#Create json object for the results on the query page
	json_obj = urllib2.urlopen(final_url)

	#Returns the JSON string as a python data structure (a list containing 3 lists (Page Title, Description, URL)
	json_data = json.load(json_obj)

	#return_object is a list of dictionaries. each dictionary corresponds to a search result
	return_object = []
	for t,d,u in zip(json_data[1], json_data[2], json_data[3]):
		return_object.append({'title': t, 'description': d, 'url': u})

	#return list of dictionaries
	return return_object

#Prompts user for a search term
user_search = raw_input("Search Wiki")

#Stores results dictionary in user_results
user_results = wiki_search(user_search)

#Prints Search results 
for result in user_results:
	print result['title'] +": "+ result['description']
