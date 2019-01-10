import apriori
import pandas as pd
import numpy as np
import time
import csv


def loadDataSet(path):
    if path == "data/kaggleData.csv":
        with open(path) as csvfile:
            reader =csv.reader(csvfile)
            data = [[row[1],row[2]] for row in reader]
        j = 1
        temp = []
        resData = []
        for i in range(len(data)):
            if data[i][0] == str(j):
                temp.append(data[i][1])
            else:
                resData.append(temp)
                temp = []
                temp.append(data[i][1])
                j += 1
    else:
        data = np.loadtxt(path, usecols=(1,2))
        np.set_printoptions(suppress=True)
        # print(data)
        j = 1
        temp = []
        resData = []
        for i in range(len(data)):
            if data[i][0] ==j:
                temp.append(str(int(data[i][1])))
            else:
                resData.append(temp)
                temp = []
                temp.append(str(int(data[i][1])))
                j += 1
    return resData


# path = "data/IBMdata0.1.txt"
# path = "data/IBMdata1.txt"
# path = "data/IBMdata10.txt"
path = "data/kaggleData.csv"


resData = loadDataSet(path)
    
start = time.time()
L, suppData = apriori.apriori(resData, minSupport=0.005)
# minSupport<0.05
rules = apriori.generateRules(L, suppData, minConf=0.9)
# minConf<4
end = time.time()
# print(rules)
# print('bbbbbbbbbbbbbbbb:', L)
# print("time: " , end - start)

# print('aaaaaaaaaaaaaaaaaaaaaaaaaaa:', suppData)




