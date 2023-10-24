# python3.x
with open('my_input.txt','r') as o:
    tmp = o.readlines()

sym_dict = {'A':'Rock',
            'B':'Paper',
            'C':'Scissors',
            'X':'Rock',
            'Y':'Paper',
            'Z':'Scissors'}
score_dict = {'Rock':1, 'Paper':2, 'Scissors':3}
rps_list = ['Rock','Paper','Scissors']

# part 1
total_score = 0
for i in range(len(tmp)):
    line = tmp[i].split()
    opp = sym_dict[line[0]]
    my  = sym_dict[line[1]]
    # Win
    if rps_list[rps_list.index(my) - 1] == rps_list[rps_list.index(opp)]:
        score = score_dict[my] + 6
    # Draw
    elif opp == my:
        score = score_dict[my] + 3
    # Lose
    elif rps_list[rps_list.index(my)] == rps_list[rps_list.index(opp) - 1]:
        score = score_dict[my]
    total_score += score
print(total_score)
    
# part 2
total_score = 0
for i in range(len(tmp)):
    line = tmp[i].split()
    opp = sym_dict[line[0]]
    my  = line[1]

    # Lose
    if my == 'X':
        my = rps_list[rps_list.index(opp)-1]
        score = score_dict[my]
    # Draw
    elif my == 'Y':
        my = rps_list[rps_list.index(opp)]
        score = score_dict[my]+3
    # Win
    elif my == 'Z':
        my = rps_list[(rps_list.index(opp)+1)%3]
        score = score_dict[my]+6
    total_score += score
print(total_score)
