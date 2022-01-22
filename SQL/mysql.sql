
-- 프로그래머스

-- 여러기준으로 정렬하기 
SELECT A.ANIMAL_ID,A.NAME,A.DATETIME
FROM ANIMAL_INS AS A
ORDER BY 2 , 3 DESC

-- 상위 n개 레코드
SELECT B.NAME
FROM ANIMAL_INS AS B
WHERE B.DATETIME=
(SELECT MIN(A.DATETIME)
FROM ANIMAL_INS AS A)

-- 중복제거
SELECT COUNT(DISTINCT A.NAME) count
FROM ANIMAL_INS AS A
WHERE A.NAME <> 'NULL'
