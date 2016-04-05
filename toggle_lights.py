import re

file = open('light_instructions.txt', 'r')
lights = [[False for y in range(1000)] for x in range(1000)]

def go_through_file():
    for line in file:
        if line[6] is 'n':
            points = get_digits(line)
            point_one = [points[0], points[1]]
            point_two = [points[2], points[3]]
            go_through_points(point_one, point_two, 'on')
        elif line[6] is 'f':
            points = get_digits(line)
            point_one = [points[0], points[1]]
            point_two = [points[2], points[3]]
            go_through_points(point_one, point_two, 'off')
        elif line[6] is ' ':
            points = get_digits(line)
            point_one = [points[0], points[1]]
            point_two = [points[2], points[3]]
            go_through_points(point_one, point_two, 'toggle')
        else:
            print('error1')

def get_digits(line):
    digits = re.findall(r'\d+', line)
    return digits

def go_through_points(p1, p2, mode):
    for i in range(int(p1[0]), int(p2[0])+1):
        for j in range(int(p1[1]), int(p2[1])+1):
            if mode is 'on':
                if lights[i][j] is False:
                    lights[i][j] = True
            elif mode is 'off':
                if lights[i][j] is True:
                    lights[i][j] = False
            elif mode is 'toggle':
                if lights[i][j] is False:
                    lights[i][j] = True
                elif lights[i][j] is True:
                    lights[i][j] = False
            else:
                print('error2')

def count_lights():
    count = 0
    for i in range(0, len(lights)):
        for j in range(0, len(lights[i])):
            if lights[i][j] is True:
                count += 1
    return count

def count_lights_2():
    count = 0
    for i in range(0, len(lights)):
        count += lights[i].count(True)
    return count

go_through_file()
print(count_lights_2())
