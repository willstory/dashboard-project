import streamlit as st
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

# Streamlit 페이지 설정
st.title('인구 이동 및 자치도 그룹 분석')
st.write('각 지역별 인구 이동 변화를 그래프와 함께 확인할 수 있습니다.')

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

# 체크 박스 생성 (Streamlit 위젯)
selected_regions = [
    region for region in regions if st.checkbox(region, value=True)]

# 자치도 그룹을 추가하는 체크박스
show_group = st.checkbox('자치도 그룹', value=True)

# 자치도 그룹 라인 생성 (세종특별자치시, 강원특별자치도, 전북특별자치도, 제주특별자치도)
group_regions = ['세종특별자치시', '강원특별자치도', '전북특별자치도', '제주특별자치도']
group_data = data_csv[group_regions].sum(axis=1)

# 선택된 지역만 그래프에 표시
for region in selected_regions:
    ax.plot(years, data_csv[region], label=region)

# 자치도 그룹 그래프를 표시할지 여부에 따라 표시
if show_group:
    ax.plot(years, group_data, label='자치도 그룹', color='black', linestyle='--')

# 그래프 범례 추가
ax.legend()

# 그래프 표시 (Streamlit에서 matplotlib 그래프 표시)
st.pyplot(fig)
