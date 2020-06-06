---
layout: slides
title: File I/O 
---
<section markdown="block" class="title-slide">
#  File I/O
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Using Files

__How do we read information from a file?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
in_file = open('my_file.txt', 'r')

#  iterate over file object
for line in in_file:
	# do stuff

#  read entire contents of file as string
contents = in_file.read()

#  read entire contents of file as list
lines = in_file.readlines()

#  read one line at a time (check if empty)
line = in_file.readline()

#  remember to close!
in_file.close()
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Using Files Continued

__Aaaand how about writing to a file?__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
out_file = open('my_file.txt', 'w')

#  write out to a file
out_file.write('foo!')

#  remember to close!
out_file.close()
{% endhighlight %}

</div>
</section>

<section markdown="block">
###  An Exercise

You have a file called __numbers.txt__.

{% highlight python %}
Numbers
5,2
9,3
144,12
{% endhighlight %}

* extract the numbers from each line
* ignore the first line
* divide the 1st number by the 2nd number
* create a new file called __results.txt__ with the results of each calculation:

{% highlight python %}
Results
2.5
3.0
12.0
{% endhighlight %}
</section>


<section markdown="block">
###  An Exercise Continued

__Now modify your file to handle this input file.__

{% highlight python %}
Numbers
hello,2
9,0
144,12
{% endhighlight %}

* use __try__ / __except__ 
* there are two exceptions you'll need to handle
* __results.txt__ should contain:

{% highlight python %}
Results
not a number
divided by 0!
12.0
{% endhighlight %}

</section>
