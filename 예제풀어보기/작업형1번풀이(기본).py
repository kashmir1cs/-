# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
from sklearn.preprocessing import MinMaxScaler #sklearn의 MinMax Scaler 사용
df = pd.read_csv('data/mtcars.csv', index_col=0) #dataframe 작성
df_qsec=df[['qsec']] 
# 사용자 코딩
scaler_minmax=MinMaxScaler()
scaler_minmax.fit(df_qsec)
qsec_scaled=scaler_minmax.transform(df_qsec)
record_overhalf=len(qsec_scaled[qsec_scaled>0.5])
print("레코드 수량: ",record_overhalf)


# 답안 제출 예시
# print(평균변수값)
