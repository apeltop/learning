-- https://school.programmers.co.kr/learn/courses/30/lessons/144855
SELECT
    A.CATEGORY,
    SUM(sales) AS TOTAL_SALES
FROM BOOK A JOIN BOOK_SALES B
    ON A.BOOK_ID = B.BOOK_ID
    WHERE DATE_FORMAT(sales_date, '%Y%m') = '202201'
GROUP BY A.CATEGORY
ORDER BY A.CATEGORY;