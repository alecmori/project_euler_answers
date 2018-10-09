Although we can reverse a number arithmatically, palindromic problems are probably best found using lexical tools, namely strings (this might not be true in Cython, have not benchmarked it).

The native thing to do would be to iterate through all pairs of three digit numbers, and choose the largest palindromic product from the answers.

```python
max_product = -1
for a in range(100, 1000):
    for b in range(100, 1000):
        if _is_palindromic(a * b)
        max_product = max(
            a * b,
            max_product,
        )
```

Despite this pseudocode starting at 100, our gut instinct should tell us that we probably want to start closer to the larger three digit numbers and work our way down. Ideally, we would sort the products by size (decreasing) and then choose the first product we see that is a palindrome. However, that is kind of a catch-22; in order to not compute smaller products, we must first have a list of all computed products. Can we generate the products we need one at a time instead? I argue yes.

## Proof 1: Given $x + y = C$, $f(x, y) = x * y$ is maximized when $x = y = C/2$

If you just want to confirm against you gut instinct, feel free to set $C=6$ and enumerate

$$x = 0, y = 6, f(x,y) = 0$$
$$x = 1, y = 5, f(x,y) = 5$$
$$x = 2, y = 4, f(x,y) = 8$$
$$x = 3, y = 3, f(x,y) = 9$$
$$x = 4, y = 2, f(x,y) = 8$$
$$x = 5, y = 1, f(x,y) = 5$$
$$x = 6, y = 0, f(x,y) = 0$$

However, this can also be solved with some calculus.

$$x + y = C \rightarrow y = C - x$$
$$f(x, y) = x * y \rightarrow f(x) = x * (C - x) \rightarrow $$
$$f'(x) = (C - x) + -x = C - 2x$$
$$ 0 = C - 2x \rightarrow x = C/2$$

Because $f'(x) > 0 | x < C/2$ and $f'(x) < 0 | x > C/2$, we know this is a maximum. Because $x = C/2$ is the only time $f'(x) = 0$, this is the global maximum.

Plugging $x = C/2$ back into the first equation yields $y = C/2$, making the maximum point along this function $(C/2, C/2)$. Q.E.D.

## Proof 2: Given $x_1 + y_1 = C_1$ and $x_2 + y_2 = C_2$ where $C_1 > C_2$, $max(f(x_1, y_1)) > max(f(x_2, y_2))$ when $f(x, y) = x * y$

#TODO Link proof 1
Using the results in Proof 1, we know $max(f(x_1, y_1)) = \frac{C_1^2}{4} > \frac{C_2^2}{4} = max(f(x_2, y_2))$
