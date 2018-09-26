from rdflib import Graph
import os
import sys
from rdflib.namespace import FOAF
g = Graph()
print help(sys.path)
#print os.path.abspath(self)

#print g.parse(location="Files\RDFs\latest.rdf", format="nt")
# for s,_,n in g.triples((None, FOAF['member_name'], None)):
#     g.add((s, FOAF['name'], n))