The Distance Vector algorithm is used to calculate the least-cost path between nodes within a weighted graph. Unlike Dijkstra's algorithm which assumes that each node has a complete topology of the graph, this routing algorithm operates with a more limited view: nodes are only aware of link costs to adjacent neighbours and utilises iterative processes to learn and exchange information about the rest of the graph to recursively improve their understanding of the least-cost paths.

This simulator performs the distance vector algorithm on directed or undirected graphs. It assumes that all distance vectors are sent to immediate neighbours at the same time, and thus updates are performed simultaneously.

