inputfile = open("customs.txt","r")
groups = inputfile.read().split("\n\n")
print(groups[0])
sum = 0

for group in groups:
    answers = {}
    for individual in group.split("\n"):
        for individualanswers in individual:
            try:
                answers[individualanswers] += 1
            except:
                answers[individualanswers] = 1
    for talliednaswers in answers:
        #value equals length of group,sum =+1
        if answers[talliednaswers] == len(group.split("\n")):
            sum += 1

print(str(sum))

