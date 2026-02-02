# 배열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 알고리즘: 기초
# 작성자: 정서영
# 작성일: 2026. 02. 02. 09:29:59

def solution(num_list):
    answer = []
    for i in range(len(num_list)-1,-1,-1):
        answer.append(num_list[i])
    return answer