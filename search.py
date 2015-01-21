#!/usr/bin/python
import wikitweet
import cgi

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>TweetWiki Results</title>'
print '</head>'
print '<body>'


form = cgi.FieldStorage()
query = form.getvalue('search_bar')

#for testing purposes
print '<p>'+query+'</p>'

#query = "atlanta"

#Calls combo search - stores search results in a list
results = wikitweet.combo_search(query)

#testing
print results


for r in results:
	print '<p>'+r+'</p>'

print '<p>done</p>'
print '</body>'
print '</html>'