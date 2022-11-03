import csv

### Question 1 part (i) ###
mylist = []
with open('lab_11_data.csv') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        mylist.append(row[0:7])

### Question 1 part (ii) ###

templist = mylist
del mylist[0] #Remove header row

func = lambda x: True if float(x[-1]) > -3.0 else False
mylist2 = list(filter(func, mylist))

### Question 1 part (iii) ###
avglist = list()
listofavg = []
res = list()
func2 = lambda avglist: sum(avglist)/len(avglist)
for j in range (1,4):
    for i in mylist2:
        i[j] = i[j].replace(",", "")
        avglist.append(float(i[j]))
    listofavg.append(avglist.copy())
    avglist.clear()
res = list(map(func2,listofavg))

f = open('avg_output.txt', 'w')
for i in res:
    f.write(str(i)+"\n")
f.close()


### Question 1 part (iv) ###

feature_list = []
inp = input("Given character A-Z: ")
for i in mylist2:
    if(i[0][0] == inp.upper()):
        feature_list.append(i)

final_list = []
f = open("stock_output.txt", "w")
for i in feature_list:
    for j in i:
        f.write(str(j)+",")
    f.write("\n")
f.close()



