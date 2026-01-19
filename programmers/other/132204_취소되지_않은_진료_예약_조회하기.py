# 취소되지 않은 진료 예약 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132204
# 작성자: 정서영
# 작성일: 2026. 01. 19. 13:55:24

-- 코드를 입력하세요
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM PATIENT P
JOIN APPOINTMENT A
ON P.PT_NO=A.PT_NO
JOIN DOCTOR D
ON A.MDDR_ID = D.DR_ID
WHERE DATE(A.APNT_YMD)='2022-04-13' AND A.APNT_CNCL_YN='N'
ORDER BY A.APNT_YMD ASC;