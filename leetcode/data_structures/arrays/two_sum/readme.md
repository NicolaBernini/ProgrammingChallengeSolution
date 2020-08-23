
# Overview 

Solution to Two Sum Leetcode Exercise

https://leetcode.com/problems/two-sum/submissions/



First we will the see the Algo explained in a language agnostic way and then we will some of its concrete implementation in different languages to familarize with the language syntax and its data structures 


# Algo in Pseudocode 

- In terms of pseudocode a good efficient solution would consist of the following Algo 

Algo 1 

```
1. Iterate over the array and build a dict where 
  - key : number 
  - value : index in the array
2. Iterate over the array and for each n look up for the corresponding (target-n) in the dict 
```

Having built the dict at step1 provides O(1) lookup which is key 

However it is still possible to do better obsering that it is still possible to do Step 2 while doing Step 1 : 

- using a math notation, let's call 
  - $a(i) \rightarrow n$ : the input array 
    - with $i \in \mathbb{N}^{+} \cap [0..N), n \in \mathbb{R}$
  - $d(n) \rightarrow i \cup \text{False}$ : the dict 
  - $n_{i}$ : the result of $n_{i} = a(i)$ the observation of the i-th element of the array 
  - $t$ : the target of the sum 
  - $x$ : the corresponding number summing up to the target
- at Step1 after $i<N$, so while we are still building $d(\cdot)$ we have $n_{i}$ but intstead of just putting it into the $d$ we have to observe it is possible the corresponding number $x = t - n_{i}$ is already in $d$ 
- to check this, we can just have a O(1) lookup $d(t-n_{i})$ and if the result is not $\text{False}$ we have solved the problem as the solution is the tuple $\{d(t-n_{i}),i\}$
- otherwise if the look up fails we just add $n_{i}$ to $d$ as we would have done normally 
- however it is important to observe 

$$\lim_{i \rightarrow N} P( d(t-n_{i}) \text{not False}) \rightarrow 1$$ 

- which means the probability of finding the corresponding number converges to 1 because of the guarantess provided in the problem description, as we approach the end of the array 
- in fact thanks to this observation we know we actually do not need any Step2 this way 




This way we can optimize Algo 1 as follows 

Algo 3

```
1. Iterate over the array and get n 
2. Lookup in the dict if the corresponding number is there 
2.1 If True, return indexes of both and solve 
2.2 If False, add key=number and value=index 
```




