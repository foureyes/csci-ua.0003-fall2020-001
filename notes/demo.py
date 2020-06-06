#  of slices in a pie
people = input("how many people are eating pizza?\n>")

try: 
    print("Each person can have %s slices" % (8/int(people)))
except ValueError:
    print('need a number plz!')
except ZeroDivisionError:
    print('moar 4 me!!!!')

'''
answer = input('give me number of inches\n>')


# if you receive a runtime error
# program crashes
# it allows to you prevent a crash from some code that could cause exceptions

# open a file... and if file doesn't exist, program crashes



# check before attempting 
# use re module and match
# regular expression module
# allows you to define patterns that match strings
# match [0-9]+.?[0-9]*
# defensive.... check values first (ask for permission)
# then do the thing you want easier to ask for forgiveness than permission
try:
    # the single line that causes the error should be here
    inches = float(answer) # error here... type is ok (str), but value maybe "the!!!"
except ValueError:
    print('error!!!!')
except SomeOtherError:
    print('do some other thing')
finally:
    inches = None

if inches:
    feet = inches / 12
    print('number of feet is', feet)

'''


'''
try:
    # tricky code that may cause errors
except ValueError:
    # handle error here
'''
'''
if answer.isnumeric():
    inches = float(answer) # error here... type is ok (str), but value maybe "the!!!"
    feet = inches / 12
    print('number of feet is', feet)
else:
    print('give me a number plz!!!!')
'''
