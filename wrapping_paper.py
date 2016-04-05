read = open('present_sizes.txt', 'r')

def get_paper_size(l, w, h):
    area = 2 * l * w + 2 * w * h + 2 * h * l
    dimen = [l, w, h]
    dimen.remove(max(dimen))
    extra = dimen[0] * dimen[1]
    return area + extra

def get_total_paper_needed():
    total = 0
    for line in read:
        lwh = 'l'
        length, width, height = '', '', ''
        for i in range(0, len(line)):
            if lwh == 'l':
                if line[i] != 'x':
                    length += line[i]
                else:
                    lwh = 'w'
                    continue
            if lwh == 'w':
                if line[i] != 'x':
                    width += line[i]
                else:
                    lwh = 'h'
                    continue
            if lwh == 'h':
                if line[i] != 'x' or '\n':
                    height += line[i]
                if i==len(line)-1:
                    lwh = 'l'
                    total += get_paper_size(int(length), int(width), int(height))
                    length, width, height = '', '', ''
    return total


def get_ribbon_length(l, w, h):
    dimen = [l, w, h]
    dimen.remove(max(dimen))
    perimeter = 2*dimen[0] + 2*dimen[1]
    bow = l*w*h
    return perimeter+bow

def get_total_ribbon_needed():
    total = 0
    for line in read:
        lwh = 'l'
        length, width, height = '', '', ''
        for i in range(0, len(line)):
            if lwh == 'l':
                if line[i] != 'x':
                    length += line[i]
                else:
                    lwh = 'w'
                    continue
            if lwh == 'w':
                if line[i] != 'x':
                    width += line[i]
                else:
                    lwh = 'h'
                    continue
            if lwh == 'h':
                if line[i] != 'x' or '\n':
                    height += line[i]
                if i==len(line)-1:
                    lwh = 'l'
                    total += get_ribbon_length(int(length), int(width),
                                           int(height))
                    length, width, height = '', '', ''
    return total

print(get_total_ribbon_needed())

read.close()
