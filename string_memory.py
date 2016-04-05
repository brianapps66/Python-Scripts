import re

file = open('string_memory_input.txt', 'r').read().splitlines()
#file2 = open('string_memory_input.txt', 'r')
#result = ''
#string_input = file2.read()
#file2.
#file.close()

#print(string_input[:80])
def main(input_file_string):

    count = 0
    input_file_iter = iter(range(1,len(input_file_string)-1))
    for i in input_file_iter:
        if not re.match(r'\s', input_file_string[i]):
            if is_end_of_line(input_file_string,i):
                next(input_file_iter)
                next(input_file_iter)
                continue
            if input_file_string[i] == '\\' and input_file_string[i + 1] == '\\':
                print('Found \\')
                next(input_file_iter)
                continue
            if input_file_string[i] == '\\' and input_file_string[i + 1] == '\"':
                print('Found \"')
                next(input_file_iter)
                continue
            if input_file_string[i] == '\\' and input_file_string[i+1] == 'x' and re.match(r'[\da-f]',input_file_string[i+2]) and re.match(r'[\da-f]',input_file_string[i+3]):
                print('Found hex')
                next(input_file_iter)
                next(input_file_iter)
                next(input_file_iter)
                continue
            print(input_file_string[i])
            count+=1
            if i > 20:
                break
    return count

def is_backslash(input_file,i):
    if input_file[i] == '\\' and input_file[i + 1] == '\\':
        return True
    else:
        return False

def is_inverted_commas(input_file,i):
    if input_file[i] == '\\' and input_file[i + 1] == '\"':
        return True
    else:
        return False

def is_hex(input_file,i):
    if input_file[i] == '\\' and input_file[i+1] == 'x' and re.match(r'[\da-f]',input_file[i+2]) and re.match(r'[\da-f]',input_file[i+3]):
        return True
    else:
        return False

def is_end_of_line(input_file,i):
    if (input_file[i] == '\"' and input_file[i+1] == '\n') or (input_file[i]
        =='\"' and input_file[i-1] == '\n'):
        return True
    else:
        return False

def to_hex(match):
    print(match)
    return '||||||'+match+'||||||||'

def main2(input_file, result=''):
    count = 0
    for line in input_file:
        line = str(line)

        print(line)
        whitespace = re.sub(r'\s','',line,re.MULTILINE)
        print(whitespace)
        count += len(whitespace)
        first_comma = re.sub(r'^\"','',whitespace)
        second_comma = re.sub(r'\"$','',first_comma)
        backslash = re.sub(r'\\\\',r'\\',second_comma)
        inverted_commas = re.sub(r'\\\"','"',backslash)
        hex_dec = re.sub(r'\\x([\da-f]{2})',lambda x: chr(int(x.group(1),16)),
                         inverted_commas)
        print(hex_dec)
        result += hex_dec
    print('count: ',count,' len(result): ',len(result))
    return count - len(result)

def main3(file):
    return sum(len(line) for line in file) - sum(len(eval(line)) for line
                                                  in file)

def main4(file):
    return sum(len('"%s"' % line.replace('\\','\\\\').replace('"', '\\"'))
               for line in file) - sum(len(line) for line in file)

print(main4(file))
