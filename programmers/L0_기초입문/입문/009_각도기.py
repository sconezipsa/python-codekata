# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 정서영
# 작성일: 2026. 01. 19. 09:17:21

def solution(angle):
    if angle==180:
        answer = 4
        return answer
    elif angle>90:
        answer = 3
        return answer
    elif angle==90:
        answer = 2
        return answer
    else:
        answer = 1
        return answer
    
angle=[70,91,180] 
