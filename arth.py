# Enter your code here. Read input from STDIN. Print output to STDOUT

### NOTES ###
# This method assumes no order of operations, which might be the reason it failing some test
# Question should specify that is what they want, otherwise because it is just as safe to assume
# that there is reverse polish notation as well
# def main():
#    s = raw_input()
#    l = len(s)
#    i = x = num = 0
#    op = '+'
#    while i < l:
#        if s[i].isdigit():
#            num, i = consume_number(i, s)
#            if op is not None:
#                x = operate(x, op , num)
#                op = None
#        else:
#            op = s[i]
#            i += 1
#    print ('%f' % x).rstrip('0').rstrip('.')


def consume_number(start, string):
    j = start
    num = 0
    if j >= len(string):
        return 0, start
    
    while string[j].isdigit():
        num *= 10
        num += int(string[j])
        j +=1
        if j >= len(string):
            break
    return num, j

def operate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return float(a) / b
    elif op == '*':
        return a * b

def consume_md(ops):
    l = len(ops)
    if l < 3:
        return ops
    x = 1
    while x < (l-1):
        c = ops[x]
        if c == '/' or c == '*':
            ops = consume_md( ops[:(x-1)] + [operate(ops[x-1], c, ops[x+1])] + ops[(x+2):] )
            l = len(ops)
        else:
            x += 1
    return ops

def consume_as(ops):
    l = len(ops)
    if l < 3:
        return ops
    x = 1
    while x < (l-1):
        c = ops[x]
        ops = consume_md( ops[:(x-1)] + [operate(ops[x-1], c, ops[x+1])] + ops[(x+2):] )
        l = len(ops)
    return ops
    
def main(inp):
    s = inp
    l = len(s)
    i = x = num = 0
    operations = []
    while i < l:
        if s[i].isdigit():
            num, i = consume_number(i, s)
            operations.append(num)
        else:
            operations.append(s[i])
            i += 1
    print consume_as(consume_md(operations))
    #print ('%f' % x).rstrip('0').rstrip('.')
inp = "5*6/3+1"
main(inp)