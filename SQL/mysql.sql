
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

-- null 처리
--1) if null(col,처리방법)
SELECT animal_type, ifnull(name,'No name') name , sex_upon_intake
from animal_ins
--2) case when (조건) then (결과) else (결과) end as (별명)
select animal_type, 
    case when name is null then 'No name'
    else name end as name,
    sex_upon_intake
from animal_ins


-- join
-- (animal_outs에만 있는 id 구하기)
SELECT  animal_outs.animal_id, animal_outs.name
from animal_outs left join animal_ins
on animal_ins.animal_id = animal_outs.animal_id
where  animal_ins.animal_id is null

-- 보호시작일이 입양일보다 늦은 경우 
select a.animal_id, a.name
from animal_ins as a left join animal_outs as b
on a.animal_id=b.animal_id
where a.datetime>b.datetime
order by a.datetime asc


-- 입양가지못한 동물중 가장 오래된 동물 3마리 출력
-- 입양을 못 간 동물 : outs에 id 없어야함 a-b
-- 그중에서 datetime이 빠른거 3 (limit n)

SELECT a.name, a.datetime
from animal_ins as a left join animal_outs as b 
on a.animal_id = b.animal_id
where b.animal_id is null
order by 2
limit 3


--보건소에 와서 중성화한 동물
-- like %,_
SELECT a.animal_id, a.animal_type, a.name
from animal_ins as a left join animal_outs as b
on a.animal_id = b.animal_id
where a.sex_upon_intake like 'Intact%' and (b.sex_upon_outcome like "Spayed%" or  b.sex_upon_outcome like "Neutered%")



-- 이름에 el 들어가는 강아지 찾기
SELECT animal_id, name
from animal_ins
where animal_type = 'Dog' and name like '%el%'
order by 2



--헤비 유저가 소유한 장소

-- host_id별 카운트해서 2이상인것만 추출 
SELECT id, name, host_id
from places 
where host_id in (
    select host_id
    from places 
    group by host_id
    having count(host_id)>1)
order by 1


-- 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니
SELECT distinct a.cart_id
from cart_products as a, cart_products as b
where a.cart_id= b.cart_id and a.name like 'Milk' and b.name like 'Yogurt'


--
-- 코드를 입력하세요
SELECT animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
order by 1

-- case when !
select animal_id , name, 
    case when sex_upon_intake like 'Neutered%' or sex_upon_intake like 'Spayed%' then 'O' 
    else 'X' end as 중성화
from animal_ins


-- 보호기간이 오래된 동물 2 (order 시 -로 해줘서 desc) 
SELECT b.animal_id, b.name 
from animal_ins as a, animal_outs as b
where a.animal_id = b.animal_id
order by (b.datetime - a.datetime) desc
limit 2


-- date_format
SELECT animal_id , name , date_format(datetime, '%Y-%m-%d') as 날짜
from animal_ins



--PostgreSQL

-- write your code in PostgreSQL 9.4
SELECT a.event_type, (a.value-b.value)
from(SELECT event_type, value
from(SELECT event_type, value, rank() over(partition by event_type order by time desc) as 순위, count(*) over(partition by event_type) as count
from events) as a
where a.count >=2 and a.순위 = 1) as a,
(SELECT event_type, value
from(SELECT event_type, value, rank() over(partition by event_type order by time desc) as 순위, count(*) over(partition by event_type) as count
from events) as a
where a.count >=2 and a.순위 = 2) as b
where b.event_type=a.event_type


-- write your code in PostgreSQL 9.4
-- 차이 반환하는 테이블, union all
-- coalesce
SELECT t.team_id, t.team_name , coalesce(result.num_points,0)
from teams as t left join
(SELECT distinct r.team_id, sum(r.score) over(partition by r.team_id ) num_points
from
(SELECT host_team as team_id,case
when (host_goals - guest_goals) > 0 then 3 
when (host_goals - guest_goals) = 0 then 1
else 0 end as score
from matches 
union all
SELECT guest_team as team_id,case
when (guest_goals - host_goals) > 0 then 3 
when (guest_goals - host_goals) = 0 then 1
else 0 end as score
from matches ) as r ) as result
on t.team_id = result.team_id
order by 3 DESC,1 ASC



-- concat, left,right, lower, order by
(select concat(name,'(',left(occupation,1),')') 
from OCCUPATIONs)
union
(select concat('There are a total of ',o.count, ' ',lower(o.occupation),'s.')
from  (select occupation, count(occupation) count 
       from OCCUPATIONs
       group by occupation
       order by count)as o)
order by 1

-- 집계함수안에 distinct 가능
select count(city)-count(distinct city)
from station


-- 한글은 CHAR_LENGTH

(select l.city
from (select city, length(city) length from station) as l 
where l.length = (select min(length(city)) from station)
order by 1
limit 1)
union all
(select l.city 
from (select city, length(city) length from station) as l 
where l.length = (select max(length(city)) from station)
order by 1
limit 1)

--
select distinct city
from station
where city like "a%" or  city like "e%" or  city like "i%" or  city like "o%" or  city like "u%" 

--
select distinct city
from station
where left(city,1) in ("a","e","i","o","u") and right(city,1) in ("a","e","i","o","u") 

--
select name
from students
where marks >75
order by right(name,3) ,id

-- ceil, trucate, round
select round(sum(lat_n),2) lat,  round(sum(long_w),2) lon
from station

-- abs
select round(abs(min(lat_n)-max(lat_n))+abs(min(long_w)-max(long_w)),4)
from station


-- format, pow(num,n) => num의 n승
select format(sqrt(pow(max(lat_n)-min(lat_n),2)+pow((max(long_w)-min(long_w)),2)),4)
from station

--중앙값(median)구하기 , set(indexing)
-- 짝수일때(0,1,2,3) > (3/2) -> 1,2
set @rowidx=-1; -- ; 꼭해주어야함

select round(avg(l.lat_n),4) as median
from (select (@rowidx:=@rowidx+1) row_idx , lat_n
     from station
     order by lat_n) as l
where l.row_idx in (floor(@rowidx/2),ceil(@rowidx/2))


-- with 외워쫌,, table이 정해져있지않을 때 좋은듯하당
-- repeat('',n)
with recursive a as(
    select 20 as cnt 
    union all
    select cnt-1
    from a
    where cnt >0
)

select repeat('* ',cnt)
from a

-- prime num // not exists ,num1.num>num2.num
with recursive a as(
    select 2 as num
    union all
    select num+1
    from a 
    where num < 1000)

select group_concat(num1.num separator '&')
from a as num1
where not exists (select *
                 from a as num2
                 where num1.num%num2.num =0
                 and num1.num>num2.num)