import csv

def writecsv(datalist):
    with open('dat.csv','a', encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

def readcsv():
     with open('dat.csv', encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file writer
        data = list(fr)
     return data

data = readcsv()
print(data)

#data = ['ขนมเยลลี่',20,'7.00 น.']
#writecsv(data)