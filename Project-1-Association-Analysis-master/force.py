# -*- coding: utf-8 -*-
import numpy as np
import csv
import time

'''
dataset：
IBM data 01：-ntrans 0.1 -tlen 10	1000筆數據 事物數為10
IBM data 02：-ntrans 1 -tlen 10		10000筆數據 事物數為10
IBM data 03：-ntrans 10 -tlen 10	100000筆數據 事物數為10
Kaggle data: 統計某大型公司各工作人員所用的編程語言，選取其中一部分轉換成IBM生成的格式約11000筆左右，統計了該公司10種目前階段最受歡迎的編程語言。

暴力法:
找出所有可能的候選 patterns，將找出的 patterns 和全部 datasets 進行比比較並且統計數量，如果dataset的计数大於min support，則這個pattern 是合法的的frequent itemset。
'''

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
        print(data)
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

def findFreItemSets(data):
    L = []
    for itemsets in data:
        for item in itemsets:
            if not [item] in L:
                L.append([item]) 
    L.sort()                     
    # print(L1)
    findItemsets = [L]      
    for i in range(0, len(L)-1):
        findItemsets.append([])         
        for j in findItemsets[i]:
            for item in L:
                lis = []
                lis = list([j]) if type(j) is int else j.copy()
                if item[-1] > lis[-1]:
                    lis.append(item[-1])
                    findItemsets[i+1].append(lis) 
    return findItemsets

def findFnlFreItemsets(data, findItemsets, minSupport):
    num = len(data)
    freItemSets = []
    for k in findItemsets:
        for m in k:
            count = 0
            for tranSet in data:
                if [element for element in m if element in tranSet] == m:
                    count += 1
            if count/num >= minSupport:
                freItemSets.append(m)
    return freItemSets

# path = "data/IBMdata0.1.txt"
# path = "data/IBMdata1.txt"
# path = "data/IBMdata10.txt"
path = "data/kaggleData.csv"

data = loadDataSet(path)
# print(data)
startTime = time.time()
findItemsets = findFreItemSets(data)
freItemSets = findFnlFreItemsets(data, findItemsets, minSupport = 0.7)
endTime = time.time()
print('frequent itemsets : ', freItemSets)
# print('time:', endTime - startTime)