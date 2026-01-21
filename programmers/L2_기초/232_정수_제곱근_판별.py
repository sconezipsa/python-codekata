# 정수 제곱근 판별
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 알고리즘: 수학
# 작성자: 정서영
# 작성일: 2026. 01. 21. 09:31:29

def solution(n):
    x = int(n ** 0.5)

    if x * x == n:
        return (x + 1) * (x + 1)
    else:
        return -1
