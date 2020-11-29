import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)

def draw(t, counter, size):
    if counter == 0:
        t.forward(size)
    else:
        draw(t, counter - 1, size/3)
        t.left(60)
        draw(t, counter - 1, size/3)
        t.right(120)
        draw(t, counter - 1, size/3)
        t.left(60)
        draw(t, counter - 1, size/3)

    '''
    if counter == 0:
        t.forward(size)
    else:
        new_counter, new_size = counter - 1, size / 3
        draw(t, new_counter, new_size)
        t.left(60)
        draw(t, new_counter, new_size)
        t.right(120)
        draw(t, new_counter, new_size)
        t.left(60)
        draw(t, new_counter, new_size)
    '''

def draw(t, size):
    t.forward(size/3)
    t.left(60)
    t.forward(size/3)
    t.right(120)
    t.forward(size/3)
    t.left(60)
    t.forward(size/3)
size = 1140
t.up()
t.goto(-570, 320)
t.down()
draw(t, size/3)
t.left(60)
draw(t, size/3)
'''
t.up()
t.goto(-570, 320)
t.down()
draw(t, 4, 1140)
t.right(120)
draw(t, 4, 1140)
t.right(120)
#draw(t, 8, 1140)
draw(t, 4, 1140)
'''

wn.update()
wn.mainloop()
