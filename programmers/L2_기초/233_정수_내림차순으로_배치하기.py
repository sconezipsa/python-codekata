# 정수 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 알고리즘: 문자열, 정렬
# 작성자: 정서영
# 작성일: 2026. 01. 21. 10:55:31

def solution(n):
    a = str(n)
    reverse_a = sorted(a, reverse=True)
    new = ''.join(reverse_a)
    answer=int(new)
    return answer