# Assignment 1
*COMP2123 - 510435765*

## ADVICE
- When designing a DSA:
1. briefly describe general idea
2. develop and elaborate

- Use lecture or textbook for proof

- Prove/explain/motivate answers

- When giving an algorithm, algorithm does not have to be given as psuedo-code or code.

- If you provide psuedo-code or code, then explain code and ideas in plain english.

- Always talk from worst-case analysis

- We are interested in the most efficient DSA

### Problem 1 (10 points)

Consider the following snippet of pseudocode that takes an array of $n$ integers. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/prob1.png" width="auto" height="auto">
</p>

Your task is to:

*a) upperbound the running time of the algorithm in terms of* $n$ *using* $O$*-notation.*

The bulk of this algorithm comprises of a nested for loop. The outer loop uses a pointer $i$ which runs from $0$ to $n-1$ where $n$ is the length of the array. The inner loop uses a pointer $j$ which runs from $i+1$ to $n-1$. Hence the inner loop runs $n-i-1$ times for each iteration of the outer loop.

The worst-case scenario is when we have to process through the full size of the array, i.e. $n$ times.

We can sum the series of how many times the inner loop runs by calculating the series of how many times ```line 5``` runs for each value of $i$ in ```line 4```. This gives us:

$$\sum_{i=0}^{n-1} (n-i-1) = \sum_{i=0}^{n-1} (n-1) - \sum_{i=0}^{n-1} (i)$$

$$= n(n-1) - \frac{(n-1)n}{2}$$

$$= \frac{n(n-1)}{2}$$

$$=O(\frac{1}{2}n^{2} + \frac{1}{2}n)$$

Considering lines 2, 3, 6, 7 and 8 all run in $O(1)$ time *(as comparisons and assignments are in constant time)*, we can drop them and take the most significant order of $n$, hence this algorithm runs in $O(n^2)$ in the worst-case scenario.

*b) lowerbound the running time of the algorithm in terms of* $n$ *using* $\Omega$ *notation.*

Assume for simplicity that $n$ is even. To lowerbound the running time, we consider only the last $n/2$ integers of the array. Since this is part of the full execution, analysing this part gives us a lower bound on the total running time. This gives us:

$$\sum_{i=\frac{n}{2} + 1}^{n-1} (n-i-1) = \sum_{i=\frac{n}{2} + 1}^{n-1} (n-1) - \sum_{i=\frac{n}{2} + 1}^{n-1} (i)$$

Using the arithmetic series:

$$=\frac{n}{4}(2n-2) - \frac{n}{4}(\frac{n}{2} + n)$$

$$=\frac{n^2-2n}{2} - \frac{n^2+2n}{8}$$

$$=\frac{3n^2-10n}{8}$$

Although the number of iterations are reduced in this modified algorithm, the growth rate of the number of operations with respect to $n$ is still quadratic.

This gives us a lowerbound of $\Omega(n^2)$.

### Problem 2 (25 points)

Consider a stack where each element stores an integer value. We want to extend the stack ADT we saw in the lectures with the additional operations listed below. The operations should run in O(1) time and the running time of the other stack operations should remain the same as those of a regular stack:

```Count()``` returns the number of items on the stack

```Sum()``` returns the sum of all elements on the stack

```Average()``` returns the average of all the elements on the stack

*For each operation, describe their implementation in English, argue the correctness and the running time.*

#### Standard ```push()``` and ```pop()``` operations

We can add two attributes to our Stack ADT Class, ```self_size``` and ```self_sum```.

In our insertion methods, every time we ```insert()``` or ```append()``` an element $E$, we increment ```self_size``` by $1$ and add the value of $E$ to ```self_sum```. 

```python
def newpush(self, e) -> None:
    self.push(e)
    self._size += 1
    self._sum += e
```

In our deletion methods, every time we ```delete()``` or ```pop()``` an element, say $Q$, we decrement ```self_size``` by $1$ and decrease ```self_sum``` by the value of $Q$.

```python
def newpop(self) -> int:
    if self.is_Empty(): #checks if stack is empty
        return None
    e = self.pop()
    self._size -= 1
    self._sum -= e
    return e
```

These functions both maintain a running time of $O(1)$. The ```newpush()``` function is modified to increment ```self._size``` by 1 ($O(1)$ time) and and increment ```self_sum``` by ```e``` ($O(1)$ time), so our ```push()``` still takes $O(1)$ time. The ```newpop()``` function checks if the stack is empty ($O(1)$ time), else it will pop the topmost value and assign it to ```e``` ($O(1)$ time), and decrement the ```self._size``` by 1 ($O(1)$ time) and decrement ```self_sum``` by ```e``` ($O(1)$ time), so our ```pop()``` still takes $O(1)$ time.

These new functions however do take up minimally more **constant space** $O(1)$ as only two additional integer variables are added regardless of the size of the stack.

#### Auxilliary Functions: ```count()```, ```sum()``` & ```average()```

Our ```count()``` function will return the size of the stack. 

**Time complexity**: This operation runs in $O(1)$ time as it only returns a pre-computed value.
**Correctness**: This operation returns the value of ```_size``` which is incremented or decremented every time an integer is pushed or popped in and out of the stack, respectfully. The invariant ```_size```: count of integers is always accurate.
```python
def count():
    return self._size
```

Our ```sum()``` function will return the sum of the stack, which is changed every time an ```Integer``` is inserted or removed from the stack, by the value of the ```Integer```. 

**Time complexity**: This operation runs in $O(1)$ time as it only returns a pre-computed value.
**Correctness**: This operation returns the value of ```_sum``` which is increased or decreased by the value of the Integer being pushed or popped in and out of the stack, respectfully. The invariant ```_sum``` will always track the summed values of all Integers in the stack, hence the sum of integers is always accurate.
```python
def sum():
    return self._sum
```

Our ```average()``` function will simply return the sum of the stack, divided by number of ```Integers``` in the stack. 

**Time complexity**: This operation runs in $O(1)$ time as it only returns the quotient of two stored values.
**Correctness**: This operations calculates the average based on ```_sum``` and ```_size``` which are both kept up to date with each push or pop operation. This calculation is based on the mathematical definition of the average, and the sum and size are always maintained accurately. It also checks to see if the list is empty to avoid runtime errors. Hence the calculated average sum is always accurate.
```python
def average():
    if self._size == 0:
        return 0
    return self._sum / self._size
```

### Problem 3 (25 points)

As input we are given a *sorted* array $B$ containing $n$ positive integers, together with an integer $m$. The aim is to compute how many indices $i$ and $j$ (with $i < j$) there are such that the sum of the $i\text{th}$ and the $j\text{th}$ element of $B$ is at least $m$, i.e., $A[i] + A[j] >= m$. For full marks, your algorithm needs to run in $O(n)$ time.

Example:
$B = [1, 4, 4, 6], m = 7 → \text{ return } 4$

*a) Design an algorithm that solves the problem.*

```python
def number_of_indices(B, m):
    n = len(B) 
    count = 0 
    i = 0 
    j = n - 1
    while i < j:
        if B[i] + B[j] >= m: 
            count += (j - i) 
            j -= 1 
        else:
            i += 1 
    return count
```

The algorithm number ```number_of_indices(array B, integer m)``` takes advantage of the properties of the sorted list stored in $B$. Two pointers, $i$ and $j$ sum up two values, starting from the start (index $0$) and end (index $n-1$) of the list. We iterate through the array:
- if $B[i]$ + $B[j] >= m$: then these two values add up to at least $m$. Hence this pair, $(i, j)$ satisfy our condition, and we can add this pair of indices to our counter. But, because the list is sorted, this also means that, for every $i < i' < j$, the pair $(i', j)$ is also valid, and will sum to a value greater than $m$, so we add these pairs too. Hence we increment our counter by the unique pairs of indices $(i', j)$ where $i <= i' < j$. which is $j-i$ indices. Then, to avoid double counting pairs with $j$, we decrement $j$ by $1$ to see if any smaller values of $j$ can add up with other values in the list to sum to equal or greater than $m$.
- if $B[i]$ + $B[j] \text{ NOT} >= m \text{, i.e., }B[i]$ + $B[j] < m$: then these two values do not add up to at least $m$. We leave the pair counter alone and increment the $i$ pointer up to continue our analysis with a larger value.
- the loop ends when $i = j$, as we have now checked every possible pair in our list.

Example:

```python
B = [1, 2, 4, 5]
m = 7

n = 4
count = 0
i, j = 1, n - 1 # j = 3

# first iteration
B[0] + B[3] = 1 + 5 = 6
# B[i] + B[j] < m in this case, increment i by 1
i += 1 # i = 1
B[1] + B[3] = 2 + 5 = 7
# B[i] + B[j] >= m: add all indices between 1 and 3 inclusive to our counter (2, 5) & (4,5)
count += 3 - 1 = 2
j -= 1 # decrement j pointer
B[1] + B[2] = 2 + 4 = 6
# B[i] + B[j] < m in this case, increment i by 1
i += 1 # i = 2
# our while loop condition is now not True, we break out of the loop and return count.
```

*b) Argue the correctness of your algorithm.*

We can use loop invariants to argue the correctness of the two-pointer algorithm. A loop invariant is a condition which holds true before and after each iteration of the loop.

We want to check that, before and after each iteration of the loop:
1. All pairs $(i', j')$, where $0 <= i' < i$ and $j < j' <= len(B) - 1$ have been considered, and that if those pairs summed to a value greater than or equal to $m$, that they have been counted.
2. If $B[i] + B[j] >= m$, then $B[i'] + B[j]$ for $i'$ where $i <= i' < j$ will also be greater than $m$, as $B$ is sorted in non-decreasing order, and thus $B[i'] >= B[i]$. Hence all pairs $(i', j)$, where $i < i' < j$ would also have a sum greater than or equal to $m$, and should be counted too.
4. All pairs $(i', j)$ where $i' < i$ and where $B[i] + B[j] < m$ are ignored and not added to the count, as $B[i'] < B[i]$.
4. The count accurately reflects the number of valid pairs.

Initialisation: $i = 0$ and $j = len(B) - 1$. There are no previously counted pairs.

Iteration: We check to see if the current pair add up to $m$: $B[i] + B[j] >= m$. 

If $B[i] + B[j] >= m$:

- the current pair $(i, j)$ is valid since their sum is at least $m$.
- for every $i'$ where $i <= i' < j$, the pair $(i', j)$ is also valid, as $B[i']$ is greater than or equal to $B[i]$ due to the sorted list.
- the number of these valid pairs is $j-i$, which we add to our counter. 
- in order to avoid double counting, we decrement $j$. 
- hence we have found the smallest value of $i$, which, when added with $j$, is more than or equal to $m$. We briefly count the all other values of $i'$ to be valid pairs with $j$. Therefore, we do not need to consider $j$ anymore, and decrement our $j$ by 1 to consider the next largest value, which we will pair our values of $i$ with.

If $B[i] + B[j] < m$:

- the current pair $(i, j)$ is not valid since their sum is less than $m$.
- for every $i'$ where $i' <= i$, the pair $(i', j)$ is also **not** valid, as $B[i']$ is less than or equal to $B[i]$ due to the sorted list.
- we do not add anything to the counter.
- as the current $j$ is the largest value of $j$, we need to increment $i$ to find a larger number which when added with $j$ sums up to greater than or equal to $m$.

Termination:

The loop termiantes when $i >= j$, which means that are no more unique pairs to consider. The count reflects all valid pairs, as determined by the loop invariant that has been maintained.


*c) Analyse the running time of your algorithm.*

The algorithm begins by creating and storing variables for the size of the array, set to ```n```, a counter for valid pairs ```count```, and an ```i``` and ```j``` pointer. These are run in constant time $O(1)$. Regardless of the number of integers in the array, the number of initialisation variables remain the same.

The bulk of this algorithm comprises of the ```while``` loop which runs while ```i < j```. Inside the ```while``` loop, ```line 7``` ```if B[i] + B[j] >= m:``` performs a constant-time check to see if $B[i] + B[j]$ is greater than $m$. Comparisons are run in constant time. If it is larger, then the ```count``` variable is updated in constant time, where arithmetic operations are run in constant time. Decrementing ```j``` by 1 in ```line 9``` is also run in constant time $O(1)$. Else, if the sum is less than $m$, then ```i``` is incrementing which takes place in constant $O(1)$ time. 

The focus is the while loop. By nature, $i$ or $j$ can move across the array at most $n$ times in total, where $n$ is the length of the array. 
- $i$ can increment from $(0, n-1)$, which is at most $n-1$ increments.
- $j$ can decrement from $(n-1, 0)$ which is at most $n-1$ decrements.

Whilst each pointer can move $n-1$ times at most, the while loop terminates when $i<j$. Given that $i$ and $j$ are at the start and end of the array and move toward each other, through increments or decrements, the loop will run until they meet, which can happen **at most**, after $n$ iterations. Given a number of integers $n$ in the array, there is no significantly distinguishable best and worst case. If there are absolutely no pairs, $i$ would have to increment $n-1$ times, until it reaches $j$, in which case the loop terminates in $O(n)$ time. If the sum of the elements at the initial indices $i, j$ are already greater than or equal to $m$, then the algorithm will still decrement $j$ in each iteration $n-1$ times until it meets with $i$, in whihc case the loop terminates in $O(n)$ time.

Even if we consider iterating through the last half of the list, where $i = \frac{n}{2}$, each pointer can increment/decrement at most $n-1 - \frac{n}{2}$, which runs in $\Omega(n)$ time.

## TODO - Clean up problem 2 correctness using invariant "#461, #462"

[1, 3, 5, 7, 8, 9]
target = 11
i, j = 0, 5
b0 + b5 = 10
incr i by 1
i, j = 1, 5
b1 + b5 = 3 + 9 = 12 > 11
(1, 5), (2, 5) (3, 5), (4, 5)
decr j by 1
i, j = 1, 4
b1 + b4 = 11 >= 11
(1, 4) (2, 4) (3, 4) = 4 - 1
decr j by 1
i, j = 1, 3
b1 + b3 = 10
incr i by 1
i, j = 2, 3
b2 + b3 = 12
2, 3
j - 1
i = j, end


i, j = 0, 5
b0 + b5 = 10
incr i by 1
i, j = 1, 5
b1 + b5 = 12
incr 1 by 1
i, j = 2, 5
b2 + b5 = 14
count += 5-3 (5, 9), (7, 9), (8, 9)
decr j by 
