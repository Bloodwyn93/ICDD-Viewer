import ontospy
from ontodocs.viz.viz_html_single import HTMLVisualizer
from ontodocs.viz.viz_d3tree import *
from ontodocs.viz.viz_d3treePie import *
from ontodocs.viz.viz_d3rotatingCluster import *
from ontodocs.viz.viz_markdown import *
from ontodocs.viz.viz_sigmajs import *

g = ontospy.Ontospy("D:\Repository\RDF_Test\Files\RDFs\Delivery\Payload triples\links.rdf")

# v = D3TreeViz(g) # => instantiate the visualization object
# v = D3TreePieViz(g) # => instantiate the visualization object
# v = D3RotatingClusterViz(g)
# v = MarkdownViz(g)
v = SigmaViz(g)
v.build() # => render visualization. You can pass an 'output_path' parameter too
v.preview() # => open in browser
