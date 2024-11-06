import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
from matplotlib.widgets import CheckButtons
from group import func

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

# 체크 박스 생성 (그래프 오른쪽 상단에 위치)
ax_check = plt.axes([0.9, 0.7, 0.1, 0.3])  # (left, bottom, width, height)
check = CheckButtons(ax_check, regions, [True] * len(regions))  # 초기 상태는 모두 활성화

# 자치도 그룹을 추가하는 체크박스 생성
ax_check_group = plt.axes([0.9, 0.4, 0.1, 0.3])  # 자치도 그룹 체크박스 위치
check_group = CheckButtons(ax_check_group, ['자치도 그룹'], [
                           True])  # 자치도 그룹 초기 상태는 활성화

# 자치도 그룹 라인 생성 (세종특별자치시, 강원특별자치도, 전북특별자치도, 제주특별자치도)
group_regions = ['세종특별자치시', '강원특별자치도', '전북특별자치도', '제주특별자치도']
group_lines, = ax.plot(years, data_csv[group_regions].sum(
    axis=1), label='자치도 그룹', color='black', linestyle='--')

# 체크박스 클릭 시 동작 정의


# 체크박스 클릭 이벤트
check.on_clicked(func)
check_group.on_clicked(func)

# 그래프 표시
plt.show()
