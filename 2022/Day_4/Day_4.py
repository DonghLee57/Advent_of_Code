# python3.x
with open('my_input.txt','r') as o:
    tmp = o.readlines()

# part 1
count = 0
for i in range(len(tmp)):
    [a, b] = tmp[i].split(',')
    a = list(map(int,a.split('-')))
    b = list(map(int,b[:-1].split('-')))
    sign = (a[0] - b[0])*(a[1] - b[1])
    # Never overlap if (sign > 0)
    # Always fully overlap
    if sign <= 0:
        count += 1
print(count)

# part 2
count = 0
for i in range(len(tmp)):
    [a, b] = tmp[i].split(',')
    a = list(map(int,a.split('-')))
    b = list(map(int,b[:-1].split('-')))
    # Never overlap 
    if (a[0] > b[1]) or (b[0] > a[1]):
        count += 1
print(len(tmp) - count)
