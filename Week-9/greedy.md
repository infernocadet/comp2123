# Greedy Algorithms

A class of algorithms where a solution is built one step at a time making locally optimal choices at each stage, hoping to find a global optimum solution.

Hard to design and analyse. Greedy algorithms can be the basis of a good hueristic $\rightarrow$ a rule of thumb that works well in practice but has no theoretical guarantees.

## Generic Form

```
def generic_greedy(input):
    # initilisation
    initialise result

    determine order in which to consider input

    # iteratively make greedy choice
    for each element i of the input do:
        if element i improves result then
            update result with element i

    return result
```

## The Fractional Knapsack Problem

Given: A set $S$ of $n$ items, with each item $i$ having:

- $b_{i}$: a positive benefit
- $w_{i}$: $: a positive weight

Goal: Choose items with maximum total benefit of weight at most $W$. Let $x_{i}$ denote the amount we take of item $i$.

Objective: maximise $\sum_{i \in S}b_{i}(x_{i}/w_{i})$ $\rightarrow$ maximise the benefit per unit weight.

Constraint: $\sum_{i \in S}x_{i} \leq W$ (total weight is bounded).

Basically, we want to take as much of the most valuable item as possible, then the next most valuable item, and so on. Make a subset of these items to fit in our backpack.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/kpsck.png" width="350" height="auto">
</p>

### Fractional Knapsack Algorithm

Initial configuration: No items chosen

Each step: Identify the "best" item available and add as much as possible to the knapsack.

What defines the "best" item? The item with the highest benefit per unit weight.

```
def fractional_knapsack(b, w, W):

    # initialisation
    x <- array of size |b| of zeros
    curr <- 0

    # iteratively make greedy choice
    while curr < W:
        i <- "best" item not yet chosen
        x[i] <- min(w[i], W - curr)
        curr <- curr + x[i]
    return x
```

### Different Strategies

A greedy choice: Keep taking as much as possible of the "best" item, where the best means:

- **highest benefit**: select items with highest benefit
- **smallest weight**: select items with smallest weight
- **benefit/weight**: select items with highest benefit to weight ratio

Each of these defines a different greedy strategy for this problem.

### Correctness of Fractional Knapsack Algorithm

Theorem: Greedy strategy of picking item with highest benefit to weight ratio computes the optimal solution.

Proof: Use an exchange arguemnt: Assume for simplicity that all rations are different $b_{i}/w_{i} \ne b_{k}/w_{k}$. Consider some feasible solution $x$ different than our one. We will prove that we can modify and improve it, eventually arriving at the greedy solution.

There must be items $i$ and $k$ such that $x_{i} < w_{i}$, $x_{k} > 0$ and $b_{i}/w_{i} > b_{k}/w_{k}$.

If we replace some $k$ with some of $i$, we get a better solution. By how much? $min(w_{i}-x_{i}, x_{k})$

We are basically saying, with item $i$ such that $x_{i} < w_{i}$ (item $i$ is not fully included in $x$), and item $k$ such that $x_{k} > 0$ (at least some of item $k$ is included in $x$), and the benefit to weight ratio of item $i$ is more than $k$, the greedy algorithm would prefer to take more of item $i$ and less of item $k$.

### Complexity of Fractional Knapsack Algorithm

Sort items by their benefit to weight values, and then process them in this order. This requires $O(n logn)$ time to sort items and then $O(n)$ $ to process.

## Task Scheduling

Given: A set $S$ of $n$ lectures, lecture $i$ starts at $s_{i}$ and finishes at $f_{i}$.

Goal: Find the minimum number of classrooms to schedules all lectures so that no two occur at the same time in the same room.

Example below uses 4 classrooms to schedule 10 lectures.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/task.png" width="350" height="auto">
</p>

We can compress this a little bit, move e and h to the first room, f and i to the second room, and j to the third. This way we only use 3 classrooms:

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/taskg.png" width="350" height="auto">
</p>

### Interval Partitioning: Lower Bound

**Definition**: The **_depth_** of a set of open intervals is the maximum number that contain any given time.

**Observation**: Number of classrooms needed $\ge$ depth. Why?

Example: Depth of schedule above is 3. (a, b, c all contain 9:30.)

### Interval Partitioning: Greedy Algorithm

Greedy algorithm: Consider lectures in increasing order of start time: assign lecture to any compatible classroom.

```
def interval_partition(S):
    # initialisation
    sort intervals in increasing starting time order
    d <- 0

    # iteratively do greedy choice
    for i in increasing starting time order do:
        if lecture i compatible with classroom k then
            schedule lecture i in classroom 1 <= k <= d
        else
            allocate a new classroom d + 1
            schedule lecture i in classroom d + 1
            d <- d + 1
        return d
```
