# Graphs

A graph ```G``` is a pair ```(V,E)``` where

- ```V``` is a set of nodes, called **vertices**
- ```E``` is a collection of pairs of vertices, called **edges**

Example:

- A vertex represents an airport, and stores the three-letter airport code
- An edge represents a flight route between two airports and stores the mileage of the route

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/ve.png" width="500" height="auto">
</p>

## Edge Types

**Directed edge**:

- ordered pair of vertices ```(u, v)```
- ```u``` is the origin/tail
- ```v``` is the destination/head
- e.g., a flight

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/de.png" width="500" height="auto">
</p>

**Undirected edge**:

- unorded pair of vertices ```(u, v)```
- e.g., a two-way road

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/ue.png" width="500" height="auto">
</p>

### Applications

Electronic circuits:

- printed circuit board
- intergrated circuit

Transportation networks:

- highway network
- flight network

Computer networks

- Internet
- Web

Modelling

- Entity relationship diagram
- Gantt precedence constraints

## Graph Concept: Paths

A **path** is a sequence of vertices such that every pair of consecutive vertices is connected by an edge.

A simple path is one where all vertices are distinct. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/path.png" width="500" height="auto">
</p>

Examples:

- (V, X, Z) is a simple path
- (U, W, X, Y, W, V) is a path that is not simple

A simple path from s to t is also called an s-t path.

### Terminology (Undirected graphs)

Consider the following graph:

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/ugterm.png" width="500" height="auto">
</p>

- Edges connect **endpoints**
  - e.g., W and Y for edge f
- Edges are **incident** on endpoints
  - e.g., a, d, and b are incident on V
- **Adjacent** vertices are connected
  - e.g., U and V are adjacent
- **Degree** is number of edges on a vertex
  - e.g., X has degree 5
- **Parallel edges** share same endpoints
  - e.g., h and i are parallel
- **Self-loop** have only one endpoint
  - e.g., j is a self loop
- **Simple graphs** have no parallel or self loops

### Terminology (Directed graphs)

Consider the following graph:

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/dgterm.png" width="500" height="auto">
</p>

- Edges go from **tail** to **head**
  - e.g., W is the tail of c and U its head
- **Out-degree** is the number of edges out of a vertex
  - e.g., W has out-degree of 2
- **In-degree** is the number of edges into a vertex
  - e.g., W has in-degree of 1
- **Parallel edges** share tail and head
  - None in this graph
- **Self-loop** have same head and tail
  - e.g., X has a self-loop
- Simple directed graphs have no parallel or self-loops, but are allowed to have anti-parallel loops
  - f and a are anti-parallel

## Graph Concept: Cycles

A **cycle** is defined by a path that starts and ends at the same vertex.

A **simple cycle** is one where all vertices are distinct.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/cycle.png" width="500" height="auto">
</p>

Examples:

- (V,X, Y, W, U V) is a simple cycle
- (U, W, X, Y, W, V, U) is a cycle (not simple)

An **acyclic graph** has no cycles.

## Graph Concept: Subgraphs

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/subgraph.png" width="500" height="auto">
</p>

Let $G=(V,E)$ be a graph. We say $S=(U,F)$ is a subgraph of $G$ if $U \subseteq V$ and $F \subseteq E$.

A subset $U \subseteq V$ induces a graph $G[U] = (U, E[U])$ where $E[U]$ are the edges in $E$ with endpoints in $U$.

A subset $F \subseteq E$ induces a graph $G[F] = (V[F], F)$ where $V[F]$ are the endpoints of edges in $F$.

## Graph Concept: Connectivity

A graph $G=(V,E)$ is connected if there is a path between every pair of vertices in $V$

A connected component of a graph $G$ is a maximal connected subgraph of $G$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/conn.png" width="500" height="auto">
</p>

## Graph Concept: Trees and Forests

An unrooted tree $T$ is a graph such that

- $T$ is connected
- $T$ has no cycles

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/gtree.png" width="500" height="auto">
</p>

A forest is a graph without cycles, and its connected components are trees.

Every tree on $n$ vertices has $n-1$ edges.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/forest.png" width="500" height="auto">
</p>

### Spaning Trees and Forests

A spanning tree is a connected subgraph on the same vertex set. A spanning tree is not unique unless the graph is a tree.

Spanning trees have applications to the design of communication networks. A spanning forest of a graph is a spanning subgraph that is a forest.

## Graph Properties

$$\sum_{v \text{ in } V}deg(v) = 2m$$

$$\text{and, in a simple undirected graph:}$$

$$m \le \frac{n(n-1)}{2}$$

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/gprop.png" width="auto" height="auto">
</p>

## Graph ADT

We model the abstraction as a combination of three data types, ```Vertex```, ```Edge``` and ```Graph```.

A ```Vertex``` stores and associated object (e.g., airport code) that is retrieved with a ```getElement()``` method.

An ```Edge``` stored an associated object (such as a flight number, travel distance) that is also retrieved with ```getElement()```.

### Directed Graph ADT

There is a large number of different functions for the Directed Graph ADT.

- ```numVertices()```
  - returns the number of vertices in a graph
- ```vertices()```
  - returns an iterable of all the vertices in the graph
- ```numEdges()```
  - returns the number of edges of the graph
- ```edges()```
  - returns an iterable of all edges in the graph
- ```getEdge(u, v)```
  - returns the edge from vertex u to vertex v. if none exists return null. for an undirected graph, there is no difference between ```getEdge(u, v)``` and ```getEdge(v, u)```
- ```endVertices(e)```
  - returns an array containing the two endpoint vertices of the edge e. if the graph is directed, the first vertex is the origin and the second is the destination.
- ```opposite(v, e)```
  - for edge e incident to vertex v, returns the other vertex of the edge.
- ```outDegree(v)```
  - returns the number of outgoing edges from vertex v
- ```inDegree(v)```
  - returns the number of incoming edges to vertex v. for an undirected graph, this returns the same value as does ```outDegree(v)```.

> :warning: for an **undirected graph**, ```outDegree()``` and ```inDegree()``` is just ```degree(v)```