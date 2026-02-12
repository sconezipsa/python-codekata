# 하샤드 수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 알고리즘: 수학, 문자열
# 작성자: 정서영
# 작성일: 2026. 02. 12. 19:08:50

def solution(x):
    original = x
    digit_sum = 0
    
    while x > 0:
        digit_sum += x % 10
        x //= 10
    
    return original % digit_sum == 0
