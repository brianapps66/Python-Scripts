import re

file = open('light_instructions.txt', 'r')
lights = [[0 for y in range(1000)] for x in range(1000)]

def go_through_file():
    for line in file:
        if line[6] is 'n':
            points = get_digits(line)
            point_one = [points[0],points[1]]
            point_two = [points[2],points[3]]
            change_brightness(point_one,point_two,'on')
        if line[6] is 'f':
            points = get_digits(line)
            point_one = [points[0],points[1]]
            point_two = [points[2],points[3]]
            change_brightness(point_one,point_two,'off')
        if line[6] is ' ':
            points = get_digits(line)
            point_one = [points[0],points[1]]
            point_two = [points[2],points[3]]
            change_brightness(point_one,point_two,'toggle')

def get_digits(line):
    digits = re.findall(r'\d+', line)
    return digits

def change_brightness(p1,p2,mode):
    for i in range(int(p1[0]),int(p2[0])+1):
        for j in range(int(p1[1]),int(p2[1])+1):
            if mode is 'on':
                lights[i][j] += 1
            if mode is 'off':
                if lights[i][j] > 0:
                    lights[i][j] -=1
            if mode is 'toggle':
                lights[i][j] += 2

def get_total_brightness():
    count = 0
    for i in range(0,len(lights)):
        for j in range(0,len(lights[i])):
            count += lights[i][j]
    return count

go_through_file()
print(get_total_brightness())
