# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 정서영
# 작성일: 2026. 01. 21. 09:21:17

def solution(n):
    answer = []
    a=str(n)
    b=a[::-1]
    for i in b:
        c = int(i)
        answer.append(c)
    return answer