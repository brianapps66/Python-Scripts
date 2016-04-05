from re import findall

ops = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'RSHIFT': lambda a, b: a >> b,
    'LSHIFT': lambda a, b: a << b,
    'NOT': lambda a: ~a
}


def evaluate(wire, wires):
    if wire.isdigit():
        print('int(wire): ', int(wire))
        return int(wire)

    if isinstance(wires[wire], int):
        print('wires[wire] 1: ', wires[wire])
        return wires[wire]

    tokens = findall("([^\s]+)", wires[wire])
    print('tokens: ', tokens)
    wires[wire] = {
        1: lambda a: evaluate(a, wires),
        2: lambda op, a: ops[op](evaluate(a, wires)),
        3: lambda a, op, b: ops[op](evaluate(a, wires), evaluate(b, wires))
    }[len(tokens)](*tokens)
    print('wires[wire] 2: ', wires[wire])

    return wires[wire]


def day7(string_input):
    wires = {k: v for v, k in findall("(.*) -> ([^\s]*)", string_input)}
    print('wires: ', wires)
    part1 = evaluate('a', wires.copy())
    wires['b'] = str(part1)
    part2 = evaluate('a', wires.copy())
    return part1, part2


file = open('bitwise_instructions.txt','r')
string = file.read()
file.close()
print(day7(string))
