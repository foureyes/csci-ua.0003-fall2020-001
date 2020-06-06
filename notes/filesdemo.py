"""




open
1. str: name of file you're opening
    * actual file name
    * can be absolute or relative path
    * /Users/jversoza/Desktop/foo.txt
    * foo.txt
        * this will be relative to pycharm project folder
2. str: a mode (single characters)
    * 'r'ead: file should exist
    * 'w'rite: will overwrite existing files or create
    * 'a'ppend: add to existing file
returns File Object

you can call methods on your file object
f.write(s) - write string to file
f.close() - to close your file object


"""
'''
fw = open('bar.txt', 'w') # will create if it doesn't exist
fw.write('more text here\none\ntwo\nthree')
fw.close()
#print(type(f))
#print(f)
'''
'''
fr = open('bar.txt', 'r')
for line in fr:
    print(line.strip())
fr.close()
'''

'''
# context manage allows some "clean up code" to be called
# automatically once a with block is left

# with some thing as some_variable
with open('bar.txt', 'r') as fr:
    for line in fr:
        print(line.strip())
# close will be called for you
# if you want to read a file
# simply loop over file object
# .readline() --- read one line at a time
# .readlines() --- entire file, but returns as list, where each list item is line from file
# .read() --- takes whole file and returns as a string
with open('bar.txt', 'r') as fr:
    content = fr.read()
    print(content)
with open('bar.txt', 'r') as fr:
    lines = [li.strip() for li in fr.readlines()]
    print(lines)
'''
'''
with open('bar.txt', 'r') as fr:
    print(fr.readline())
    print(fr.readline())


four ways of reading:

    prefer these
    > * iterate over file object

    * readline

    * read
    * readlines

depends on what data structure you want to store it in:
    do you need as a list? readlines()
    read / iteration

'''
with open('bar.txt', 'r') as fr:
    print('first loop')
    for line in fr:
        print(line.strip())
    print('second loop')
    for line in fr:
        print(line.strip())



























