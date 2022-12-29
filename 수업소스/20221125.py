# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:34:37 2022

@author: kimyh
"""



'''
   print(값) : 화면에 출력하기
   print(값1,값2) : 값을 여러개 출력
   print("{0:d}{1:2d}...".format(값1,값2,...))  형식문자 이용하여 출력
   print("%2d,%3d" % (값1,값2)) : 형식문자 이용하여 값을 여러개 출력
   print(f"{변수1} {변수2}") : 변수에 해당하는 값을 출력
   print(""" 문자열 """) : 여러줄 문자열
   
   문자열 : 문자들의 모임. 인덱스(첨자)를 사용가능
   "문자열"[시작인덱스:종료인덱스+1:증감값]
      시작인덱스 생략시 : 0번부터시작
      종료인덱스 생략시 : 마지막문자까지
      증감값 생략시 : 1씩 증가 
      
   조건문 : if else, if elif else , True if 조건식 else False   
   반복문 : for 변수 in 범위 , while 조건식  
           범위 : range(초기값,종료값+1,증감식)
           break,continue
   조건문,반복문 : 들여쓰기에 주의.         
   
   문자열 함수
     len(문자열) : 문자열의 길이
     문자열.count(문자) : 문자열에서 문자의 갯수 리턴
     문자열.find(문자) : 문자열에서 문자의 위치 리턴  문자가 없는 경우 -1 리턴
     문자열.index(문자) : 문자열에서 문자의 위치 리턴 문자가 없는 경우 오류 발생
     문자열.isdigit() : 숫자?
     문자열.isalpha() : 문자?
     문자열.isalnum() : 숫자또는문자?
     문자열.isupper() : 대문자?
     문자열.islower() : 소문자?
     문자열.isspace() : 공백 ?
'''

###################
# Collection : 여러개의 데이터 저장할 수 있는 객체
# List(리스트) : 배열의 행태. 인덱스사용가능. []로 표시함.
# tuple(튜플) : 상수화된 리스트. 변경불가리스트. ()로 표시함.
# set(셋) : 중복불가. 집합 []로 표시함
# dictionnary(딕셔너리) : 자바의 map. (key, value)쌍인 객체를 {}로 표시함
###################
#리스트
a = [0,0,0,0]
b = []
print(a,len(a))  #len(a) : 리스트 요소의 갯수
print(b, len(b))
# a 리스트의 길이만큼 숫자를 입력받아, a에 저장하고, 입력받은 수의 합계 출력하기
# 전체 합계를 출력하기
hap = 0
for i in range(len(a)) :
    a[i] = int(input(str(i+1)+'번째 숫자 입력: '))
    hap += a[i]
print(a,"요소의 합:",hap)
print(a,"요소의 합:",sum(a))

# a 리스트의 길이만큼 숫자를 입력받아,
# b에 저장하고, 입력받은 수의 합계 출력하기
for i in range(len(a)) :  #i : 0~2
#   b 리스트 요소는 없으므로 0번 인덱스에 해당하는 b[0]은 없다.
#   b[i] : int(input(str(i+1)+'번째 숫자 입력: ')) : 오류발생
#   b.append : b 리스트에 요소를 추가.
    b.append(int(input(str(i+1)+'번째 숫자 입력: ')))
print(b,"요소의 합:",sum(b))
print("b=%s" % b)
a.append(1)
a
# a 리스트 정렬
a.sort()
a
# a 리스트의 마지막 요소 출력하기
a[4]         # a 리스트의 4변 인덱스
a[len(a)-1]  # a 리스트의 마지막 인덱스
a[-1]        # 뒤에서 첫번째 인덱스 마지막 인덱스
a[-2]        # 뒤에서 두번째 인덱스 

a.pop()  # 마지막 요소를 제거하여 출력
a  #[1, 100, 200, 300]

a.reverse() #요소의 순서를 역순으로
a
#index() 함수 : 요소의 위치 리턴
a.index(100)  #2
a.index(400)  #값이 없는 경우 오류 발생
#a.find(400)   #함수오류. find 함수는 리스트에 없는 함수

# insert(인덱스, 값) : 리스트 중간에 요소를 추가
a
a.insert(1, 222)
a
# remove(값) : 해당 요소를 제거
a.remove(222)
a
# a 리스트에 b 리스트 추가
a.extend(b)
a
# 10 요소의 갯수 출력하기
a.count(10)

# 문자열을 분리하여 리스트로 저장하기
dd = "2022/11/25"
c = dd.split("/")
print(c)

# 문제 : ss 문자열의 모든 숫자들의 합을 출력하기
ss = "10,20,50,60,30,40,50,60,30"
sslist = ss.split(",")
sum(sslist)  #sslist 요소가 숫자아니가 고 문자열이므로 sum 사용불가
hap = 0
for n in sslist :
    hap += int(n)  #n의 값을 정수형 형변환
print(sslist,"의 요소의 합:",hap)

# map 함수 : 리스트의 요소에 적용함수를 설정
print(sslist,"의 요소의 합:",sum(list(map(int,sslist))))
# map(함수이름, 리스트) : 리스트의 요소들마다 함수 적용
# map(int, sslist) : sslist의 모든 요소들이 int 함수 적용
#                    하여 요소들의 자료형이 정수형으로 변환
# list 함수 : 리스트로 변환
mlist = list(map(int,sslist))
mlist
sum(mlist)

######## dictionnaty : {key1:value1,key2:value2,...}
score_dic = {'lee':100,'hong':70,'kim':90}
print(score_dic)
print(type(score_dic))
# hong의 점수 출력하기
# value <= dict['key']
score_dic['hong']
# hong의 점수 75점으로 수정하기
score_dic['hong'] = 75
print(score_dic)
# park의 점수 80점으로 추가하기
score_dic['park'] = 80
print(score_dic)

# park의 정보 제거하기
del score_dic['park']
print(score_dic)

# 키값만 조회
print(score_dic.keys())
print(list(score_dic.keys()))
# 값들만 조회
print(score_dic.values())
print(list(score_dic.values()))
# 키와 값들의 쌍인 값으로 조회
print(score_dic.items())
print(list(score_dic.items()))
# dictionnary 객체들을 반복문으로 조회
for n in score_dic :
    #n : key값
    print(n,"=",score_dic[n])
    
for n in score_dic.keys() :
    #n : key값
    print(n,"=",score_dic[n])
    
for n,s in score_dic.items() :
    #n:key값
    #s:value값
    print(n,"=",s)
    
for v in score_dic.items() :
    #v : 튜vmf객체.(k,v)쌍인 객체
    print(v[0],"=",v[1])
    print(v)

for s in score_dic.values() :
    print(s)  #key값을 조회 못함.
    
'''
문제 : 1. 궁합음식의 키를 입력받아 해당되는 음식을 출력하기
         등록안된 경우 오류 발생. => 등록여부 판단필요
       2.종료 입력시 등록된 내용 출력하기
         등록된음식 :
              떡볶이 : 오뎅
              짜장면 : 단무지
       3. 등록이 안된경우 
          등록여부를 입력받아, 등록하는 경우 궁합음식을 입력받기  
          등록하시겠습니까(y)? 
             y입력 : foods객체에 추가.
                     궁합음식 입력받아서 foods에 추가함
             y가아닌경우 :
                     음식을 다시 입력하기

'''
foods = {"떡볶이":"어묵","짜장면":"단무지","라면":"김치","맥주":"치킨"}
while True :
    myf = input(str(list(foods.keys())) + "중 입력(종료):")
    if myf == '종료' :
        break
    if myf in foods :  #foods 데이터의 키값 중 myf값이 존재?
        print("%s의 궁합음식:%s" % (myf,foods[myf]))
    else :  # 입력된 값이(myf)이 foods의 키값에 없는 데이터인 경우
        print("%s는 등록된 음식이 아닙니다." % myf)
        y = input("등록하시겠습니까?")
        #y.lower() : y 문자열을 소문자로 변경
        if y.lower() == 'y' :  #y = y|Y
            #myf2 : 입력된 궁합음식 값
            myf2 = input(myf + "의 궁합음식 입력:")  #궁합음식 입력
            foods[myf] = myf2  #(myf(key),myf2(value))
    
print("등록된 음식:")
for f in foods.items() :
    print(f[0],":",f[1])
for f in foods :
    print(f,":",foods[f]) 

# 튜플 : 상수화(변경 불가)된 리스트. ( )
tp1 = (10,20,30)
print(tp1)

for t in tp1 :
    print(t)
    
# 인덱스 사용 가능
print(tp1[0],tp1[1],tp1[2])
tp1.append(40)  #튜플은 변경안됨
tp1[0] = 100    #튜플은 변경안됨

# 튜플객체를 변경하기 위해서는 리스트로 변경하면 됨.
list1 = list(tp1)
list1.append(40)
list1[0] = 100
list1
# tuple() : 튜플객체로 변경
tp1 = tuple(list1)
tp1

# tp1의 요소의 갯수와 변수의 갯수가 동일하면 사용가능
a,b,c,d = tp1
print(a,b,c,d)

# tp1의 요소의 갯수 구하기
print(len(tp1))
# list1의 요소의 갯수 구하기
print(len(list1))

# tp1의 요소의 합구하기
print(sum(tp1))
# list1의 요소의 합구하기
print(sum(list1))

# 2,3번째 요소만 출력하기
print(tp1[1],tp1[2])
print(tp1[1:3])
print(tp1[:3])
print(tp1[::2])

# tp1 의 요소를 역순으로 출력하기
tp1.reverse()  #역순으로 객체를 수정. 튜플에서 불가
list1.reverse() #역순으로 객체를 수정. 
list1
# 1
for i in range(len(tp1)-1,-1,-1) :
    print(tp1[i],end=",")
# 2
print(tp1[::-1])    #역순 출력
tp1
print(list1[::-1])  #역순 출력

# set : 중복불가. 집합을 표현하는 객체 { }
set1 = {30,10,20,10}
print(set1)  # 10 요소는 힌 개만 출력됨. 순서지정안됨.
#print(set1[0])  #인덱스 사용 불가

# 집합 구현하기
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,1,2,3,4,5}
print(set1)
print(set2)
set3 = {5,6,7,8}
# 교집합 : 두 개의 집합에 공통 요소들
print("set1과 set2의 교집합 요소 : ",set1 & set2)
print("set1과 set3의 교집합 요소 : ",set1 & set3)
print("set1과 set3의 교집합 요소 : ",set1.intersection(set3))
# 합집합 : 두 개의 집합에 속한 모든 요소들
print("set1과 set2의 합집합 요소 : ",set1 | set2)
print("set1과 set3의 합집합 요소 : ",set1 | set3)
print("set1과 set3의 합집합 요소 : ",set1.intersection(set3))

#### comprehension(컴프리헨션) 방식으로 Collection 객체 생성
# 규칙성이 있는 데이터를 Collection 객체의 요소로 저장하는 방식
# numbers 리스트 : 1~10까지의 데이터 저장
# 1
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
# 2 반복문
numbers = []
for n in range(1,11) :
    numbers.append(n)
print(numbers)
# 3 컴프리헨션 이용
numbers = [x for x in range(1,11)]
print(numbers)

# numbers 리스트 : 2 ~ 20까지의 짝수 데이터 저장
numbers = [x*2 for x in range(1,11)]
print(numbers)

numbers = [x for x in range(2,21,2)]
print(numbers)

numbers = [x for x in range(1,21) if x % 2 == 0]
print(numbers)

# 문제 : 1 ~ 20까지의 수 중 2의 배수와 3의 배수만을 nums 리스트에 데이터 저장
numbers = [x for x in range(1,21) if (x % 2 == 0) or (x % 3 == 0)]
print(numbers)

# 두 개의 리스트 데이터를 각각 한 개씩 튜플로 생성하고, 튜플을 리스트로 생성하기
clist = ['black','white']
slist = ['S','M','L']
# (black,S),(black,M),(black,L),(white,S),(white,M),(white,L)
# 1 반복문 이용
dlist = []
for c in clist :        #'black','white'
    for s in slist :    #'S','M','L'
        dlist.append((c,s))
print(dlist)
# 2 컴프리헨션 방식
dlist = [(c,s) for c in clist for s in slist]  
print(dlist)

dlist = list((c,s) for c in clist for s in slist)
print(dlist)

# 두 개의 리스트 데이터를 각각 한 개씩 리스트로 생성하고,
# 리스트를 리스트로 생성하기
dlist = [[c,s] for c in clist for s in slist]  
print(dlist)

# 1~10사이의 짝수 제곱값을 가진 set 객체 생성하기
set1 = {x*x for x in range(1,11) if x%2==0}
print(set1)

set1 = {x*x for x in range(2,11,2)}
print(set1)

# dictionnary 데이터 생성하기
products = {"냉장고":200,"건조기":140,"TV":130,"세탁기":150,"컴퓨터":200}
# 200미만의 제품만 product1 객체 저장하기
product1 = {}
for k in products :
    if products[k] < 200 :
        product1[k] = products[k]
print(product1)

product1 = {}
for k in products.keys() :
    if products[k] < 200 :
        product1[k] = products[k]
print(product1)

product1 = {}
for k,v in products.items() :
    if v < 200 :
        product1[k] = v
print(product1)

# 컨프리헨션 방식
product2 = { k:v for k,v in products.items() if v<200 }
print(product2)

product2 = { k:products[k] for k in products if products[k] < 200 }
print(product2)

