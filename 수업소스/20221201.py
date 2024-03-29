# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:22:50 2022

@author: kimyh
"""

'''
    파일
      하위 목록 : os.listdir()
      폴더생성  : os.mkdir()
      폴더삭제  : os.rmdir()
      
    엑셀 파일 읽기 : 엑셀 파일 종류에 따라 다른 모듈이 필요 => pandas로 접근
      xlsx : opoenpyxl 모듈 사용
      xls  : xlrd 모듈로 읽기
             xlwd 모듈로 쓰기
             
    db 연결
      sqlite : sqlite3 모듈 이용
      oracle : cx_Oracle 모듈 이용
          => 외부 모듈 pip install cx_Oracle 실행 후 사용가능

'''
'''
    pandas : 표향태의 데이터 저장 모듈
      Series : 1차원형태의 데이터
      DataFrame : 2차원 형태(행,열)의 데이터
          Series 데이터의 모임
'''
import pandas as pd
#딕셔너리 데이터를 Series 데이터로
dict_data = {'a':1,'b':2,'c':3}
sr = pd.Series(dict_data)
print(sr)
print(sr.index)
print(sr.values)
#튜플 데이터를 Series 데이터로
tuple_data = ("홍길동",'1991-01-25','남',True)
sr = pd.Series(tuple_data,index=["이름","생년월일","성별","학생여부"])
print(sr)
print(sr.index)  #값의 이름
print(sr.values)

#한개의 값만 조회
print(sr[0])  #순서로 조회
print(sr["이름"])  #인덱스로 조회
print(sr.이름)
print(sr[1])  #순서로 조회
print(sr["생년월일"])  #인덱스로 조회
print(sr.생년월일)  #인덱스로 조회
#여러개의 값 조회
print(sr[[0,1]])  #순서로 조회
print(sr[['이름','생년월일']])  #인덱스로 조회
#print(sr['이름','생년월일'])  #오류발생
#여러개의 값 조회. 범위 지정하여 조회
print(sr[0:2])  #순서로 조회. 마지막값 앞까지
print(sr['이름':'성별'])  #인덱스로 조회. 마지막 값까지

#데이터 프레임 객체 생성하기
#딕셔너리 이용
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(df)
print("컬럼명:",df.columns)  #열의 이름
print("인덱스명:",df.index)  #행의 이름
#한개 조회
df["c0"]
type(df["c0"])
#여러개 조회
df[["c0","c1"]]
type(df[["c0","c1"]])

#리스트를 이용하여 데이터프레임 객체 생성
df = pd.DataFrame([[15,'남','서울중'],[17,'여','서울여고'],[17,'남','서울고']],
                  index=['홍길동','성춘향','이몽룡'])
df
df = pd.DataFrame([[15,'남','서울중'],[17,'여','서울여고'],[17,'남','서울고']],
                  index=['홍길동','성춘향','이몽룡'],
                  columns=['나이','성별','학교'])
print(df)
print(df.index)
print(df.columns)

#인덱스명 변경하기
df.index=["학생1","학생2","학생3"]
print(df)
#컬럼명 변경하기
df.columns=["age","gender","school"]
print(df)

#rename : 컬럼명, 인덱스명의 일부만 변경하기
# inplace=True : 객체 자체 변경
df.rename(columns={"age":"나이"},inplace=True)
print(df)
# inplace=True 사용하지 않으면, df = 대입구문이 대체 효과
df = df.rename(index={"학생1":"홍길동"})  # inplace=True 효과
print(df)


exam_data={'수학':[90,80,70],'영어':[98,88,95],
           '음악':[85,95,100],'체육':[100,90,90]}
# 문제 exam_data를 이용하여 인덱스는 홍길동, 이몽룡, 김삿갓인 
# DataFrame 객체 생성하기
print(exam_data)
# 1
df = pd.DataFrame(exam_data,index=['홍길동','이몽룡','김삿갓'])
print(df)
# 2
df = pd.DataFrame(exam_data)
df.index=['홍길동','이몽룡','김삿갓']
print(df)
#mean() : 평균
print(df.mean())
#수학평균
print("수학평균:",df.mean()["수학"])
print("수학평균:",df["수학"].mean())  #Serise.mean() 함수
print(df["수학"])  #Series 객체
#수학총점
print(df.sum())
print(type(df.sum()))
print(df.sum()["수학"])
print(df["수학"].sum())
#과목별 최대점수
print(df.max())
#수학 최대점수
print(df.max()["수학"])
print(df["수학"].max())
#median() : 중간값
'''
    중간값 : 데이터를 정렬하여 가운데 값
    수학 : [90,80,70]
    영어 : [98,95,88]
    데이터의 갯수 홀수 : 가운데 값
    데이터의 갯수 짝수 : 가운데 두 값의 평균
'''
print(df.median())
#수학의 중간값
print(df.median()["수학"])
print(df["수학"].median())

#홍길동 데이터 조회하기
df.수학
df["수학"]
#인덱스명으로 조회하기 => 행의 값 조회 .loc 사용
# loc[인덱스명] : 인덱스에 해당하는 행을 조회
# iloc[순서] : 순서로 해당하는 행을 조회
df.loc["홍길동"]  #홍길동 행 조회
df.iloc[0]  #첫번째 행 조회
type(df.loc["홍길동"])  #Series 객체
df.loc["홍길동"].mean()  #평균
df.loc["홍길동"].median()  #중간값
#표준편차 : std() : sqrt((평균값-값) ** 2 합계)
#                   sqrt(분산)                   
#분산 : var()
df.std()  #표준편차
df.var()  #분산

#기술통계 => 기본적인 수치데이터조회
df.describe()
type(df.describe())
#수학 통계정보
df.describe()["수학"]
df["수학"].describe()
#간략정보
df.info()
df["수학"].info()  #오류
#데이터의 처름 일부(5개) 조회
df.head()
#데이터의 마미막 5개 조회
df.tail()

#김삿갓의 총점, 평균, 중간값, 표준편차를 조회하기
df.loc["김삿갓"]
print("총점:",df.loc["김삿갓"].sum())
print("평균:",df.loc["김삿갓"].mean())
print("중간값:",df.loc["김삿갓"].median())
print("표준편차",df.loc["김삿갓"].std())
df.loc["김삿갓"].describe()

#데이터프레임 복사하기
df2 = df  #얕은 복사. df, df2는 동일한 객체임
df2.info()
df
#df 데이터의 홍길동 인덱스를 홍길순으로 변경하기
df.rename(index={"홍길동":"홍길순"},inplace=True)
df
df2

#깊은 복사 : 두 개 객체가 다른 객체
df3 = df[:] #깊은 복사. [:] 범위지정. 전체 영역
#df 데이터의 홍길동 인덱스를 홍길동으로 변경하기
df.rename(index={"홍길순":"홍길동"},inplace=True)
df
df3

#drop() : 행, 열 제거하기
# axis=0 : 행을 의미
# axis=1 : 열을 의미
#행 제거하기
df3.drop(["홍길순"],axis=0,inplace=True)
df3
#열 제거하기
df3.drop(["체육"],axis=1,inplace=True)
df3
#열 제거하기
del df3["음악"]
df3

#copy() : 깊은 복사
df4 = df.copy()
df4
#df4에서 음악, 체육 제거하기
del df4["음악"],df4["체육"]
df4
df4 = df.copy()
df4
df4.drop(["음악","체육"], axis=1, inplace=True)
df4

#df 데이터의 수학, 영어 컬럼 조회하기
df[["수학","영어"]]
df["수학","영어"]  #오류
#df 데이터의 수학 컬럼 조회하기
df["수학"]  #Series 객체
df[["수학"]]  #DataFrame 객체
type(df["수학"])  #Series 객체
type(df[["수학"]])  #DataFrame 객체

#df 데이터의 이몽룡 학생 점수 조회하기
df.loc["이몽룡"]  #인덱스 이름
df
df.iloc[1]  #순서 조회
#df 데이터의 이몽룡, 김삿갓 학생 점수 조회하기
df.loc[["이몽룡","김삿갓"]]  #인덱스 이름
df.iloc[[0,1]]  #순서 조회
#범위로 조회하기
df.loc["이몽룡":"김삿갓"]  #이몽룡부터 김삿갓까지
df.loc["이몽룡":]  #이몽룡부터 끝까지
df.loc[:"김삿갓"]  #처음부터 김삿갓까지
df.loc[:]  #처음부터 끝까지
df.loc[::2]  #처음부터 끝까지 2칸씩 조회
df.loc[::-1]  #처음부터 끝까지 역순으로 조회

df.iloc[1:3] #1번부터 2번까지
df.iloc[1:]  #1번부터 끝까지
df.iloc[:2]  #처음부터 1번까지
df.iloc[:]  #처음부터 끝까지
df.iloc[::2]  #처음부터 끝까지 2칸씩 조회
df.iloc[::-1]  #처음부터 끝까지 역순으로 조회

#이몽룡의 수학, 영어, 점수 조회하기
df[["수학","영어"]].loc["이몽룡"]  #Seies 객체
df.loc["이몽룡"][["수학","영어"]]
df.loc["이몽룡",["수학","영어"]]
df.loc[["이몽룡"],["수학","영어"]]  #DataFrame 객체
df.loc[["이몽룡"]][["수학","영어"]]  #DataFrame 객체

df[:]  #컬럼만 조회
df.loc[:,:]  #df.loc[행의 범위,열의 범위]

#jeju1.csv 파일을 판다스모듈을 이용하여 읽기
import pandas as pd
#read_csv : jeju1.csv 파일 읽기 DataFrame 객체로 생성
df = pd.read_csv("data/jeju1.csv")
df.info()  #간략 정보
df.head()  #상위 5건 조회
df.tail()  #하위 5견 조회

#장소만 조회하기
df.장소
df["장소"]
df[["장소"]]
df[0:1]

#LON,LAT만 조회하기
df[["LON","LAT"]]
df
#장소컬럼을 인덱스로 변경하기
df.set_index("장소",inplace=True)
#돔베돈의 경도 위도 조회하기
df.loc["돔베돈"]
df.loc[["돔베돈"]]
#인덱스 값을 여행지 컬럼으로 추가하기
#컬럼추가 : dataFrame[새로운컬럼명]=값
#컬럼수정 : dataFrame[기존컬럼명]=값
df["여행지"]=df.index
df
df.info()

#현재의 index값을 컬럼으로 변경
df.reset_index(inplace=True)
df.info()
df
#장소 컬럼 제거하기
df.drop("장소", axis=1, inplace=True)
df
#df 데이터의 내용을 csv 파일로 저장하기
#to_csv("파일이름",index=False)
# index=False : 인덱스 파일에 저장 안함
#               기본값 True
df.to_csv("data/df_jeju.csv",index=False)  #index 제외
df.to_csv("data/df_jeju.csv")  #index 포함

#excel 파일 읽기
'''
    read_excel("파일이름","sheet이름","인덱스컬럼")
    ("data/sales_2015.xlsx","january_2015",index_col=None)
    => data/sales_2015.xlsx 파일에서 january_2015 sheet 데이터 읽기.
    인덱스 컬럼 설정 안함
    
    sheet_name=None : sheet 이름 지정 안함
                      모든 sheet 읽기
'''
#한개의 sheet 읽기
df = pd.read_excel("data/sales_2015.xlsx","january_2015",index_col=None)
type(df)  #DataFrame 객체
df
df.info()

#모든 sheet 읽기
df = pd.read_excel("data/sales_2015.xlsx",sheet_name=None,index_col=None)
df
type(df)  #딕셔너리 객체 데이터
'''
    {"sheet이름 : dataframe 데이터, ..."}
'''
for name, data in df.items() :
    print("sheet 이름:",name)
    print("data의 자료형:",type(data))
type(data)
data.info()

data
#Sale Amount 컬럼의 값이 500보다 큰 레코드만 조회
data[data["Sale Amount"] > 500]
data.loc[data["Sale Amount"] > 500]

data["Sale Amount"] > 500  #True, False 값들
data[[False,True,False,True,False,True]]
# => data 중 레코드의 값이 True인 데이터만 조회
#500보다 큰 레코드만 df500 데이터에 저장
df500 = data[data["Sale Amount"] > 500]
df500  #DataFrame 객체
#df500 데이터를 pd_sale_2015.xlsx 파일의 2015_500 sheet로 저장하기

# 내용없는 엑셀파일 pd_sale_2015.xlsx 생성함
outexcel = pd.ExcelWriter("data/pd_sale_2015.xlsx")
# df500 데이터의 내용을 outexcel 파일의 2015_500 sheet 이름으로
# 인덱스를 제외하고 저장
df500.to_excel(outexcel, sheet_name="2015_500",index=False)
data.to_excel(outexcel, sheet_name="2015",index=False)
outexcel.save()  #엑셀 저장하기


#매입일자가 2015-03-17일 정보만 조회하기
df0317 = data[data["Purchase Date"] == '2015-03-17']
df0317

'''
df[[컬럼,...]] => 컬럼조회
df[:] => 범위를 지정. row 조회함.
'''
df.info()
df["Part Number":"Cost"] #row 인식 . 오류

df[:1]   #행조회
df.iloc[:1] # 행조회

df[:1,:1]   #오류
df.iloc[:1,:1] # 정상


import pandas as pd
import cx_Oracle as co
from datetime import datetime
import sqlite3

conn=sqlite3.connect("mydb")
sqlite_result = pd.read_sql("select * from member",conn)
sqlite_result
conn.close()

start_tm = datetime.now()
#  DB Connecion
conn = co.connect("kic", "1234","localhost/xe")
query_result = pd.read_sql("select * from student", conn)     
conn.close()

end_tm = datetime.now()
print('START: ', str(start_tm))
print('END: ', str(end_tm))
print('ELAP: ', str(end_tm - start_tm))

query_result.info()

