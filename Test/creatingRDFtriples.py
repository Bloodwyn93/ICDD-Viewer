from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import RDF, FOAF
import pprint
import rdflib_jsonld
import urllib2

bob = URIRef("http://example.org/people/Bob")
linda = BNode()

name = Literal("Bob")
age = Literal(24)
height = Literal(78.5)

n = Namespace("http://example.org/people/")
# print n.bob
# print n.eve
RDF.type
FOAF.knows

g = Graph()

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.knows, linda))
g.add((bob, FOAF.age, Literal(42)))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal("Linda")))

# print g.serialize(format="turtle")
# print "Bob is", g.value(bob, FOAF.age)
#
# g.set((bob, FOAF.age, Literal(43)))
# print "Bob is now", g.value(bob, FOAF.age)

if (bob, None, None) in g:
   print "This graph contains triples about Bob!"
