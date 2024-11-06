def func(label_total):
    if label_total == '자치도 그룹':
        group_lines.set_visible(check_group.get_status()[0])  # 자치도 그룹의 가시성 제어
    else:
        index = regions.tolist().index(label_total)
        lines[index].set_visible(check.get_status()[index])  # 개별 지역 라인의 가시성 제어
    plt.draw()
