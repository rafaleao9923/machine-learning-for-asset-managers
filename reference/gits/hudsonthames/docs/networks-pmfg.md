Note

The following sources elaborates extensively on the topic:

  1. [Tumminello, Michele, et al. “A tool for filtering information in complex systems.” Proceedings of the National Academy of Sciences 102.30 (2005): 10421-10426.](https://arxiv.org/pdf/cond-mat/0501335.pdf)

  2. [Aste, Tomaso, et al. “Correlation filtering in financial time series.” Noise and Fluctuations in Econophysics and Finance. Vol. 5848. International Society for Optics and Photonics, 2005.](https://arxiv.org/pdf/physics/0508118.pdf)

# Planar Maximally Filtered Graph (PMFG)¶

Get full version of MlFinLab

  

  

  

A planar graph is a graph which can be drawn on a flat surface without the
edges crossing. The Planar Maximally Filtered Graph (PMFG) is a planar graph
where the edges connecting the most similar elements are added first
(Tumminello et al, 2005).

For example, for a correlation-based PMFG, the edges with the highest
correlation would be added first. The steps to construct the PMFG are defined
as follows:

  1. Order the edges from the highest similarity to the lowest.

  2. Add the edge with the highest similarity to the PMFG, if the resulting graph is planar

  3. Keep adding edges from the ordered list, until \\(3 (n - 2)\\) edges have been added.

The PMFG retains the Minimum Spanning Tree (MST) as a subgraph, thus retains
more information about the network than a MST (Tumminello et al, 2005).

![../_images/pmfg_dash_ui.png](../_images/pmfg_dash_ui.png)

PMFG example user interface.¶

PMFG contains \\(3 (n - 2)\\) edges as opposed to the MST, which contains \\(n
- 1\\) edges for \\(n\\) number of nodes in the network.

* * *

## PMFG¶

### Background on Topology and Graph Theory¶

PMFG is the specific case where the graph is planar on genus \\(k = 0\\),
which means the graph can be drawn on a flat surface without the edges
crossing. However, the greater the genus, the greater the information stored
in the graph. However, Tumminello et al (2005) state “major relative
improvement” when the simplest graph is created of genus \\(k = 0\\), instead
of for higher genus.

The figure shows three different shapes with different genera. A sphere in 2
dimensions is of genus \\(k = 0\\) (much like the PMFG). The torus is of genus
\\(k =1\\) and the double torus of genus \\(k = 2\\) and so on. A coffee cup
with a handle, would have the same topology as a torus.

[![../_images/Topological-genera.png](../_images/Topological-
genera.png)](../_images/Topological-genera.png)

Topological genera. From the left: Genus 0 (sphere), Genus 1 (torus), Genus 2
(double torus) (Warne, 2013).¶

The PMFG “is a topological triangulation of the sphere” (Tumminello et al,
2005).

[![../_images/sphere_triangulation.png](../_images/sphere_triangulation.png)](../_images/sphere_triangulation.png)

Example of a topological triangulation of a sphere (Renka, 1984).¶

**Planar Graph Theory**

According to Kuratowski’s theorem on planar graphs, a planar graph cannot
contain a 5 clique (see \\(k_{5}\\) graph), nor can it contain a \\(k_{3,3}\\)
bipartite graph where each node connects to every other node in the other
group (see \\(k_{3,3}\\) graph) (Grünbaum and Bose, 2013).

[![../_images/Kuratowski-theorem.png](../_images/Kuratowski-
theorem.png)](../_images/Kuratowski-theorem.png)

Graph a) shows a 5 clique graph (\\(k_{5}\\)) and b) shows \\(k_{3,3}\\)
bipartite graph (Staniec and Debita, 2012).¶

Only 3 cliques and 4 cliques are allowed in the PMFG. Cliques of higher orders
are allowed if the genus is greater. For example, 5 cliques would be allowed
in genus \\(k = 1\\). Analysing 3-cliques and 4-cliques can show the
underlying hierarchical structure of the network and “have important and
significant relations with the market structure and properties” (Aste et al,
2005).

[![../_images/3_cliques_4_cliques.png](../_images/3_cliques_4_cliques.png)](../_images/3_cliques_4_cliques.png)

An example of a 3 clique graph and a 4 clique graph.¶

Where \\(k\\) is the genus, and \\(r\\) is the number of elements, the number
of elements allowed in a clique is given by Ringel (2012) as:

\\[r ≤ \frac{7+\sqrt{1+48k}}{2}\\]

For example, for a graph of genus \\(k = 1\\), 5 cliques are allowed in the
graph.

### Analysing Cliques in PMFG¶

Analysis of 3-cliques and 4-cliques, describe the underlying hierarchical
structure of the network and “have important and significant relations with
the market structure and properties” (Aste et al, 2005). In the case of
interest rates, the 4 cliques group together the rates with similar maturity
dates (Aste et al, 2005). For stocks, 4-cliques tend to group with similar
industry or sector groups (Tumminello et al, 2005). Therefore, 3-cliques and
4-cliques can be useful to analyse and understand the network.

Tumminello et al (2005) proposes a measure of disparity \\(y_{i}\\) defined as
follows:

\\[y_{i} = \sum_{j ≠i, j ∈clique} [\frac{p_{ij}}{s_{i}}]^2\\]

The mean value of the disparity measure is the sum of \\(y_{i}\\) divided by
the number of nodes in the clique. The strength of an element \\(s_{i}\\) is
calculated by:

\\[s_{i} = \sum_{j ≠i, j ∈clique} p_{ij}\\]

The disparity measure is only meaningful if all of the edges in the clique
have a correlation value of 0 or greater, which is why some disparity measure
values may be excessively large.

[![../_images/cliques_pmfg.png](../_images/cliques_pmfg.png)](../_images/cliques_pmfg.png)

PMFG 34 US interest rates, with 4 cliques highlighted (Aste et al, 2005).¶

Aste et al (2005) found that the groups of 4-cliques “reveal the hierarchical
organization of the underlying system… grouping together the interest rates
with similar maturity dates”. The figure above is an example of how the
cliques form according to the maturity dates.

The average disparity measure for all 3 cliques and 4 cliques are shown in the
PMFG interface under the statistic name disparity_measure.

* * *

## Creating the PMFG¶

You can create the PMFG visualisation using generate_pmfg_server. This
requires you to input a log returns dataframe.

[![Code example
demo](../_images/example_medium8.png)](../_images/example_medium8.png)

Note

Log returns dataframe should be calculated as \\(log P_{i}(t) - log
P_{i}(t-1)\\) for asset \\(i\\) and price \\(P\\).

### Implementation¶

Here are the options you can use for the generate_pmfg_server:

[![Code implementation
demo](../_images/implementation_medium11.png)](../_images/implementation_medium11.png)

Specifying “correlation” instead of the default “distance”, the PMFG algorithm
orders the edges from largest to smallest edge instead of the other way round.
The optional format for the colours and sizes, can be specified in the
following manner:

[![Code example
demo](../_images/example_medium8.png)](../_images/example_medium8.png)

[![../_images/sizes_colours_no_toast.png](../_images/sizes_colours_no_toast.png)](../_images/sizes_colours_no_toast.png)

The MST edges, contained within the PMFG, are displayed in green.

* * *

## Custom Input Matrix PMFG¶

As is the case for MST and ALMST, to input a custom matrix, you must create a
PMFG class directly. This gives you the option to transform the input
dataframe directly, instead of a log returns dataframe, allowing you to make
specific transformations instead of the default way to create “correlation” or
“distance” matrix. However, PMFG only allows input_type of “correlation” or
“distance” to specify whether the PMFG algorithm should add the edges from
largest to smallest or smallest to largest respectively.

[![Code example
demo](../_images/example_big8.png)](../_images/example_big8.png)

Once the PMFG class object has been created, you can set the colours and sizes
properties of the graph.

### Adding Colours to Nodes¶

[![../_images/pmfg_colours_new.png](../_images/pmfg_colours_new.png)](../_images/pmfg_colours_new.png)

The colours can be added by passing a dictionary of group name to list of node
names corresponding to the nodes input. You then pass the dictionary to the
set_node_groups method.

[![Code example
demo](../_images/example_small5.png)](../_images/example_small5.png)

### Adding Sizes to Nodes¶

[![../_images/sizes_colours_pmfg.png](../_images/sizes_colours_pmfg.png)](../_images/sizes_colours_pmfg.png)

The sizes can be added in a similar manner, via a list of numbers which
correspond to the node indexes. The UI of the graph will then display the
nodes indicating the different sizes.

[![Code example
demo](../_images/example_small5.png)](../_images/example_small5.png)

The PMFG object, once constructed, serves as the input to the PMFGDash class.
To run the PMFGDash within the Jupyter notebook, make sure to pass in the
parameter.

[![Code example
demo](../_images/example_small5.png)](../_images/example_small5.png)

Where calling get_server will return the Dash server with the frontend
components. Then you can call:

[![Code example
demo](../_images/example_small5.png)](../_images/example_small5.png)

Which is the default option, or alternatively for Jupyter dash, specify the
mode as ‘inline’, ‘external’ or ‘jupyterlab’. The ‘external’ mode is very
useful for larger graphs, as you can view the PMFG in a new window.

[![Code example
demo](../_images/example_small5.png)](../_images/example_small5.png)

[![../_images/jupyter_inline_dash.png](../_images/jupyter_inline_dash.png)](../_images/jupyter_inline_dash.png)

* * *

## PMFG Class¶

[![Code implementation
demo](../_images/implementation_big7.png)](../_images/implementation_big7.png)

* * *

## PMFGDash Class¶

[![Code implementation
demo](../_images/implementation_big7.png)](../_images/implementation_big7.png)

* * *

## Research Notebook¶

The following notebook provides a more detailed exploration of the PMFG
creation.

[![Notebook demo](../_images/notebook11.png)](../_images/notebook11.png)

* * *

## Research Article¶

Read our article on the topic

  

* * *

## Presentation Slides¶

  

* * *

## References¶

  * [Tumminello, M., Aste, T., Di Matteo, T. and Mantegna, R.N., 2005. A tool for filtering information in complex systems. Proceedings of the National Academy of Sciences, 102(30), pp.10421-10426.](https://arxiv.org/pdf/cond-mat/0501335.pdf)

  * [Grünbaum, B., & Bose, R. (2013, August 14). Applications of graph theory. Retrieved September 16, 2020, from](https://www.britannica.com/science/combinatorics/Applications-of-graph-theory)

  * [Ringel, Gerhard. Map color theorem. Vol. 209. Springer Science & Business Media, 2012.](https://www.springer.com/gp/book/9783642657610)

  * [Aste, Tomaso, et al. “Correlation filtering in financial time series.” Noise and Fluctuations in Econophysics and Finance. Vol. 5848. International Society for Optics and Photonics, 2005.](https://arxiv.org/pdf/physics/0508118.pdf)

  * [Renka, R.J., 1984. Interpolation of data on the surface of a sphere. ACM Transactions on Mathematical Software (TOMS), 10(4), pp.417-436.](https://dl.acm.org/doi/10.1145/2701.356107)

  * [Warne, D., 2013. On the effect of topology on cellular automata rule spaces.](https://eprints.qut.edu.au/76202/4/76202_Accepted.pdf)

  * [Staniec, K. and Debita, G., 2012. Evaluation of topological planarity and reliability for interference reduction in radio sensor networks. EURASIP Journal on Wireless Communications and Networking, 2012(1), p.56.](https://jwcn-eurasipjournals.springeropen.com/articles/10.1186/1687-1499-2012-56)

