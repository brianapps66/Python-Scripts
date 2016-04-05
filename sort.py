import math

def bubble_sort(list):
    length = len(list)
    for num in range(length-1,0, -1):
        for i in range(num):
            if list[i] > list[i+1]:
                swap(list, i, i+1)

def gnome_sort(l):
    i = 1
    while i < len(l):
        if (l[i] >= l[i-1]):
            i += 1
        else:
            swap(l,i, i-1)
            if i > 1:
                i-=1

def gnome_sort_optimised(l):
    i = 1
    last = 0
    while i < len(l):
        if (l[i] >= l[i-1]):
            if last is not 0:
                i = last
                last = 0
            i += 1
        else:
            swap(l,i, i-1)
            if i > 1:
                if last is 0:
                    last = i
                i-=1
            else:
                i+=1

def quick_sort_lomuto(l, low, high):
    if low < high:
        p = lomuto_partition(l, low, high)
        quick_sort_lomuto(l, low, p-1)
        quick_sort_lomuto(l, p+1, high)

def lomuto_partition(l, low, high):
    x = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= x:
            i+=1
            swap(l,i,j)
    swap(l,i+1,high)
    return i+1

def quick_sort_hoare(l, low, high):
    if low < high:
        p = hoare_partition(l,low, high)
        quick_sort_hoare(l, low, p-1)
        quick_sort_hoare(l, p+1, high)

def hoare_partition(l, low, high):
    x = l[low]
    i = low - 1
    j = high + 1
    while True:
        j -= 1
        while l[j] > x:
            j -= 1
        i += 1
        while l[i] < x:
            i += 1
        if i < j:
            swap(l, i, j)
        else:
            return j

def cocktail_sort(list):
    swapped = False
    while not swapped:
        for i in range(0, len(list)-2):
            if list[i] > list[i+1]:
                swap(list,i,i+1)
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(len(list)-2,0,-1):
            if list[i] > list[i+1]:
                swap(list, i, i+1)

def cocktail_sort_improved(list):
    begin = -2
    end = len(list) - 1
    swapped = True
    while swapped:
        begin+=1
        for i in range(begin, end):
            if list[i] > list[i+1]:
                swap(list,i,i+1)
                swapped = True
        if swapped is False:
            break
        swapped = False
        end-=1
        for i in range(end, begin, -1):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                swapped = True

def odd_even_sort(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(list)-1, 2):
            if list[i] > list[i+1]:
                swap(list,i,i+1)
                sorted = False
        for i in range(0,len(list)-1, 2):
            if list[i] > list[i+1]:
                swap(list,i,i+1)
                sorted = False

def comb_sort(list):
    gap = len(list)
    shrink = 1.3
    swapped = False
    while gap is not 1 or swapped is not False:
        gap = int(gap/shrink)
        if gap < 1:
            gap = 1
        i = 0
        swapped = False
        while i+gap < len(list):
            if list[i] > list[i+gap]:
                swap(list,i,i+gap)
                swapped = True
            i+=1

def stooge(l):
    return stooge_sort(l, 0, len(l)-1)

def stooge_sort(l, low, high):
    if l[high] < l[low]:
        swap(l,low,high)
    if (high-low) > 1:
        t = (high-low+1) // 3
        stooge_sort(l, low, high-t)
        stooge_sort(l, low+t, high)
        stooge_sort(l, low, high-t)
    return l

def bingo_sort(l):
    max = len(l)-1
    nextElem = l[max]
    for i in range(max-1,-1,-1):
        if l[i] > nextElem:
            nextElem = l[i]
    while max > 0 and l[max] is nextElem:
        max -= 1

    while max > 0:
        curr = nextElem
        nextElem = l[max]
        for i in range(max-1,-1,-1):
            if l[i] is curr:
                swap(l,i,max)
                max -= 1
            elif l[i] > nextElem:
                nextElem = l[i]
        while max > 0 and l[max] is nextElem:
            max -= 1

def selection_sort(l):
    for i in range(0,len(l)-1):
        min = i
        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                min = j
        if min is not i:
            swap(l,i,min)

def heap_sort(l):
    end = len(l) - 1
    heapify(l)
    while end > 0:
        swap(l,end,0)
        end -= 1
        siftDown(l,0, end)

def heap_parent(i):
    return math.floor((i-1)/2)

def heap_left(i):
    return 2*i +1

def heap_right(i):
    return 2*i +2

def heapify(l):
    start = heap_parent(len(l)-1)
    while start >= 0:
        siftDown(l, start, len(l)-1)
        start -= 1

def siftDown(l,start, end):
    root = start
    while heap_left(root) <= end:
        child = heap_left(root)
        temp = root
        if l[temp] < l[child]:
            temp = child
        if child+1 <= end and l[temp]< l[child+1]:
            temp = child+1
        if temp is root:
            return
        else:
            swap(l, root, temp)
            root = temp

def bottom_up_heap_sort(l):
    bottom_up_heapify(l)
    end = len(l)-1
    while end > 0:
        swap(l,end,0)
        end -=1
        bottom_up_sift_down(l,end,0)

def bottom_up_heapify(l):
    start = heap_parent(len(l)-1)
    while start >= 0:
        bottom_up_sift_down(l, len(l)-1, start)
        start -= 1

def leafSearch(l, end, i):
    while heap_left(i) <= end:
        if heap_right(i) <= end and l[heap_right(i)] > l[heap_left(i)]:
            i = heap_right(i)
        else:
            i = heap_left(i)
    return i

def bottom_up_sift_down(l, end, i):
    j = leafSearch(l, end, i)
    while l[i] > l[j]:
        j = heap_parent(j)
    temp = l[j]
    l[j] = l[i]
    while j>i:
        temp, l[heap_parent(j)] = l[heap_parent(j)], temp
        j = heap_parent(j)

def cycle_sort(l):
    writes = 0
    for i in range(0,len(l)-1):
        item = l[i]
        p = i
        for j in range(i+1,len(l)):
            if l[j] < item:
                p +=1
        if p is i:
            continue
        while item is l[p]:
            p += 1
        l[p],item = item, l[p]
        writes +=1
        while p is not i:
            p = i
            for j in range(i+1, len(l)):
                if l[j] < item:
                    p += 1
            while item is l[p]:
                p += 1
            l[p],item = item, l[p]
            writes += 1

def insertion_sort(l):
    for i in range(0,len(l)):
        while i>0 and l[i-1]>l[i]:
            swap(l,i,i-1)
            i -=1

def shell_sort(l):
    gaps = [10, 4, 1]
    for gap in gaps:
        for i in range(gap,len(l)):
            temp = l[i]
            for j in range(i,gap-2, -gap):
                if l[j-gap] <= temp-1:
                    break
                l[j] = l[j-gap]

            l[j] = temp
            print(l)

def radix_sort(l, base):
    passes = int(round(math.log(maxAbs(l),base))+1)
    new_l = list(l)
    for digit in range(passes):
        new_l = merge(split(new_l, base, digit))
    return merge(split_by_sign(new_l))

def split_by_sign(l):
    buckets = [[],[]]
    for i in l:
        if i<0:
            buckets[0].append(i)
        else:
            buckets[1].append(i)
    return buckets

def maxAbs(l):
    return max(abs(i) for i in l)

def merge(l):
    new_l = []
    for sub in l:
        new_l.extend(sub)
    return new_l

def split(l,base,i):
    buckets = make_blanks(base)
    for j in l:
        buckets[get_digit(j, base, i)].append(j)
    return buckets

def make_blanks(size):
    return [[] for i in range(size)]

def get_digit(num, base, i):
    return (num//base ** i)%base

def insertion_sort_improved(l):
    for i in range(0,len(l)):
        x = l[i]
        while i > 0 and l[i-1] > x:
            l[i] = l[i-1]
            i -= 1
        l[i] = x

def odd_even_merge(x, y, s):
    step = s*2
    if step < y - x:
        yield from odd_even_merge(x, y, step)
        yield from odd_even_merge(x + s, y, step)
        yield from [(i, i + s) for i in range(x+s, y-s, step)]
    else:
        yield (x, x+s)

def odd_even_merge_sort_range(x, y):
    if (y - x) >= 1:
        midpoint = x + ((y-x)//2)
        yield from odd_even_merge_sort_range(x, midpoint)
        yield from odd_even_merge_sort_range(midpoint+1, y)
        yield from odd_even_merge(x, y, 1)

def odd_even_merge_sort_pairs(length):
    yield from odd_even_merge_sort_range(0, length-1)

def odd_even_swap(list, a, b):
    if list[a] > list[b]:
        swap(list,a, b)

def odd_even_merge_sort(l):
    pairs = list(odd_even_merge_sort_pairs(len(l)))
    for i in pairs:
        odd_even_swap(l, *i)

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def swap2(a,b):
    a,b = b,a

l = [3, 10, 13, 5, 6, 14, 7, 16, 2, 4, 15, 12, 1, 9, 8, 11]
print(l)
shell_sort(l)
print(l)
