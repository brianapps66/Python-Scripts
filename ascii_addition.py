string = input('Enter a string:')
total = 0
for letter in string:
    total += ord(letter)
print(total)
