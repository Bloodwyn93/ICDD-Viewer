from rdflib import Graph
from rdflib.namespace import FOAF
g = Graph()
print g.parse(location="D:\Repository\RDF_Test\Files\RDFs\latest.rdf", format="nt")
# for s,_,n in g.triples((None, FOAF['member_name'], None)):
#     g.add((s, FOAF['name'], n))