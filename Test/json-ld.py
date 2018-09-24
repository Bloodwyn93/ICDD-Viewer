import urllib2
import rdflib
import pprint
import rdflib_jsonld

uri = 'http://www.worldcat.org/oclc/82671871'

request_headers = {'Accept': 'application/rdf+xml'}

request = urllib2.Request(uri, headers = request_headers)

response = urllib2.urlopen(request).read()

graph = rdflib.Graph()

graph.parse(data=response, format='xml')

for stmt in graph:
    pprint.pprint(stmt)

# predicate_query = graph.query("""
#                     select ?predicates
#                     where {?s ?predicates ?o}
#                     """)
#
# for row in predicate_query:
#     print ("%s" %row)

predicates = graph.predicates(subject=None, object=None)

# For each item in the predicates generator, print it out

for predicate in predicates:

    print(predicate)
