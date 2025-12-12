from itertools import product

#Rating of Difficulty: 4/10 (bcuz of part c >:( )
# Q1 Coloured Triangle
row = input()
temp = ""
while len(row) != 1:
 for x in range(len(row)-1):
    if row[x] == row[x+1]:
        temp += row[x]
    if (row[x] == "G" and row[x+1] == "B") or (row[x] == "B" and row[x+1] == "G"):
        temp += "R"
    if (row[x] == "R" and row[x+1] == "G") or (row[x] == "G" and row[x+1] == "R"):
        temp += "B"
    if (row[x] == "R" and row[x+1] == "B") or (row[x] == "B" and row[x+1] == "R"):
        temp += "G"
 row = temp
 temp = ""
  
print(row)
#1 (b) RRRBBGGRG, GBGGRRBBB, BGBRGBRGR 3 combos
# 1 (c) 3^x + 1
# 1 (d) 10 


colours = "RGB"
combos = product(colours, repeat = 9)
count = 0
for i in combos:
    perm = "".join(i)
    row = perm
    temp = ""
    for x in range(len(row)-1):
        if row[x] == row[x+1]:
          temp += row[x]
        if (row[x] == "G" and row[x+1] == "B") or (row[x] == "B" and row[x+1] == "G"):
           temp += "R"
        if (row[x] == "R" and row[x+1] == "G") or (row[x] == "G" and row[x+1] == "R"):
           temp += "B"
        if (row[x] == "R" and row[x+1] == "B") or (row[x] == "B" and row[x+1] == "R"):
           temp += "G"
    if temp == "RRGBRGBB":
       count += 1
       print(row)
print(count)
