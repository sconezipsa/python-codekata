# 직사각형 별찍기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 알고리즘: 반복문
# 작성자: 정서영
# 작성일: 2026. 01. 19. 10:44:38

n , m = map(int,input().split(" "))
a = '*'
for i in range(m):
    print (a*n)