# python3.x
with open('my_input.txt','r') as o: 
    tmp = o.read()

tmp = tmp.split('\n\n')

for i in range(len(tmp)):
    tmp[i] = sum(list(map(int,tmp[i].split())))

print(max(tmp))
