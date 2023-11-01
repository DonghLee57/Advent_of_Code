# python3.x
with open('my_input.txt','r') as o:
    tmp = o.read()
signal = tmp[:-1]

# part 1
packet = []
for idx, char in enumerate(signal):
    #print(idx, char, packet)
    if len(packet) < 4:
        packet.append(char)
    elif len(packet) == 4:
        if len(list(set(packet))) == 4:
            print(idx, packet)
            break
        else:
            packet.append(char)
            del packet[0]

# part 2
packet = []
for idx, char in enumerate(signal):
    #print(idx, char, packet)
    if len(packet) < 14:
        packet.append(char)
    elif len(packet) == 14:
        if len(list(set(packet))) == 14:
            print(idx, packet)
            break
        else:
            packet.append(char)
            del packet[0]
