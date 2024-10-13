ZADD daliy-score:220817 28 player:286
ZADD daliy-score:220817 400 player:224
ZADD daliy-score:220817 45 player:101
ZADD daliy-score:220817 357 player:24
ZADD daliy-score:220817 199 player:143

ZRANGE daliy-score:220817 0 -1 withscores
-- 1) "player:286" 28
-- 2) "player:101" 45
-- 3) "player:143" 199
-- 4) "player:24" 357
-- 5) "player:224" 400

ZREVRANGE daliy-score:220817 0 2 withscores
-- 1) "player:224" 400
-- 2) "player:24" 357
-- 3) "player:143" 199

ZADD daliy-score:220817 200 player:286

ZINCRBY daliy-score:220817 100 player:24

-- 5개 이상 데이터 저장되지 않도록 강제
ZREMRANGEBYRANK daliy-score:220817 -6 -6
