The canonical way to think about the fibonacci sequence is to say

$$F_n = F_{n-1} + F{n-2} | n >= 3$$
$$F_1 = 1$$
$$F_2 = 2$$

However, running the function recursively would only cause more function than necessary - $O(2^n)$ without memoization, $O(n)$ with (and that's with an $O(n)$ space requirement as well). In order to get an $O(1)$ space fulfilled, I will opt to instead make a generator function and filter out only the values I need.

This is not very cythonic, but I think adds to the readability by separating out the iterating logic from the computation logic.
