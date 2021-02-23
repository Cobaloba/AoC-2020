import re

regpat = re.compile(r'(?<=[0-9] )(\w+ \w+)')
rawtxt = open("HandyHaversacks.txt","r").read()
rules = {}
count = 0

#create dictionary of rules
for line in rawtxt.split("\n"):
    rules[line.split(" ")[0] + " " + line.split(" ")[1]] = regpat.findall(line)

def Goldfinder(bag):
    if len(bag) == 0:
        return False
    for i in bag:
        if i == "shiny gold":
            return True
        else:
            temp  =Goldfinder(rules[i])
            if temp:
                return temp
             

for currbag in rules:
    if Goldfinder(rules[currbag]):
        count +=1
        print(currbag)

print(count)