import sys
import wikitweet

raw_arg = sys.argv

#Pops off name of python prorgram from arguments
raw_arg.pop(0)

#Concatenates argument list to a string
query = ""
for i in raw_arg:
	query = query + " " + i

#Removes first space
query.strip()

#Calls combo search - stores search results in a list
results = wikitweet.combo_search(query)

for r in results:
	print r

