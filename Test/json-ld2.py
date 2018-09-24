from __future__ import print_function
import sys
import rdflib
from rdflib import URIRef, Namespace, RDF, Graph, Literal, BNode, plugin, Variable
from optparse import OptionParser

def get_labels(graph, uri, predicate_string):

    predicate = rdflib.term.URIRef(u'http://schema.org/'+predicate_string)
    name = URIRef(u"http://schema.org/name")
    object_list = []
    for obj in graph.objects(uri, predicate):
        label = obj
        if graph.value(obj, name):
            label = graph.value(obj, name)
        object_list.append(label)
    object_labels = ('\n'.join(object_list))
    return (object_labels)

def main():

    uri = URIRef(u'http://www.worldcat.org/oclc/82671871')
    predicates_delimited = "name,creator,description,about"

    parser = OptionParser()

    parser.add_option("-u", dest="uri", help="The URI of the RDF resource", action="store")

    parser.add_option("-p", dest="predicates_delimited",
                      help="A comma-sparated list of predicates to list, e.g., names, creator,contributor,about",
                      action="store")

    (options, args) = parser.parse_args(sys.argv)

    if options.uri:

        uri = URIRef(options.uri)

    if options.predicates_delimited:

        predicates_delimited = options.predicates_delimited

    predicates = predicates_delimited.split(",")

    graph = Graph()

    graph.parse(uri)

    for predicates_string in predicates:
        print(get_labels(graph,uri,predicates_string))

if __name__ == "__main__":
    main()