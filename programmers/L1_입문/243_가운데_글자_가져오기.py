# 가운데 글자 가져오기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 알고리즘: 문자열
# 작성자: 정서영
# 작성일: 2026. 01. 19. 10:06:56

def solution(s):
    a = len(s)
    if a%2 != 0:
        return s[a//2]
    else:
        return s[a//2-1:a//2+1]