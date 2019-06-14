#Dishan Wickremasinghe
import os
import csv

election_data_csv = os.path.join('..','..','..','Resources','election_data.csv')
with open(election_data_csv, 'r', newline = '', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    data = {}
    for x in csvreader:
        if x[2] not in data.keys():
            data[x[2]] = 1
        else:
            data[x[2]] = data[x[2]] + 1

def totalvotes(dict1):
    total = 0
    for x, y in dict1.items():
        total = total + y
    return total

def dataprint(dict1):
    output = "Election Results\n--------------------------"
    total = totalvotes(dict1)
    output = output + "\nTotal Votes: " + str(total) + "\n--------------------------"
    winner = ''
    winnervotes = 0
    for x, y in dict1.items():
        output = output + "\n" + x + ": " + str(round((y/total)*100,2)) + "% (" + str(y) + ")"
        if y > winnervotes:
            winner = x
            winnervotes = y
    output = output + "\n--------------------------\nWinner: " + winner + "\n--------------------------"
    return output

# output of results to the terminal
print (dataprint(data))

# output of results to a text file in the folder
txtfile = open("output.txt","w")
txtfile.write(dataprint(data))
txtfile.close()