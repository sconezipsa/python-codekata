# 뒤집힌 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 알고리즘: 기초
# 작성자: 정서영
# 작성일: 2026. 02. 02. 20:29:09

def solution(my_string):
    answer = ''
    for i in range(len(my_string)-1,-1,-1):
        answer += my_string[i]
    return answer