# 특정 기간동안 대여 가능한 자동차들의대여비용 구하기

SELECT C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS C, ECOLI_DATA AS P
WHERE C.GENOTYPE & P.GENOTYPE = P.GENOTYPE AND C.PARENT_ID = P.ID
ORDER BY ID ASC