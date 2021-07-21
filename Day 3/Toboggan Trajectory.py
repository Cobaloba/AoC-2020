#Ready the data
f = open("Day 3\AoC_3_Input.txt")
fields = []
trees = 0
rightspeed = 3
tbx = 0
for lines in f:
    fields.append(lines)


for counter, field in enumerate(fields):
  #only land on even fields
  if counter % 2 == 0:
    #modulo as pattern repeats
    if field[tbx % 31] == "#":
      trees+=1
    tbx += rightspeed
    #for debugging - draw X at curent location in field
    field = field[:tbx % 31] + "X" + field[(tbx % 31) + 1:]
    print(field)
    

print(trees)
