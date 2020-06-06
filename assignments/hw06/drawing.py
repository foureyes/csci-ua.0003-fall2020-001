def line(t, coord1, coord2):
    # write code here

def poly(t, *coords):
    # write code here

def rectangle(t, coord, width, height, color):
    # write code here

if __name__ == '__main__':
    import turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    rectangle(t, [0, 0], 100, 200, 'green')
    t.color('blue')
    poly(t, [100, 100], [50, 50], [-50, 50])
    poly(t, [-100, 100], [-100, 50], [-200, 50], [-200, 100], [-150, 0])
    #poly(t, [0, 0], 100, 200)
    wn.mainloop()
    
