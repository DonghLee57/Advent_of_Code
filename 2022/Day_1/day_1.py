# python3.x
with open('my_input.txt','r') as o: 
    tmp = o.read()

tmp = tmp.split('\n\n')

for i in range(len(tmp)):
    tmp[i] = sum(list(map(int,tmp[i].split())))

# part 1
print(max(tmp))

# part 2
tmp.sort()
print(sum(tmp[-3:]))
