## $\text{Specification}$.
Given an array of integers, $\large \text{nums}$, return the _number_ of _good pairs_.

A pair, $\large (i, j)$ is called _good_ if $\large \text{nums[i] == nums[j]}$ and $\large i < j$.

## $\text{Algorithm}$.
1. Initialize an empty dictionary $\large \text{count}$  to keep track of the number of occurrences of each number.
2. Iterate the number list and do:
	1. Add each number to $\large \text{count}$ if it has not yet been added 
3. Initialize a variable $\large res$ to keep track of number of pairs.
4. Iterate the dictionary, $\large \text{count}$, and do:
	1. if the current number only appears once, skip
	2. Otherwise, for some number of appearances $\large k: k >1$ at each element, let $\large res := res + \sum_{n=k}^{1}n-1$
5. Return the variable $\large \text{res}$.

## $\text{Analysis}$.
By iterating through the array and keeping track of the number of occurrences of each number, we are able to perform a mathematical analysis. We know that for any arbitrary array $\large A$ with $\large k$ elements, if there are $\large n$ repetitions, then the total number of pairs that are formed is given by 

```math 
\large 
S = n-1 + n-2 + n-3 + \ldots  + 1.
```
We can see this is the case as shown below. Suppose we have an array $\large A$ as such:
```math
\large 
A = [1,2, 3, 1, 1, 3]
```
we can see that 
```math
\large 
\begin{array}{c |c | c}

\text{Number}  & 1 & 2 & 3\\ 
\hline
\text{Occurence(s)} & 3 & 1 & 2\\
\end{array}
```
Therefore, the total number of pairs for each number are:
```math 
\large 
\begin{aligned}
\text{Number} &:= 1 => (3-1) + (3-2) = 3 \text{ pairs} \\[7pt]
&:= 3 => (2 - 1) \text{ pairs}.
\end{aligned}
```
So adding them altogether gives us $\large 4$ _good_ pairs.
