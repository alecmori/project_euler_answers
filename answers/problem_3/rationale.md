Conceptually, this problem is pretty easy to wrap your head around: given a number $n$, find the prime factorization such that

#TODO: Use product symbol
$$n=p_1^{c_1}p_2^{c_2}...p_k^{c_k}=ProductSymbol p_i^{c_i}$$

where each $p_i$ is a distinct prime number, and each $c_i$ is a positive integer. Every positive integer has exactly one of these, so we should always have exactly one $p_i$ such that $p_i > p_j$.

How do we get a prime factorization? There are many ways but I am going for a fairly naive one, namely;

1. Generate prime numbers (I used the [Sieve of Atkins](link somewhere)) up until $\sqrt{n}$. Call this set of prime numbers $P$
# TODO: Use congruent to and all and iff
2. Create a new set of prime numbers $P'$ where $P' = \all p_i \in P iff n mod p_i = 0$
3. For each $p_i \in P'$, find the largest $c_i$ such that $n mod p_i^{c_i} = 0$.

There are ways to improve this algorithm, such as dividing $n$ by $p_i^{c_i}$ so you don't need to compute on such large numbers, but overall this should be fine.
