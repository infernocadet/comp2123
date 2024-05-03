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

## Minimum Spanning Trees

Given a connected graph $G=(V,E)$, with real-valued edge weights $c_{e}$, an MST (minimum spanning tree) is a subset of the edges $T \subseteq E$ such that $T$ is a spanning tree who sum of edge weights is minimised. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/mst.png" width="500" height="auto">
</p>

### MST Properties

**Simplifying Assumptiong**: All edge costs $c_{e}$ are distinct.

**Cut Property**: Let $S$ be any subset of nodes, and let $e$ be the min-cost edge with exactly one endpoint in $S$. Then the MST contains $e$.
- This property is used to determine whether an edge should be included in the MST. A cut in a graph is a partition of the vertices into two non-empty disjoint subsets. The cut property states that for any cut that respects the MST (meaning no edge in the MST crosses the cut), the minimum weight edge that crosses the cut is in the MST.

**Cycle Property**: Let $C$ be any cycle, and let $f$ be the max cost edge belonging to $C$. Then the MST does not contain $f$.
- A cycle in a graph is a path that starts and ends at the same vertex and includes at least one other vertex. The cycle property states that the maximum weight edge on any cycle of the graph does not belong to the MST. This is because including the edge would create a cycle in the MST, and removing it would result in a spanning tree with a smaller total weight.

### Cycles and Cuts

**Cycle**: A set of edges of the form $a-b, b-c, c-d, \dots y-z, z-a$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/cyc.png" width="500" height="auto">
</p>

**Cutset**: A cut is a subset of nodes $S$, the corresponding cutset $D$ is the subset of edges with exactly one endpoint in $S$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/cutset.png" width="500" height="auto">
</p>

It looks like there is nothing actually in the cut, but every edge that touches the cut is in the cutset. And it only includes edges which touch the cut.

#### Cycle-Cut Intersection

**Our claim is**: A cycle and a cutset intersect in an even number of edges. 

### Proving the Cut Property

**Simplifying assumption**: All edge costs $c_{e}$ are distinct.

**Cut property**: Let $S$ be any subset of nodes, and let $e$ be the min-cost edge with exactly one endpoint in $S$. Then the MST contains $e$. (I think this basically means, we have a group of nodes, S. Then, in order to like "access" this group of nodes, we would use the lowest cost edge that connects to this group of nodes. This edge would be in the MST. Because, if it wasn't, then we would have to use a higher cost edge to access the group of nodes, which would mean the MST would have a higher cost.)

**Proof** (exchange argument): 
- Let $T*$ be the MST and suppose $e$ does not belong to $T*$.
- Adding $e$ to $T*$ creates a cycle $C$ in $T*$.
- Edge $e$ is both in the cycle $C$ and in the cutset $D$ corresponding to $S$.
- $T' = T* \cup \{e\} - \{f\}$ is a spanning tree with $c(T') < c(T*)$.
- Since $c_{e} < c_{f}, \text{cost}(T') < \text{cost}(T*)$, we have a contradiction.

## Prim's Algorithm

### Psuedocode

```
def prim(G, c):
    u <- arbitrary vertex in V
    S <- {u}
    T <- {}
    while |S| < |V|:
        (u, v) = min-cost edge with exactly one endpoint in S (u in S and v not in S)
        add (u, v) to T
        add v to S
    return T
```

### Implementation

We need to also implement how we will search for an edge, and add an edge.

The main idea is that for every $v \text{ in } V\setminus{S}$, we want to find the edge $(u,v)$ with the smallest cost such that $u \text{ in } S$. We keep:
- $d[v]$: the distance to closest neighbour in $S$
- $parent[v]$: closest neighbour in $S$

```
def prim(G, c){
    for v in V:
        d[v] = inf
        parent[v] = None
    u = arbitrary vertex in V
    d[u] = 0
    Q = new Priority Queue for {(v, d[v]): v in V}
    S = {}

    while Q is not empty:
        u = Q.remove_min()
        add u to S
        for (u, v) incident to u:
            if v not in S and c(u,v) < d[v]:
                parent[v] = u
                decrease priority d[v] to c(u,v)
    return parent
}
```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/prim1.png" width="500" height="auto">
</p>

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/prim2.png" width="500" height="auto">
</p>

### Prim's Algorithm Complexity

Similar analyssi to Dijkstra's algorithm:
- $O(mlogn)$ with a heap
- $O(m + nlogn)$ with a Fibonacci heap

## Kruskal's Algorithm - Union Find ADT

Consider edges in ascending order of weight.

**Case 1**: If adding $e$ to $T$ creates a cycle, discard $e$ according to cycle property.

**Case 2**: Otherwise, insert $e = (u,v)$ into $T$ according to cut property where $S$ is the set of nodes in $u$'s connected component.