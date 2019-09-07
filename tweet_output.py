#format [last name, first name, gender, date]
import json
helptweets = []
nohelptweets = []

for line in open("help.txt", 'r', encoding = 'utf-8'):
        helptweets.append(line)
        
for line in open("nothelp.txt", 'r', encoding = 'utf-8'):
        nohelptweets.append(line)

if "\n" in helptweets[0]:
    helptweets[0] = helptweets[0].replace("\n", "")
#print(helptweets)
import csv
from random import randrange

print ("------------------------")
helptweets = helptweets[0].split("',")
for i in range(len(helptweets)):
    if "'" in helptweets[i]:
        helptweets[i] = helptweets[i].replace("'", "")
        #print("HEREEEE2")
        #print(helptweets[i])
    elif "\\n" in helptweets[i]:
        #print("HEREEEE")
        helptweets[i] = helptweets[i].replace("\\n", "")
    elif "\\\n" in helptweets[i]:
        #print("here")
        helptweets[i] = helptweets[i].replace("\\\n", "")
    elif helptweets[i][-1] == "n":
        helptweets[i] = helptweets[i][:-3]
        #print(helptweets[i])

print ("------------------------")
names_lst = []
with open('Common_Surnames_Census_2000.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count > 178:
            break
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        #print(f'\t{row["name"]} is the last name')
        entry = [helptweets[line_count], row["name"][0] + row["name"][1:].lower()]
        names_lst.append(entry)
        line_count += 1
    print(f'Processed {line_count} lines.')

last_names_set = set()
with open('SSA_Names_DB.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count > 178:
            break
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        #print(f'\t{row["Name"]} is the first name')
        line_count += 1
        last_names_set.add((row["Name"], row["Gender"]))
    print(f'Processed {line_count} lines.')

prev_month = "Oct"
for i in range(len(names_lst)):
    last_name, gender = last_names_set.pop()
    names_lst[i].append(last_name)
    names_lst[i].append(gender)
    if prev_month == "Oct":
        prev_month = "Nov"
        date = randrange(1, 29)
    else:
        prev_month = "Oct"
        date = randrange(22, 30)
    names_lst[i].append(str(date) + " " + prev_month + " " + "2012")


#print(names_lst)
print(len(helptweets))
fullList = []
print("--------------------")
for tweet in names_lst:
    d = dict()
    d["handle"] = tweet[2] + "_" + tweet[1]
    d["body"] = tweet[0]
    d["timestamp"] = tweet[4]
    fullList.append(d)
res = json.dumps(fullList)
print(res)


