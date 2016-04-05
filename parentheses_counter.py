input = open('parentheses.txt','r')
total = 0
count = 0
for line in input:
    for c in line:
        count = count + 1
        if c == '(':
            total = total + 1
        else:
            total = total - 1
        if total == -1:
            print(count)
            break
input.close()
