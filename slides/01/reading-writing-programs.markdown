---
layout: slides
title: Reading and Writing Programs
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
##  Reading and Writing Python Files
</section>

<section markdown="block">
##  About PyCharm

__What are the three ways that we can use PyCharm? &rarr;__

<div class="fragment" markdown="block">
1. Create or open existing Python files in a text-editor view (and view the output of your program through the interactive Python shell) 
2. Type and run commands line-by-line through the Python Shell
3. Debug an existing Python program
</div>

</section>

<section markdown="block">
##  Again, You Can...

* run your program all at once 

<aside>or</aside>

* run commands one-step-at-a-time using the interactive Python shell

Lastly, if your program ever outputs anything, it should show up in the interactive Python Shell
</section>


<section markdown="block">
##  PyCharm Demo

* projects
* file system
* files in projects
* running a file
* interactive shell
</section>

<section markdown="block">
##  A First Program

__"Hello world!"__ is traditionally the first program you write when learning a new language.  It simply outputs "Hello world" (yeah, that's all).  __Follow these steps__:

* create a new file
* type in ...

<pre><code data-trim contenteditable>
print("Hello world!")
</code></pre>

* run your program
	* you may be prompted you to save your file
	* if you haven't saved it yet, you'll be prompted for a file name

<details>
</details>
</section>

<section markdown="block">
##  Modifying Your Program
<aside>Most of the time, we're editing existing programs rather than creating entirely new ones</aside>

Let's modify the program that we just wrote:

* if your file is closed, reopen it
* add a second line:

<pre><code data-trim contenteditable>
print("Hi again!")
</code></pre>

* run your program

<details>
</details>
</section>

<section markdown="block">
##  Making Mistakes
<aside>Programs don't always work the way we expect them to!</aside>

Let's purposely make a mistake, then fix it

* if your file is closed, reopen it
* add a third line, but leave off the last parentheses: 

<pre><code data-trim contenteditable>
print("Hola"
</code></pre>

* run your program
* you should see a pop-up and a red highlight where your syntax error occurred
* this occurs if your program is not syntactically correct
* fix the mistake (how?)

<details markdown="block">
* DEMO - make a syntactic mistake, show where the error is
* QUESTION - How do we fix this?
</details>
</section>

<section markdown="block">
##  Making More Mistakes
<aside>That was syntactic mistake; what about errors that occur when the program is actually running?</aside>

Let's make a run-time error:

* if your file is closed, reopen it
* add a fourth line: 

<pre><code data-trim contenteditable>
print("Howdy" + 2)
</code></pre>

* run your program
* you should see the error in the console
* let's read it and try to interpret it
* fix the error
* note that the current line number is on the lower-right-hand corner of the window (prefixed with "Ln: ")

<details>
DEMO - make a run-time error
QUESTION - what line number did the error happen on?
DEMO - find the line
</details>
</section>

<section markdown="block">
##  Errors

Notice that we looked at two different _types_ of errors:

* __syntax error__ - an error with the syntax/structure of the program; the program cannot run _at all_
* __runtime error__ - the program is syntactically correct, but some sort of error occurs while the program is running
</section>

<section markdown="block">
##  A Quick Note on Syntax Highlighting

* The different colors represent different syntactic elements
* Some examples include
	* __strings__ - green
	* __built-in functions__ - purple 
	* __keywords__ - orange
* __strings__ - a primitive type of data in Python; a sequence of characters
* __keywords__ - (reserved words) words that have special meaning in Python

<details>
DEMO - function and for loop for syntax highlighting
</details>
</section>

