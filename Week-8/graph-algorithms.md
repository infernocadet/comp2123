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

Property: A subpath of a shortest path, is itself a shortest path.

For example, the shortest path from PVD to HNL also contains the shortest path from PVD to LAX, in the photo above.

