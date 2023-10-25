# python3.x
with open('my_input.txt','r') as o:
    tmp = o.readlines()

def get_score(char):
    # Lowercase
    if char == char.lower():
        score = ord(char)-96
    # Uppercase
    elif char == char.upper():
        score = ord(char)-64+26
    # Bug?
    else:
        print(f"Check this character: {char}")
    return score

# part 1
def ext_char(string):
    NCHAR = len(string)
    MID = NCHAR//2
    left = string[:MID]
    right = string[MID:]
    for idx in range(len(left)):
        for jdx in range(len(right)):
            if left[idx] == right[jdx]:
                return left[idx]

SCORE = 0
for i in range(len(tmp)):
    char = ext_char(tmp[i])
    score= get_score(char)
    SCORE += score
print(SCORE)

# part 2
def ext_char2(a,b,c):
    common = []
    for idx in range(len(a)):
        for jdx in range(len(b)):
            if a[idx] == b[jdx]:
                common.append(a[idx])
    common = list(set(common))
    for idx in range(len(common)):
        for jdx in range(len(c)):
            if common[idx] == c[jdx]:
                return c[jdx]

SCORE = 0
NGR = len(tmp)//3
for n in range(NGR):
    [a,b,c] = tmp[n*3:(n+1)*3]
    char = ext_char2(a[:-1],b[:-1],c[:-1])
    score= get_score(char)
    SCORE += score
print(SCORE)
