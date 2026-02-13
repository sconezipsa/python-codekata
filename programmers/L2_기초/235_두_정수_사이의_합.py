# 두 정수 사이의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 알고리즘: 수학
# 작성자: 정서영
# 작성일: 2026. 02. 13. 09:37:17

def solution(a, b):
    start = min(a,b)
    end = max(a,b)
    answer = 0
    for i in range(start, end+1):
        answer += i
        
    return answer