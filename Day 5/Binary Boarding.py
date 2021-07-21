import math
#test ticket
test = "BFFFBBFRRR"
winnertkt = 0
allids = []

def SeatIdentifier(ticket):
    #initialise
    rows = []
    columns = []
    rowtxt = ticket[:7]
    columntxt = ticket[7:10]
    for rowseats in range(128):
        rows.append(rowseats)
    for columnseats in range(8):
        columns.append(columnseats)

    #Find row
    for i in rowtxt:
        splitpoint = math.ceil(len(rows)/2)
        if i == "F":
            for j in range(splitpoint,len(rows)):
                rows.pop()
        else:
            for j in range(0,splitpoint):
                rows.pop(0)
    
    #Find Column
    for i in columntxt:
        splitpoint = math.ceil(len(columns)/2)
        if i == "L":
            for j in range(splitpoint,len(columns)):
                columns.pop()
        else:
            for j in range(0,splitpoint):
                columns.pop(0)

    #return seat ID
    return(  (int(rows[0]) * 8) + columns[0]     )


data = open("Day 5\input.txt","r")
for ticketpool in data:
    curr = SeatIdentifier(ticketpool)
    allids.append(curr)

    if curr > winnertkt:
        print("Curr:" + str(curr))
        winnertkt = curr

print(winnertkt)
allids = sorted(allids)

lowest = allids[0]
for i in allids:
    if i > lowest:
        print("Seat missing: " + str(lowest)) 
        break
    lowest +=1
