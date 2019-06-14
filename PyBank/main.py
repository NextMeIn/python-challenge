#Dishan Wickremasinghe
import os
import csv

budget_data_csv = os.path.join('..','..','..','Resources','budget_data.csv')
month = []
value = []

with open(budget_data_csv,'r',newline='',encoding='utf-8') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
   
    for x in csvreader:
        month.append(x[0])
        value.append(int(x[1]))

def headings():
    return "\t\tFinancial Analysis\n----------------------------------------------------\n"

def noofmonths(list1):
    return("Total Months: " + str(len(list1)))

def total(list1):
    return "Total: $"+str(sum(list1))

def avgchange(list1):
    list2 = []
    for x in list1:
        if (list1.index(x)-1) > -1:
            list2.append(x - list1[list1.index(x)-1])
    return "Average Change : $" + str(round(sum(list2)/len(list2),2))

def greatestIncrement(list1,list2):
    return "Greatest Increment In Profits : " + str(list1[(list2.index(max(list2)))]) + " ($" + str(max(list2)) + ")"

def greatestDecrease(list1,list2):
    return "Greatest Decrease In Profits : " + str(list1[(list2.index(min(list2)))]) + " ($" + str(min(list2)) + ")"

# output of results to the terminal
print(headings())
print(noofmonths(month))
print(total(value))
print(avgchange(value))
print(greatestIncrement(month,value))
print(greatestDecrease(month,value))

# output of results to a text file in the folder
txtfile = open("output.txt","w")
txtfile.write(headings())
txtfile.write(noofmonths(month))
txtfile.write("\n"+total(value))
txtfile.write("\n"+avgchange(value))
txtfile.write("\n"+greatestIncrement(month,value))
txtfile.write("\n"+greatestDecrease(month,value))
txtfile.close()