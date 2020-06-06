---
layout: homework
title: "Practice"
---

<style>
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}
</style>


# Practice

### Setup

* [download list_utils.py](../assignments/hw07/practice.py)

### Complete Missing Function Definitions

All of the functions in <code>practice.py</code> have headers, but
none of them have a body. __Some of the functions don't return a value,
but instead change the original argument passed in__...

1. Implement the functions listed below
2. The docstrings in <code>list_utils.py</code> contain additional details for how the functions should work
3. Copy and paste the example usage in your <code>if __name__ == '__main__'</code> part of <code>practice.py</code> to test your completed functions
4. Run your code and make sure that your program's output matches the expected values displayed below  (do not remove your tests / keep them in the file that you submit)

### flattened

<code>flattened(lst)</code>


<code> # Given a list of lists, lst, create a new list composed of all elements from the sublists so that there are no longer any nested lists. You can assume that the argument passed in is a list of lists.</code>

Example Usage

<pre><code data-trim contenteditable>print("\nflattened\n=====")
nested = [[1, 2], [3, 4]]
flat = flattened(nested)
print(flat) # --> [1, 2, 3, 4]
</code></pre>

Expected Output

<pre><code data-trim contenteditable>shifted_left
=====
[1, 2, 3, 4]
</code></pre>

<br>


### shift\_left

<code>shift_left(lst, n, fill_value=0)</code>

<code># Shifts the elements in list, lst, by n places to the left. This is done in place (the original list passed in is changed)</code>

Example Usage

<pre><code data-trim contenteditable>print("\nshift_left\n=====")
numbers = [1, 2, 3, 4]
shift_left(numbers, 2)
print(numbers)
numbers = [1, 2, 3, 4]
shift_left(numbers, 5)
print(numbers)
numbers = [1, 2, 3, 4]
shift_left(numbers, -5)
print(numbers)
numbers = [1, 2, 3, 4]
shift_left(numbers, 1, None)
print(numbers)
</code></pre>

Expected Output

<pre><code data-trim contenteditable>shift_left
=====
[3, 4, 0, 0]
[0, 0, 0, 0]
[1, 2, 3, 4]
[2, 3, 4, None]
</code></pre>

<br>

### shifted_left

<code>shifted_left(lst, n, fill_value=0)</code>

<code> # Creates a new list with elements shifted left by n places.</code>

Example Usage

<pre><code data-trim contenteditable>print("\nshifted_left\n=====")
numbers = [1, 2, 3, 4]
print(shifted_left(numbers, 2))
print(shifted_left(numbers, 5))
print(shifted_left(numbers, -5))
print(shifted_left(numbers, 1, None))
</code></pre>

Expected Output

<pre><code data-trim contenteditable>shifted_left
=====
[3, 4, 0, 0]
[0, 0, 0, 0]
[1, 2, 3, 4]
[2, 3, 4, None]
</code></pre>

<br>

### shift\_right

<code>shift_right(lst, n, fill_value=0)</code>

<code># Shifts the elements in list, lst, by n places to the right.</code>

Example Usage

<pre><code data-trim contenteditable>print("\nshift_right\n=====")
numbers = [1, 2, 3, 4]
shift_right(numbers, 2)
print(numbers)
numbers = [1, 2, 3, 4]
shift_right(numbers, 5)
print(numbers)
numbers = [1, 2, 3, 4]
shift_right(numbers, -5)
print(numbers)
numbers = [1, 2, 3, 4]
shift_right(numbers, 1, None)
print(numbers)
</code></pre>

Expected Output

<pre><code data-trim contenteditable>shift_right
=====
[0, 0, 1, 2]
[0, 0, 0, 0]
[1, 2, 3, 4]
[None, 1, 2, 3]

</code></pre>

<br>

### shifted\_right

<code>shifted_right(lst, n, fill_value=0)</code>

<code># Creates a new list with elements shifted right by n places.</code>

Example Usage

<pre><code data-trim contenteditable>print("\nshifted_right\n=====")
numbers = [1, 2, 3, 4]
print(shifted_right(numbers, 2))
print(shifted_right(numbers, 5))
print(shifted_right(numbers, -5))
print(shifted_right(numbers, 1, None))
</code></pre>

Expected Output

<pre><code data-trim contenteditable>shifted_right
=====
[0, 0, 1, 2]
[0, 0, 0, 0]
[1, 2, 3, 4]
[None, 1, 2, 3]
</code></pre>

<br>

### fill

<code>fill_in_place(lst, fill_value=0)</code>

<code># Fills an existing list, lst, with the value, fill_value.</code>

Example Usage

<pre><code data-trim contenteditable>print("\nfill\n=====")
numbers = [1, 2, 3, 4]
fill_in_place(numbers)
print(numbers)
numbers = [1, 2, 3, 4]
fill_in_place(numbers, fill_value=None)
print(numbers)
</code></pre>

Expected Output

<pre><code data-trim contenteditable>fill
=====
[0, 0, 0, 0]
[None, None, None, None]
</code></pre>

<br>

