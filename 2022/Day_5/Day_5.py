# python3.x
with open('my_input.txt','r') as o:
    tmp = o.readlines()

def initialization(input):
    size = 4
    cols = input[8].split()
    ncol = len(cols)
    stack = []
    for i in range(ncol): stack.append([])
    for i in range(8):
        for c in range(ncol):
            item = input[i][c*size+1]
            if item != ' ':
                stack[c].append(item)
    return stack, ncol

def get_order(COMMAND):
    items = COMMAND.split()
    NMOVE = int(items[1])
    FROM  = int(items[3])
    TO    = int(items[5])
    return NMOVE, FROM-1, TO-1

# part 1
stack, ncol = initialization(tmp)
for i in range(10,len(tmp)):
    N, f, t = get_order(tmp[i])
    for n in range(N):
        stack[t].insert(0,stack[f][0])
        del stack[f][0]
ans = ''
for i in range(ncol):
    ans += stack[i][0]
print(ans)

# part 2
stack, ncol = initialization(tmp)
for i in range(10,len(tmp)):
    N, f, t = get_order(tmp[i])
    for n in range(N):
        stack[t].insert(0, stack[f][(N-1)-n])
    del stack[f][0:N]
ans = ''
for i in range(ncol):
    ans += stack[i][0]
print(ans)
