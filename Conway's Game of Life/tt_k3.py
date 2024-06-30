import turtle

def draw_square(t, size, x, y, square_id, color):
    t.penup()
    t.goto(x, y)
    # t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    return square_id, color

def draw_grid(rows, cols, size):
    screen = turtle.Screen()
    w = cols * size + 100
    h = rows * size + 100
    screen.setup(w, h) 
    screen.screensize(cols * size, rows * size)  

    t = turtle.Turtle()
    t.hideturtle() 

    screen.tracer(0, 0) 

    square_id = 1
    colors = ["pink", "black"]
    time = 0
    import random
    numbers = list(range(900))
    begin = [random.sample(numbers, 200)]
    import numpy
    begin = numpy.sort(begin)
    print(begin)
    start_key = 1
    map = {}
    k =[2,3]
    # bmap= {}
    while True:
        t.clear()
        square_id = 1
        for row in range(rows):
            for col in range(cols):
                x = col * size
                y = -(row * size)
                if start_key == 1:
                    if square_id in begin:
                        sid, clr = draw_square(t, size, x - cols * size / 2, y + rows * size / 2, square_id, 'pink')
                        map[sid] = clr
                    else:
                        sid, clr = draw_square(t, size, x - cols * size / 2, y + rows * size / 2, square_id, 'black')
                        map[sid] = clr
                    import copy
                    bmap = copy.copy(map)
                    
                else:
                    c = 0 
                    dic = []
                    if square_id % rows in [0, 1] or square_id < rows or square_id > rows*(rows-1):
                        if not square_id - 1 in map:
                            map[square_id - 1] = 'black'
                            dic.append(square_id - 1)
                        if not square_id + 1 in map:
                            map[square_id + 1] = 'black'
                            dic.append(square_id + 1)
                        if not square_id - 1 - rows in map:
                            map[square_id - 1 - rows] = 'black'
                            dic.append(square_id - 1 - rows)
                        if not square_id + 1 - rows in map:
                            map[square_id + 1 - rows] = 'black'
                            dic.append(square_id + 1 - rows)
                        if not square_id - rows in map:
                            map[square_id - rows] = 'black'
                            dic.append(square_id - rows)
                        if not square_id - 1 + rows in map:
                            map[square_id - 1 + rows] = 'black'
                            dic.append(square_id - 1 + rows)
                        if not square_id + 1 + rows in map:
                            map[square_id + 1 + rows] = 'black'
                            dic.append(square_id + 1 + rows)
                        if not square_id + rows in map:
                            map[square_id + rows] = 'black'
                            dic.append(square_id + rows)
                        if map[square_id + 1] == 'pink':
                            c += 1
                        if map[square_id + 1] == 'pink':
                            c += 1
                        if map[square_id - 1 - rows] == 'pink':
                            c += 1
                        if map[square_id + 1 - rows] == 'pink':
                            c += 1
                        if map[square_id - rows] == 'pink':
                            c += 1
                        if map[square_id - 1 + rows] == 'pink':
                            c += 1
                        if map[square_id + 1 + rows] == 'pink':
                            c += 1
                        if map[square_id + rows] == 'pink':
                            c += 1
                        if c == 3:
                            bmap[square_id] = 'g'
                        else:
                            bmap[square_id] = 'b'   
                        for i in dic:
                            map.pop(i, None)
                    else:
                        c = 0
                        # print(map)
                        if map[square_id - 1] == 'pink':
                            c += 1
                        if map[square_id + 1] == 'pink':
                            c += 1
                        if map[square_id - 1 - rows] == 'pink':
                            c += 1
                        if map[square_id + 1 - rows] == 'pink':
                            c += 1
                        if map[square_id - rows] == 'pink':
                            c += 1
                        if map[square_id - 1 + rows] == 'pink':
                            c += 1
                        if map[square_id + 1 + rows] == 'pink':
                            c += 1
                        if map[square_id + rows] == 'pink':
                            c += 1
                        # print(c, end=' ')
                        if c == 3:
                            bmap[square_id] = 'g'
                        else:
                            bmap[square_id] = 'b' 
                        
                square_id += 1
        # print(bmap)
        for i in range(len(map)):
            i += 1
            if bmap[i] == 'b':
                map[i] = 'black'
            elif bmap[i] == 'g':
                map[i] = 'pink'
            draw_square(t, size, x - cols * size / 2, y + rows * size / 2, i, map[i])
            # print()
        t.clear()
        square_id = 1
        for row in range(rows):
            for col in range(cols):
                x = col * size
                y = -(row * size)
                sid, clr = draw_square(t, size, x - cols * size / 2, y + rows * size / 2, square_id, map[square_id])

                        
                square_id += 1
        start_key = 0
        time += 1

        screen.update()
        turtle.time.sleep(0)

draw_grid(30, 30, 10)
