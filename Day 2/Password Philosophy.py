#Ready the data
input = open("Day 2\AoC_2_Input.txt", "r")
inputlines = []
for lines in input:
  inputlines.append(lines)

def find_pass():
  valids = 0
  for passstring in inputlines:
    #Parse Data
    firstpos = int(passstring.split(" ")[0].split("-")[0]) - 1
    secondpos = int(passstring.split(" ")[0].split("-")[1]) - 1
    letterreq = passstring.split(" ")[1][0]
    password = passstring.split(" ")[2] 

    if password[firstpos] == letterreq and password[secondpos] == letterreq:
      pass
    #Valid case
    elif password[firstpos] == letterreq or password[secondpos] == letterreq:
      valids += 1
    else:
      pass
    
  return(valids)

print(find_pass())