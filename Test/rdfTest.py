import rdflib
import pprint
import os
import ontospy

# g = rdflib.Graph()
# file = os.path.abspath("D:\Repository\RDF_Test\Files\RDFs\Delivery\Ontology resources\Linkset.rdf")
# print (file)
# test = (open(file, "r"))
#
# with open("D:\Repository\RDF_Test\Files\RDFs\Delivery\Ontology resources\Linkset.rdf") as f:
#     read_data = f.read()
#     print f
#     g.parse(f, format="xml")

#linda = rdflib.BNode()
#print linda +" GUID is"
g = rdflib.Graph()
print g.parse("D:\Repository\RDF_Test\Files\RDFs\Delivery\index.rdf")
print (len(g))

Test_ontospy.

for stmt in g:
    pprint.pprint(stmt)
    #print stmt.type()
#f.closed