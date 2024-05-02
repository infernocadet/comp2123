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
  - This should be greater or equal to the true distance from s to v.
- Keep track of a subset $S$ of $V$ s.t.
  - $D[v] = dist_{w}(s,v)$ for all $v \in S$

Initially:
- $D[s] = 0$
- $D[v] = \infty$ for all $v \in V\ussetmin{s}$

In each iteration we:
- add to $S$, vertex $u \in V\setminus{S}$ with smallest $D[u]$
- update $D$-values for vertices adjacent to $u$.

### Edge Relaxation

This basically refers to updating the distance estimate of a vertex $v$ based on the distance estimate of another vertex $u$ and the weight of the edge $(u,v)$.

Consider edge $e=(u,z)$ such that:
- $u$ is the last vertex added to $S$
- $z$ is not in $S$

The relaxation of edge $(u,z)$ updates $D[z]$ as follows:
- $D[z] \leftarrow min{D[z], D[u] + w(u,z)}$

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/dal.png" width="500" height="auto">
</p>

### Dijkstra's Algorithm Pseudocode

```
def Dijkstra(G, w, s):

    # initialise algorithm
    for v in V do:
        D[v] = inf
        parent[v] = None
    D[s] = 0
    Q = new Priority Queue for {(v, D[v]): v in V}

    # iterative add vertices to S
    while Q is not empty:
        u = Q.remove_min()
        for z in G.neighbours(u):
            if D[u] + w[u, z] < D[z]:
                D[z] = D[u] + w[u, z]
                Q.update_priority(z, D[z])
                parent[z] = u
    return D, parent
```

Marc's Explanation:
- **Initialisation**: First, set the distance $D[v]$ to infinity for all verticies $v$, except for the start vertex $s$, which is set to 0. This preparation also includes setting all parent pointers to `None` for reconstructing the path later.
- **Priority Queue**: A priority queue $Q$ is used to efficiently fetch the next vertex with the smallest distance. Initially it includes all vertices with their respective distances.
- **Iterative Processing**: The algorithm continuously removes the vertex $u$ with the smallest distance from $Q$. It then checks each of $u$'s neighbours $z$. If the path through $u$ offers a shorter path to $z$ than preivously known and stored, it updates $D[z]$ to the new lower distance, and updates the queue and $z$'s parent to $u$ (note: we update the parent because we are making the shortest path, which is now through $u$).
- **Result**: The process repeats until the queue is empty, ensuring the shortest paths from $s$ to all vertices are found and can be reconstructed using the parent pointers. 

### Dijkstra's Algorithm Complexity Analysis except PQ operations

Given the following pseudocode:

```
def Dijkstra(G, w, s):

    # initialise algorithm
    for v in V do:
        D[v] = inf
        parent[v] = None
    D[s] = 0
    Q = new Priority Queue for {(v, D[v]): v in V}

    # iterative add vertices to S
    while Q is not empty:
        u = Q.remove_min()
        for z in G.neighbours(u):
            if D[u] + w[u, z] < D[z]:
                D[z] = D[u] + w[u, z]
                Q.update_priority(z, D[z])
                parent[z] = u
    return D, parent
```

Initialisation takes $O(n)$ time, where $n$ is the number of vertices in the graph. We are making an array which holds the distance to each vertex, and an array which holds the parent of each vertex, which takes up $O(n)$ space.

The iterative process of updating the distances of each neighbour of a vertex takes $O(deg(u))$ time, for each $u in V$ plus `update_priority` work. AS we know, $deg(u)$ is simply $O(m)$, where $m$ is the number of edges in the graph.

This means that the total running time of Dijkstra's is $O(n+m)$.

Assuming the graph is connected (so $m \ge n-1$), the algorithm spends $O(m)$ time on everything except for the PQ operations.

Priority queue operation counts:
- `insert`: $n$
- `decrease_key`: $m$
- `remove_min`: $n$

Using a heap for PQ, Dijkstra's algorithm runs in $O(mlogn)$ time.

The Fibonacci heap is a PQ that can carry out decrease key in $O(1)$ amortized time. Using that instead, we get $O(m + nlogn)$ time.

`decrease_key` just means `update_priority`, when we update the next closest nodes after edge relaxation.

### Dijkstra's Algorithm Correctness

**Invariant**: For each $s \in S = V\setminus{Q}$, we have $D[u] = dist_{w}(s,u)$.

**Proof** *(by induction on $|S|$)*:
- Base case: $|S| = 1$ is trivial since $D[s] = 0$
- Inductive hypothesis: Assume true for $|S| = k \ge 1$
  - Let $v$ be the next node added to $S$ and $u=\text{parent}[v]$
  - The shortest $s-u$ path plus $(u, v)$ is an $s-v$ path of length $D[v]$.
  - Consider any $s-v$ path $P$. We will see it is no shorter than $D[v]$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/dac.png" width="500" height="auto">
</p>

  - Let $x-y$ be the first edge in $P$ that leaves $S$, and let $P'$ be the subpath to $x$.
  - $P$ is already too long as soon as it leaves $S$:

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/expl.png" width="500" height="auto">
</p>

#### Negative-weight edges

Dijkstra's may not work for negative-weight edges, Where even if $D[v]$ is the smallest label, it may be that $dist_{w}(s,v) < D[v]$ if $w(P'') < 0$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/new.png" width="500" height="auto">
</p>

