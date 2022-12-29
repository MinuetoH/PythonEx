# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:51:20 2022

@author: kimyh
"""

#1. test.xlsx 파일을 읽어 df 변수에 저장하기. index이름은 학생의 이름으로 한다.
df = pd.read_excel("data/test.xlsx")
df.info()
df.set_index("Unnamed: 0",inplace=True)
df
#2. 알고리즘 과목의 평균을 구하여 출력하는 코드
df.mean()

#3. 파이썬 과목의 중간값을 구하여 출력하는 코드 작성하기
df["파이썬"].median()

#4. R 과목의 표준편차값을 구하여 출력하는 코드 작성하기
df["R"].std()

#5. 각 과목의 상관계수를 출력하는 코드 작성하기
df.corr()

#6. 홍길동 학생의 과목 평균을 구하는 코드를 작성하기
df.loc["홍길동"].mean()

#7. 각 과목별 합계을 구하는 코드 작성하기
df.sum()

#8. 각 이름별 합계을 구하는 코드 작성하기
df["합계"]=df["알고리즘"]+df["파이썬"]+df["R"]
df
