
# Overview 

Solutions in Python 

## Sol1.py 

[Sol1.py](sol1.py)

Comments 

- The naive solution of course won't work because even if correct it won't fit in the time budget 

- In terms of cost in fact, considering `K = Number of Queries` and `N = Size of Array` then 

- The Naive Solution is `O(NK)`

- The idea implemented in Sol1 is to avoid updating each array value for each query but to store only the derivative the query produces 

- So in order to solve the problem, at the end it is necessary to integrate over the derivatives storing array and track the max reached 

- To sum hence the query cost gets down to `O(1)` so applying the full set of queries is `O(K)` while the final integration loop is `O(N)` which means the full algo costs max between `O(K)` and `O(N)`







