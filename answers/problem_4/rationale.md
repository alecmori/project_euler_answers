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

## Proof 1: Given <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/ab15186021e40b8624ac175df5be923e.svg?invert_in_darkmode" align=middle width=72.76863pt height=22.381919999999983pt/>, <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/6ba740927cdc41d29ccefa1b4f4f1631.svg?invert_in_darkmode" align=middle width=103.133745pt height=24.56552999999997pt/> is maximized when <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/4046156e0cc4653d0192c20a9501c2e3.svg?invert_in_darkmode" align=middle width=90.519825pt height=24.56552999999997pt/>

If you just want to confirm against you gut instinct, feel free to set <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/612444b82593db589936ada174a27d89.svg?invert_in_darkmode" align=middle width=42.939105pt height=22.381919999999983pt/> and enumerate

<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/6f44da277b23ccf9bba665b83e828800.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/42b38f5845814df0d44fcdfe1e7de615.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/21ab8e49204af85582ac4c4e70592ede.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/34a201c9f7d308907d2b60fc513f7ab3.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/e2166dfd3132b7b13b447152114ed41a.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/8dabaef318f10a05074060ddefe0ab57.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/af5912d18ecc53b334e3258a45f7c112.svg?invert_in_darkmode" align=middle width=170.52419999999998pt height=16.376943pt/></p>

However, this can also be solved with some calculus.

<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/bbbc0ded94da1c020dfb7d1bd3cc3874.svg?invert_in_darkmode" align=middle width=171.0555pt height=14.3753115pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/a2e79932b5bd706007ef54434be091bf.svg?invert_in_darkmode" align=middle width=283.2192pt height=16.376943pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/dd089887450cb00d1330727bb974e143.svg?invert_in_darkmode" align=middle width=227.8716pt height=17.250255pt/></p>
<p align="center"><img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/7c99a89a197fb0c385164a9b7bdca674.svg?invert_in_darkmode" align=middle width=166.07084999999998pt height=16.376943pt/></p>

Because <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/0a86c91817c3463af1d624e120046b36.svg?invert_in_darkmode" align=middle width=131.135235pt height=24.668490000000013pt/> and <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/27ec5c2067a5d67b62049782efa69291.svg?invert_in_darkmode" align=middle width=131.135235pt height=24.668490000000013pt/>, we know this is a maximum. Because <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/3381855c1c02e0f03e27b65c005d6c95.svg?invert_in_darkmode" align=middle width=60.03096pt height=24.56552999999997pt/> is the only time <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/8a273a027e69ad055166571f8e7835ab.svg?invert_in_darkmode" align=middle width=66.555225pt height=24.668490000000013pt/>, this is the global maximum.

Plugging <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/3381855c1c02e0f03e27b65c005d6c95.svg?invert_in_darkmode" align=middle width=60.03096pt height=24.56552999999997pt/> back into the first equation yields <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/260acb5faa22c91fe24fc5623f789fde.svg?invert_in_darkmode" align=middle width=59.29011pt height=24.56552999999997pt/>, making the maximum point along this function <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/ed758013f632fc83e825845ce04c5359.svg?invert_in_darkmode" align=middle width=77.628705pt height=24.56552999999997pt/>. Q.E.D.

## Proof 2: Given <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/659a3575b9b6f5ae42bbb53ff4369357.svg?invert_in_darkmode" align=middle width=92.2845pt height=22.381919999999983pt/> and <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/ada5231ffcadf2940bbc948ddcb05e35.svg?invert_in_darkmode" align=middle width=92.2845pt height=22.381919999999983pt/> where <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/7950d646528f30cb67bcec009d0243e8.svg?invert_in_darkmode" align=middle width=59.182365000000004pt height=22.381919999999983pt/>, <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/1a5789db93834a84626ed26aa6167735.svg?invert_in_darkmode" align=middle width=236.04124499999998pt height=24.56552999999997pt/> when <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/6ba740927cdc41d29ccefa1b4f4f1631.svg?invert_in_darkmode" align=middle width=103.133745pt height=24.56552999999997pt/>

#TODO Link proof 1
Using the results in Proof 1, we know <img src="https://rawgit.com/alecmori/project_euler_answers (fetch/None/svgs/d80a2e18699f02d7ada4341f19493131.svg?invert_in_darkmode" align=middle width=320.971695pt height=37.24248000000001pt/>
