---
layout: slides
title: "Counting"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>
<section markdown="block">
##  Frequency of Dice Rolls

* roll two three sided dice simultaneously 1000 times 🎲
* [(btw, what does a three-sided die look like?)](https://www.google.com/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1303&bih=730&q=three+sided+die&oq=three+sided+die)
* count the frequency of the results... 2 through 6
* __let's code that up really quickly__, without using any compound data types (so, no `list`, `tuple`, `set`, etc.)
	* generate two random numbers
	* do this 1000 times
	* keep track of the number of times a two is rolled... a three... up through six
	* use multiple assignment for initializing your counts!

<!-- (http://suptg.thisisnotatrueending.com/archive/14752803/images/1304091112226.jpg) -->
</section>

<section markdown="block">
## Dice Rolls Solution 

<pre><code data-trim contenteditable>
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
    roll = random.randint(1,3) + random.randint(1,3)
    if roll == 2:
        twos += 1
    if roll == 3:
        threes += 1
    if roll == 4:
        fours += 1
    if roll == 5:
        fives += 1
    if roll == 6:
        sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 

</code></pre>
</section>


<section markdown="block">
### Dice Rolls 

Whew! 😅

That was a long if-else.  What if we had to write one for two twenty-sided dice?  

* {:.fragment} that would be pretty lengthy
* {:.fragment} and consequently error prone
* {:.fragment} also, seeing that lengthy if-else makes me feel _sad_ 😭

What are some other alternatives?
{:.fragment}
</section>
<section markdown="block">
## Lists (Only)

__Use two lists: one to keep track of the rolls, and the second to keep track of the counts.__ &rarr;

<pre><code data-trim contenteditable>
import random
items, counts = [], []
for roll in range(1000):
    roll = random.randint(1, 3) + random.randint(1, 3)
    if roll in items:
        counts[items.index(roll)] += 1
    else:
        items.append(roll)
        counts.append(1)
for i, val in enumerate(items):
    print(val, 'x', counts[i])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Lists and Sets

__Store all of the rolls in a list, and count each unique element (easy with a set, but can also construct with a secondary list)__ &rarr;

<pre><code data-trim contenteditable>
import random
rolls = []
for roll in range(1000):
    rolls.append(random.randint(1, 3) + random.randint(1, 3))
for roll in set(rolls):
    print(roll, 'x', rolls.count(roll))
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## With a dictionary

__Use a dictionary's keys as the thing to be counted and its values as the actual counts__ &rarr;

<pre><code data-trim contenteditable>
import random
freq_dice_rolls = {}
for i in range(1000):
    roll = random.randint(1, 3) + random.randint(1, 3)
    if roll in freq_dice_rolls:
        freq_dice_rolls[roll] += 1
    else:
        freq_dice_rolls[roll] = 1
print(freq_dice_rolls)
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## Exception Handling / Get

__Rather than checking for the existence of a key, exception handling and the `.get` method can be used__ &rarr;

1. {:.fragment} If we get a `KeyError`, set the value to 1:
	<pre><code data-trim contenteditable>
try:
    freq_dice_rolls[roll] += 1
except KeyError:
    freq_dice_rolls[roll] = 1
</code></pre>
2. {:.fragment} Use `.get`'s default value and add 1
	<pre><code data-trim contenteditable>
freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1
</code></pre>
</section>


<section markdown="block">
## Counter Object

__A `Counter` object is a dictionary-like object with features specifically for keep track of counts__ &rarr;

Creating a `Counter`:
{:.fragment}

1. {:.fragment} `from collections import Counter`
2. {:.fragment} use the `Counter` function (it's a "constructor"):
	<pre><code data-trim contenteditable>
c = Counter() # empty counter
</code></pre>

</section>

<section markdown="block">
## The Counter Constructor

__`Counter` can be initialized with values:__ &rarr;

<pre><code data-trim contenteditable>
# passing in a list creates each list item as a key
# and the count of each items as the value
# {'heads': 3, 'tails': 1}
c = Counter(['heads', 'heads', 'tails', 'heads'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# beware - this is for any literal, so 'aabbbc'
# {'a': 2, 'b': 3, 'c': 1}
c = Counter('aabbbc')
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# finally, keyword arguments work too!
# (no quotes)
c = Counter(heads=5, tails=1)
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Counter vs Dictionary

__If a key doesn't exist in a counter, 0 is returned rather than a runtime error occurring (no `KeyError`)__ &rarr;

<pre><code data-trim contenteditable>
c = Counter()
print(c['tails'])  # 0 instead of KeyError
</code></pre>
{:.fragment}

This feature allows us to fearlessly increment! 😈
{:.fragment}

<pre><code data-trim contenteditable>
# do we even know if the key, 'heads', exists?
# NOPE! but everything's ok
c['heads'] += 1
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Counter Methods

__Counter objects offer some convenient methods__ &rarr;

* {:.fragment} `elements` - gives back list like object (an _iterable_) that contains each element repeated based on its count
* {:.fragment} `most_common(n)` - gives back the `n` most common elements (or all if n is not passed in) as a list of tuples (first index is element, second is count)
</section>

<section markdown="block">
## Finally, Using a Counter

<pre><code data-trim contenteditable>
import random
from collections import Counter
c = Counter()
for roll in range(1000):
    c[(random.randint(1, 3) + random.randint(1, 3))] += 1
print(c)
</code></pre>
</section>
