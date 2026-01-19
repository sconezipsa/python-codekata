# 평균 구하기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 알고리즘: 기본연산, 배열
# 작성자: 정서영
# 작성일: 2026. 01. 19. 09:32:13

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer = answer/len(arr)
    return answer