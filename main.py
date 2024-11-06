import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# 한글 폰트 설정 (윈도우일 경우, 'Malgun Gothic', 맥일 경우 'AppleGothic' 사용)
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 제대로 표시되게 설정

# CSV 파일 읽기
data_csv = pd.read_csv('move_people_10years.csv', encoding='utf-8')

# 데이터 구조 확인
data_csv.head()

# 데이터 준비
years = data_csv['년도']
regions = data_csv.columns[1:]  # 지역 이름들

plt.figure(figsize=(14, 8))

# 각 지역별로 라인 그래프 생성
for region in regions:
    plt.plot(years, data_csv[region], label=region)

# 그래프 제목 및 축 레이블 설정
plt.title('Population Movement by Region Over Years')
plt.xlabel('년도')
plt.ylabel('인구 변동 추이')

# 범례를 오른쪽에 표시
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 그래프 표시
plt.show()
