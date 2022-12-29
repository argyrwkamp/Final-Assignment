USE liquorsales;

SELECT *
FROM finance_liquor_sales
WHERE YEAR(date)>=2016 and YEAR(date)<=2019