def max_heap(list, index):
    largest = index
    left = 2*index
    right = 2*index+1
    if left <= len(list)-1 and list[left]>list[largest]:
        largest = left
    if right <= len(list)-1 and list[right] > list[largest]:
        largest = right
    if largest is not index:
        temp = list[index]
        list[index] = list[largest]
        list[largest] = temp
        return max_heap(list, largest)

def repr(list, index, indent=0):
    string = ""
    string = ('\t' * indent) + str(list[index-1]) + '\n'

    if len(list) >= index * 2:
        string += ('\t' * (indent+1)) + 'Left:\n'
        string += repr(list, index*2, indent+1)

    if len(list) >= index * 2 + 1:
        string += ('\t' * (indent+1)) + 'Right:\n'
        string += repr(list, index*2+1, indent+1)

    return string

list = [None, 3, 14, 7, 4, 8, 2, 1, 7, 6, 11, 9]
max_heap(list, 1)
print(list)
print(repr(list,1))
