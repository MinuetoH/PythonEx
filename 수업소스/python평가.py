# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:53:17 2022

@author: kimyh
"""

print("123456"[1:3])

mylist1=[1,2,3,4,5]

#mylist1 보다 각각의 요소가 10이 더많은 요소를 가진 mylist2 생성
mylist2=[] #11,12,13,14,15
#1 반복문
for n in mylist1 :
    mylist2.append(n+10)
print(mylist2)    

#2 컴프리헨션
mylist2=[n+10 for n in mylist1]
print(mylist2) 
   
#3 map 방식
#map(함수,리스트) : 리스트의 각 요소에 함수 적용
def add10(n) :
    return n+10

mylist2 = list(map(add10,mylist1))
print(mylist2)    

#4 map 람다방식 
mylist2 = list(map(lambda n:n+10,mylist1))
print(mylist2)    

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [11,12,13,14,15,16,17,18,19]

list1 = [x for x in range(1,10)]
list1
list2 = [x for x in range(11,20)]
list2

list3 = list(map(lambda x,y: x + y, list1, list2))
list3

def mean(x) :
    return sum(x)/len(x) if len(x)>0 else 0
print("평균:",mean(list3))

def median(x) :
    import numpy as np
    return np.median(x)
print("중간값:",median(list3))


def median(x) :
    median=0
    idx=0
    if len(x)%2==0 :
        idx=len(x)//2
        median=(x[idx-1]+x[idx])/2
    else :
        idx=len(x)//2
        median=x[idx]
    return median
print("중간값:",median(list3))

import math as m
def std1(x) : 
    mean = sum(x)/len(x)
    hap=0
    for i in x :
        hap += (i-mean) ** 2
    std=m.sqrt(hap/len(x))
    return std
c=list3
print("표준편차:",std1(c))



