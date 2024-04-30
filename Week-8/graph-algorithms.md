# Graph Algorithms

## Weighted Graphs

In a weighted graph, each edge has an associated numerical value, called the weight of the edge. Edge weights may represent distances, costs, or any other quantity that you want to associate with the edge.

E.g.: In a flight route graph, the weight of an edge represents the distance between the endpoint airports.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/ap.png" width="500" height="auto">
</p>

## Shortest Paths

Given an edge weighted graph, and two vertices `u` and `v`, we want to find a path of minimum total weight between `u` and `v`, where the weight of a path is the sum of the weights of its edges.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/hon.png" width="500" height="auto">
</p>

### Shortest Path Properties

**Property**: A subpath of a shortest path, is itself a shortest path.

For example, the shortest path from PVD to HNL also contains the shortest path from PVD to LAX, in the photo above.

**Property**: There is a tree of shortest paths from a start vertex to all other vertices (shortest path tree).

For example, the shortest path tree from PVD to all other vertices.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/spt.png" width="500" height="auto">
</p>

## Djikstra's Algorithm

Input:
- Graph $G = (V, E)$
- Edge weights $w : E \rightarrow R_{+}$
- Start vertex $s$

Output:
- Distance from $s$ to all $v$ in $V$
- Shortest path tree rooted at $s$

Assumptions:
- $G$ is connected and undirected
- Edge weights are non-negative

High level idea:
- Maintain a distance estimate
  - $D[v] \ge dist_{w}(s,v)$ for all $v \in V$
- Keep track of a subset $S$ of $V$ s.t.
  - $D[v] = dist_{w}(s,v)$ for all $v \in S$

Initially:
- $D[s] = 0$
- $D[v] = \infty$ for all $v \in V\setminus{s}$