SELECT TITLE,
       USED_GOODS_BOARD.BOARD_ID,
       USED_GOODS_REPLY.REPLY_ID,
       USED_GOODS_REPLY.WRITER_ID,
       USED_GOODS_REPLY.CONTENTS,
       DATE_FORMAT(USED_GOODS_REPLY.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD
         JOIN USED_GOODS_REPLY ON USED_GOODS_BOARD.BOARD_ID = USED_GOODS_REPLY.BOARD_ID
WHERE DATE_FORMAT(USED_GOODS_BOARD.CREATED_DATE, '%Y-%m-01') = '2022-10-01'
ORDER BY USED_GOODS_REPLY.CREATED_DATE, USED_GOODS_BOARD.TITLE
;