
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Find all of rows
pos_row1_combos = []
pos_row2_combos = []
pos_row3_combos = []
pos_row4_combos = []

for i in x:
    temp1 = list(x)
    temp1.remove(i)
    for j in temp1:
        temp2 = list(temp1)
        temp2.remove(j)
        for k in temp2:
            temp3 = list(temp2)
            temp3.remove(k)
            for l in temp3:
                if i + j - k - l == 5:
                    ans = [i, j, k, l]
                    pos_row1_combos.append(ans)
                if i + j + k - l == 10:
                    ans = [i, j, k, l]
                    pos_row2_combos.append(ans)
                if i - j + k + l == 9:
                    ans = [i, j, k, l]
                    pos_row3_combos.append(ans)
                if i - j + k - l == 0:
                    ans = [i, j, k, l]
                    pos_row4_combos.append(ans)

print(len(pos_row1_combos)) # 1536
#print(pos_row1_combos)
print(len(pos_row2_combos)) # 1446
#print(pos_row2_combos)
print(len(pos_row3_combos)) # 1302
#print(pos_row3_combos)
print(len(pos_row4_combos)) # 2016
#print(pos_row4_combos)

print("starting")
ite = 0
workingCombs = []
for combo1 in pos_row1_combos:
    for combo2 in pos_row2_combos:
        s1 = set(combo1)
        s2 = set(combo2)
        if not set.intersection(s1, s2):
            s1s2 = set(combo1+combo2)
            for combo3 in pos_row3_combos:
                s3 = set(combo3)
                if not set.intersection(s1s2,s3):
                    s1s2s3 = set(combo1+combo2+combo3)
                    for combo4 in pos_row4_combos:
                        s4 = set(combo4)
                        if not set.intersection(s1s2s3,s4):
                            if combo1[0] + combo2[0] + combo3[0] - combo4[0] == 17:
                                if combo1[1] + combo2[1] - combo3[1] - combo4[1] == 8:
                                    if combo1[2] - combo2[2] - combo3[2] + combo4[2] == 11:
                                        if combo1[3] + combo2[3] + combo3[3] + combo4[3] == 48:
                                            ans = [combo1 + combo2 + combo3 + combo4]
                                            print(ans)
                                            workingCombs.append(ans)
    print(ite)
    ite = ite + 1


print("------------------------------------FINISHED ----------------------------")
print(workingCombs)
print(len(workingCombs))
