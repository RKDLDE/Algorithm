-- 코드를 입력하세요
SELECT
      ANIMAL_TYPE
    , IFNULL(NAME, "No name") as NAME
    , SEX_UPON_INTAKE
    FROM animal_ins
  ORDER BY ANIMAL_ID;