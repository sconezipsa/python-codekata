# 나머지가 1이 되는 수 찾기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 알고리즘: 수학, 반복문
# 작성자: 정서영
# 작성일: 2026. 01. 20. 13:47:20

def solution(n):
    for x in range(1,n):
        if n%x==1:
            return x
        
        # → 처음 만족한 순간 종료
        # → 자동으로 “가장 작은 x”