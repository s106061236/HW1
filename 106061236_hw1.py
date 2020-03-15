# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061236.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data
length = len(data)

num_C0A880 = 0
num_C0F9A0 = 0
num_C0G640 = 0
num_C0R190 = 0
num_C0X260 = 0

temp_C0A880 = 0
temp_C0F9A0 = 0
temp_C0G640 = 0
temp_C0R190 = 0
temp_C0X260 = 0

#remove -99 & -999 PRES data
for i in range(length):
    if data[length-i-1]["PRES"] == '-99.000':
        del data[length-i-1]
    elif data[length-i-1]["PRES"] == '-999.000':
        del data[length-i-1]

#count the value
for i in range(len(data)):
    if data[i]["station_id"] =='C0A880':
        temp_C0A880 = temp_C0A880 + float(data[i]["PRES"])
        num_C0A880 = num_C0A880+1
   
    if data[i]["station_id"] =='C0F9A0':
        temp_C0F9A0 = temp_C0F9A0 + float(data[i]["PRES"])
        num_C0F9A0 = num_C0F9A0+1
       
    if data[i]["station_id"] =='C0G640':
        temp_C0G640 = temp_C0G640 + float(data[i]["PRES"])
        num_C0G640 = num_C0G640+1
   
    if data[i]["station_id"] =='C0R190':
        temp_C0R190 = temp_C0R190 + float(data[i]["PRES"])
        num_C0R190 = num_C0R190+1
   
    if data[i]["station_id"] =='C0X260':
        temp_C0X260 = temp_C0X260 + float(data[i]["PRES"])
        num_C0X260 = num_C0X260+1

#=======================================

# Part. 4
#=======================================
# Print result
if num_C0A880 == 0:
    print("C0A880,None")
else:
    print("C0A880",(temp_C0A880/num_C0A880))

if num_C0F9A0 == 0:
    print("C0F9A0,None")
else:
    print("C0F9A0",(temp_C0F9A0/num_C0F9A0))
   
if num_C0G640 == 0:
    print("C0G640,None")
else:
    print("C0G640",(temp_C0G640/num_C0G640))
   
if num_C0R190 == 0:
    print("C0R190,None")
else:
    print("C0R190",(temp_C0R190/num_C0R190))
   
if num_C0X260 == 0:
    print("C0X260 None")
else:
    print("C0X260",(temp_C0X260/num_C0X260))
#=======================================