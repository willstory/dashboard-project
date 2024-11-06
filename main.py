import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.widgets import CheckButtons

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

# 그래프 크기 설정
fig, ax = plt.subplots(figsize=(14, 8))

# 각 지역별로 라인 그래프 생성
lines = []
for region in regions:
    line, = ax.plot(years, data_csv[region], label=region)
    lines.append(line)

# 그래프 제목 및 축 레이블 설정
ax.set_title('Population Movement by Region Over Years')
ax.set_xlabel('년도')
ax.set_ylabel('인구 변동 추이')

# 범례를 오른쪽에 표시
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 체크 박스 생성 (그래프 오른쪽에 위치)
ax_check = plt.axes([0.85, 0.3, 0.1, 0.4])  # (left, bottom, width, height)
check = CheckButtons(ax_check, regions, [True] * len(regions))  # 초기 상태는 모두 활성화

# 체크박스 클릭 시 동작 정의


def func(label):
    index = regions.tolist().index(label)
    lines[index].set_visible(check.get_status()[index]
                             )  # 체크박스 상태에 따라 라인 표시 여부 결정
    plt.draw()


check.on_clicked(func)

# 그래프 표시
plt.show()
