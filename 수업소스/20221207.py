# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:11:47 2022

@author: kimyh
"""

### numpy : 행렬, 통계관련 기본함수, 배열 기능 제공하는 모듈
import numpy as np
#배열 생성
#np.arange(15) : 0 ~ 14까지의 숫자를 1차원 배열로 생성
#reshape(3,5) : 3행5열의 2차원 배열로 생성
#               배열의 갯수가 맞아야 함.
a = np.arange(15).reshape(3,5)
a  #0~14까지의 숫자를 3행5열의 2차원배열로 생성
type(a)

#배열 요소의 자료형
a.dtype  #int32 => 32비트, 4바이트

#배열 형태
a.shape  #(3,5) : 3행5열

np.arange(15).shape  #(15,) : 1차원배열
np.arange(15).reshape(15,1).shape  #(15, 1) : 2차원배열

#배열의 차수
a.ndim  #2차원
np.arange(15).ndim  #1

#배열의 요소의 바이트 크기
a.itemsize  #4
#배열 요소의 갯수
a.size  #15
np.arange(15).size

#리스트로 배열 생성
b = np.array([6,7,8])
b
type(b)
#튜플로 배열 생성하기
c = np.array([6,7,8])
c
type(c)
#리스트로 2차원 배열 생성하기
d = np.array([[6,7,8],[1,2,3]])
d

#0으로 초기화된 3행 4열 배열 e 생성하기
e = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
e
e.shape

e = np.zeros((3,4))
e
e.shape

#모든 요소의 값이 0인 배열 100개를 1차원으로 생성하기
f = np.zeros(100)
f.shape

#모든 요소의 값이 1인 배열 100개를 1차원으로 생성하기
g = np.ones(100)
g.shape

#1으로 초기화된 10행 10열 배열 h 생성하기
h = np.ones((10,10))
h.shape
#0~9999까지의 값을 가진 배열을 100행 100열 배열 i 생성하기
i = np.arange(10000).reshape(100,100)
i.shape
i
#0 ~ 2까지의 숫자를 9개로 균등분할하여 배열 생성
j = np.linspace(0,2,9)
j

#0 ~ 9까지의 숫자를 20개로 균등분할하여 배열 생성
k = np.linspace(0,9,20)
k
k.size
#정수형 1의 값으로 10개를 가진 배열;
l = np.ones(10,dtype=int)
l
l.dtype

#상수값
np.pi

#numpy 데이터 연산
#1차원 배열의 연산
a = np.array([20,30,40,50])
b = np.arange(4)  #(0,1,2,3)
c = a-b  #각각의 요소들을 연산
c  #array([20, 29, 38, 47])

c = a + b
c  #array([20, 31, 42, 53])

c = b**2  #b 요소들 각각의 제곱
c

c = a < 35  #a 배열의 요소를 35와 비교하여 작으면 True, 크면 False
c

#2차원 배열의 연산
a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
a
b
c = a + b  #각각의 요소를 연산
c 
c = a - b  #각각의 요소를 연산
c
c = a * b  #각각의 요소를 연산
c
# @ : 행렬의 곱. dot
c = a @ b
c
'''
    a  @  b   =                        c
  [1,1] [2,0] = [1*2+1*3][1*0+1*4] = [5,4]
  [0,1] [3,4]   [0*2+1*3][0*3+1*4]   [3,4]
  
'''
c = a.dot(b)
c

# 난수를 이용한 배열 생성
rg = np.random.default_rng(1)  #seed값 설정
rg
a = rg.random((2,3))  #2행3열배열.
a
b = np.ones((2,3),dtype=int)
b
a.dtype
b.dtype
c = a + b  #실수형 = 실수형 + 정수형 
c = b + a  #실수형 = 정수형 + 실수형 
c

a+=b  #실수형 = 실수형 + 정수형 
a
a.dtype

b+=a  #오류. 정수형 = 정수형 + 실수형

#a배열의 전체 요소들의 합
a.sum()
#a배열의 전체 요소들 중 최소값
a.min()
#a배열의 전체 요소들 중 최대값
a.max()
#a배열의 전체 요소들 중 평균값
a.mean()
#a배열의 전체 요소들의 표준편차
a.std()
a
#a배열의 행 중 최대값
a.max(axis=1)
#a배열의 열 중 최대값
a.max(axis=0)
#a배열의 행 중 최소값
a.min(axis=1)
#a배열의 열 중 최소값
a.min(axis=0)
#a배열의 행 별 합계
a.sum(axis=1)
#a배열의 행 별 누적합계
a.cumsum(axis=1)
#a배열의 열 별 합계
a.sum(axis=0)
#a배열의 열 별 누적합계
a.cumsum(axis=0)

#10부터 49까지의 c배열을 생성하기
c = np.arange(10,50)
c
#첫번째 값 출력하기
c[0]
#첫번째부터 4번째까지 값 출력하기
c[:4]  #0~3번 인덱스까지
#4번 인덱스값을 100으로 변경
c[4] = 100
c[:5]
#처음부터 3씩 증가하여 10인덱스까지 조회
c[:11:3]
c[:11]
#0부터 11까지의 숫자를 3행4열 배열 d로 생성하기
d = np.arange(12).reshape(3,4)
d
#1행 1열의 값을 조회하기
d[1,1]
d[0:2,0:2]  #1행까지, 1열까지 조
d[:2,:2]    #1행까지, 1열까지 조
d[::2,::2]  #2씩 증가
#1값으로 채워진 10행 10열 배열 e 생성하기
e = np.ones((10,10))
e
#e배열의 가장자리는 1로, 내부는 0으로 채워진 배열로 수정하기
e[1:9,1:9] = 0
e
e[1:-1,1:-1] = 0
e

#e배열과 같은 모양의 배열 f 생성
f = np.zeros((8,8))
f
'''
    행과 열에 각각 1인 값인 행열을 추가하기
    pad() : 행과 열을 추가.
    pad_width=1 : 추가될 행과 열의 갯수
    constant_values=1 : 추가될 행과 열의 값
'''
f = np.pad(f,pad_width=1,constant_values=1)
f.shape

#np.fromfunction() : 함수를 이용하여 요소의 값 설정
#np.fromfunction(함수명,행열,요소자료형) 
def f(x,y) :  #x : 행의 인덱스, y : 열의 인덱스
    return 10*x+y
'''
    f(0행,0열) : 0
    f(0행,1열) : 1
    f(0행,2열) : 2
    f(0행,3열) : 3
    f(1행,0열) : 10
        ...
    f(2행,0열) : 20
    
    g[0,1,2,3]
     [10,11,12,13]
     [20,21,22,23]
         ...
'''
g = np.fromfunction(f,(5,4),dtype=int)
g

#g배열의 0행 출력하기
g[0]
#g배열의 0열 출력하기
g[:,0]  # : => 모든 행, 0:0열
#g배열의 2열 출력하기
g[:,2]
#g배열의 0,1행, 0,1열 출력하기
g[:2,:2]

#g.flat : 배열의 요소들만 리턴
for i in g.flat :
    print(i)

#난수를 이용하여 0~9사이의 정수값을 가진 임의의수를 3행4열 배열 생성
#np.floor : 작은 근사정수
#np.ceil : 큰 근사정수
h = np.floor(np.random.random((3,4)) * 10)
h
h.ndim
h.shape
#h배열을 1차원배열 h1 변경하기
h1 = h.ravel()  #h배열이 변경되지 않음
h1.ndim
h1.shape
#h배열을 6행2열 배열 h2 변경하기
h2 = h.reshape(6,2)  #h배열이 변경되지 않음
h2.shape
h.shape
#h배열 자체를 6행2열 배열로 변경하기
h.resize(6,2)
h.shape
#h배열을 3행5열로 변경하기
h.reshape(3,5)  #오류. h배열의 요소의 갯수가 12. 3행5열:15개
h.reshape(3,4)
h.shape
#3행을 지정. 열을 자동 맞춤
h.reshape(3,-1)  #-1을 지정하면 자동으로 맞춤
h.reshape(4,-1).shape  #-1을 지정하면 자동으로 맞춤
h.reshape(-1,4).shape

#0~9사이의 정수형 난수값을 가진 2행2열 배열 생성
#randint : 정수형 난수 리턴.
i = np.random.randint(10,size=(2,2))
i
j = np.random.randint(10,size=(2,2))
j

#2개의 배열을 합하기
np.vstack((i,j))  #행기준 합. 열의 갯수가 같아야 함.
np.hstack((i,j))  #열기준 합. 행의 갯수가 같아야 함.
#배열 나누기
k = np.random.randint(10,size=(2,12))
k
np.hsplit(k,3)  #3개로 열을 분리
np.vsplit(k,2)  #2개로 열을 분리
k.shape
#k배열의 모든 요소값을 100으로 변경하기
#k = 100. k변수에 100 정수값을 저장. k값은 배열이 아님.
k[0,0] = 100
k[0,:] = 100
k[:] = 100
k[:,:] = 200
k
#0~19사이의 임의의 정수를 가진 5행 4열 배열 l을 생성하기
l = np.random.randint(20,size=(5,4))
l
l.max()
#각 행의 최대값들을 조회하기
l.max(axis=1)
#각 행의 최대값들을 조회하기
l.max(axis=0)

#각 행의 최대값의 인덱스를 조회하기
l.argmax(axis=1)
#각 행의 최대값의 인덱스를 조회하기
l.argmax(axis=0)
#각 행의 최소값의 인덱스를 조회하기
l.argmin(axis=1)
#각 행의 최소값의 인덱스를 조회하기
l.argmin(axis=0)

#단위행렬 : 대각선(행==열) 셀으 값이 1인 배열
m = np.eye(10,10)  #10행10열 단위 행렬
m
#m배열의 0이 아닌 요소의 인덱스 조회
np.nonzero(m)
n = [1,2,0,4,0]  #list
type(n)
np.nonzero(n)  #요소의 값이 0이 아닌 요소의 인덱스 리턴

#정규분포 값을 가진 임의의 수 10000개를 가진 배열
#np.random.normal : 정규분포에 맞는 난수 발생 함수
# (0,1,10000) => (평균,표준편차,데이터갯수)
#                평균이 0, 표준편차가 1인 난수들
o = np.random.normal(0,1,10000)
o
o.mean()
o.std()
#정규분포 확인 : 히스토그램을 이용하여 확인
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus']=False  #음수표시 -설정
plt.hist(o,bins=100)

#평균:2, 표준편차:2인 난수 10000개를 생성.
p = np.random.normal(2,2,10000)
p
p.mean()
p.std()
plt.rcParams['axes.unicode_minus']=False  #음수표시 -설정
plt.hist(p,bins=100)

#choice 함수 : 값을 선택
#   choice(값의범위,선택갯수,재선택여부)
#   choice(값의범위,선택갯수,확)
#   (10,5,replace=False)
#   10 : 0 ~ 9사이의 값
#   5 : 5개 선택
#   replace=True/False : 중복가능/중복불가
q = np.random.choice(10,5,replace=False)
q

#1 ~ 45사이의 수를 중복없이 6개를 선택한 r배열 생성
r = np.random.choice(45,6,replace=False) + 1
r
#정렬
r.sort()
r

#0 ~ 3사이의 수를 중복없이 5개 선택.
#오류. 중복되어아 함
s = np.random.choice(4,5,replace=False)  #오류. 불가능한 선
s = np.random.choice(4,5,replace=True)
s

#확률 적용 선택
# p=[0.1,0.2,0.3,0.2,0.1,0.1]
# p의 전체 합 : 1

p=[0.1,0.2,0.3,0.2,0.1,0.1]
sum(p)

#choice(값의범위,선택갯수,확률)
'''
    선택수  확률   100개 선택 시 추정갯수
     0      0.1         10
     1      0.2         20
     2      0.3         30
     3      0.2         20
     4      0.1         10
     5      0.1         10
'''
t = np.random.choice(6,100,p=[0.1,0.2,0.3,0.2,0.1,0.1])
t
listt=list(t)  #list <= array
listt.count(0)  #9
listt.count(1)  #20
listt.count(2)  #26
listt.count(3)  #30
listt.count(4)  #8
listt.count(5)  #7

fruits = ["apple","banana","cherries","duriab","grapes"]
u = np.random.choice(fruits,100,p=[0.1,0.2,0.3,0.2,0.2])
listu = list(u)
for d in fruits :
    print(d,"=",listu.count(d))

'''
    행정안전부 : www.mois.go.kr
    정책자료 -> 통계 -> 주민등록 인구통계 -> 연령별 인구현황
'''
import csv
f=open("data/age.csv")
data = csv.reader(f)  #csv 형태의 파일을 읽어서 저장
type(data)  #
data  #반복문을 통해 한 행씩 조회가능
import matplotlib.pyplot as plt
name="역삼"
for row in data :
    if row[0].find(name) >= 0 :  #행정구역의 내용에 name 값 존재?
        print(row)
        name=row[0]
        #숫자의 , 제거
        row = list(map((lambda x:x.replace(",","")),row))
        print(row)
        #0세 컬럼 이후의 셀들을 배열 생성
        home = np.array(row[3:],dtype=int)
        print(home)
        break  #반복문 종료
    
#home : 해당 동의 나이별 인구수를 배열로 저장
plt.style.use('ggplot')  #스타일 설정
plt.figure(figsize=(10,5),dpi=100)
plt.rc('font',family='Malgun Gothic')   #한글 설정
plt.title(name+' 지역의 인구 구조')
plt.plot(home)  #선그래프 출




