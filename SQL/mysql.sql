
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

-- groupby
-- 고양이와 개는 몇마리 있을까
SELECT ANIMAL_TYPE, COUNT(*) 
FROM ANIMAL_INS 
WHERE ANIMAL_TYPE IN ('Cat', 'Dog') 
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE

--동명 동물 수 찾기
SELECT *
FROM(
    SELECT A.NAME, COUNT(A.NAME) COUNT
    FROM ANIMAL_INS AS A
    WHERE A.NAME <>'NULL'
    GROUP BY A.NAME) AS B
WHERE B.COUNT >1
ORDER BY 1



/*
mysql 날짜 관련 함수 

1) dayofweek(date) : 날짜를 한 주의 몇 번째 요일인지를 나타내는 숫자로 리턴
(1 = 일요일, 2 = 월요일, ... 7 = 토요일)

2) weekday(date) : (0 = 월요일, ... 6 = 일요일)

# 나중에 다시정리 

hour(time) : 시간을 알려줌 (0~23)
*/

-- 입양시각 구하기(1)

SELECT A.HOUR , COUNT(A.HOUR) COUNT
FROM (
    SELECT hour(B.DATETIME) HOUR
    FROM ANIMAL_OUTS AS B
    WHERE hour(B.DATETIME) >= 9 AND hour(B.DATETIME) < 20
) AS A
GROUP BY 1
ORDER BY 1

-- 다른 방법
SELECT hour(A.DATETIME) HOUR, COUNT(A.DATETIME) COUNT
FROM ANIMAL_OUTS AS A
WHERE hour(A.DATETIME) >= 9 AND hour(A.DATETIME) <= 19
GROUP BY 1
ORDER BY 1


--입양시각 구하기 (2)

/* 
1) recursive
with recursive time as (
    select 1 as HOUR
    union all (전체 합치기)
    select HOUR + 1
    from time
    where HOUR < 23
)
2) left join
select HOUR count(animal_id) COUNT
from time
left join animal_outs on HOUR = hour(datatime)
group by 1
*/
with recursive time as(
    select 0 as HOUR
    union all 
    select HOUR + 1
    from time 
    where HOUR < 23
)

select HOUR, count(animal_id) COUNT
from time
left join animal_outs on HOUR = hour(datetime)
group by 1 
order by 1

-- 이름 없는 동물의 아이디

SELECT animal_id 
from animal_ins as a
where name is null
order by 1