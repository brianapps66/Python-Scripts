file = open('santa_directions.txt', 'r')

def find_array_size():
    x = 0
    y = 0
    x_max = 0
    x_min = 0
    y_max = 0
    y_min = 0
    for line in file:
        for c in line:
            if c == '>':
                x = x + 1
                if x > x_max:
                    x_max = x
            if c == '<':
                x = x - 1
                if x < x_min:
                    x_min = x
            if c == '^':
                y = y + 1
                if y > y_max:
                    y_max = y
            if c == 'v':
                y = y - 1
                if y < y_min:
                    y_min = y
    print(x, y, x_min, x_max, y_min, y_max)
    return [x, y, x_min, x_max, y_min, y_max]


def find_robo_array_size():
    real_x = 0
    real_y = 0
    robo_x = 0
    robo_y = 0
    real_x_max = 0
    real_x_min = 0
    real_y_max = 0
    real_y_min = 0
    robo_x_max = 0
    robo_x_min = 0
    robo_y_max = 0
    robo_y_min = 0
    switch = True
    for line in file:
        for c in line:
            if switch:
                if c == '>':
                    real_x = real_x + 1
                    if real_x > real_x_max:
                        real_x_max = real_x
                if c == '<':
                    real_x = real_x - 1
                    if real_x < real_x_min:
                        real_x_min = real_x
                if c == '^':
                    real_y = real_y + 1
                    if real_y > real_y_max:
                        real_y_max = real_y
                if c == 'v':
                    real_y = real_y - 1
                    if real_y < real_y_min:
                        real_y_min = real_y
                switch = not switch
            else:
                if c == '>':
                    robo_x = robo_x + 1
                    if robo_x > robo_x_max:
                        robo_x_max = robo_x
                if c == '<':
                    robo_x = robo_x - 1
                    if robo_x < robo_x_min:
                        robo_x_min = robo_x
                if c == '^':
                    robo_y = robo_y + 1
                    if robo_y > robo_y_max:
                        robo_y_max = robo_y
                if c == 'v':
                    robo_y = robo_y - 1
                    if robo_y < robo_y_min:
                        robo_y_min = robo_y
                switch = not switch
    print(real_x, real_y, real_x_min, real_x_max, real_y_min, real_y_max,
          robo_x, robo_y,
          robo_x_min, robo_x_max, robo_y_min, robo_y_max)
    return [real_x, real_y, real_x_min, real_x_max, real_y_min, real_y_max,
            robo_x, robo_y,
            robo_x_min, robo_x_max, robo_y_min, robo_y_max]


dimen = find_array_size()
houses = [[0 for j in range(abs(dimen[4])+dimen[5])] for i in range(abs(
    dimen[2])+dimen[3])]

start_x = abs(dimen[2])-1
start_y = abs(dimen[4])-1

file.seek(0)

def count_revisited_houses(start_x, start_y):
    count = 0
    for line in file:
        for c in line:
            if houses[start_x][start_y] != True:
                count = count + 1
            houses[start_x][start_y] = True
            if c == '>':
                start_x = start_x + 1
            if c == '<':
                start_x = start_x - 1
            if c == '^':
                start_y = start_y + 1
            if c == 'v':
                start_y = start_y - 1
    print(count)


def real_santa(real_x, real_y, c):
    print('real ', real_x, real_y)
    if c == '>':
        real_x = real_x + 1
    if c == '<':
        real_x = real_x - 1
    if c == '^':
        real_y = real_y + 1
    if c == 'v':
        real_y = real_y - 1
    if houses[real_x][real_y] != True:
        visited = 0
    else:
        visited = 1
    houses[real_x][real_y] = True
    return [real_x, real_y, visited]


def robo_santa(robo_x, robo_y, c):
    print('robo ', robo_x, robo_y)
    if c == '>':
        robo_x = robo_x + 1
    if c == '<':
        robo_x = robo_x - 1
    if c == '^':
        robo_y = robo_y + 1
    if c == 'v':
        robo_y = robo_y - 1
    if houses[robo_x][robo_y] != True:
        visited = 0
    else:
        visited = 1
    houses[robo_x][robo_y] = True
    return [robo_x, robo_y, visited]


def delivery_with_robo_santa(start_x, start_y):
    count = 0
    switch = True
    real_santa_position = [start_x, start_y]
    robo_santa_position = [start_x, start_y]
    for line in file:
        for c in line:
            if switch:
                move = real_santa(real_santa_position[0],
                                  real_santa_position[1], c)
                real_santa_position = [move[0], move[1]]
                count = count + move[2]
                switch = not switch
            else:
                move = robo_santa(robo_santa_position[0],
                                  robo_santa_position[1], c)
                robo_santa_position = [move[0], move[1]]
                count = count + move[2]
                switch = not switch
            print(count)

count_revisited_houses(start_x,start_y)
