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

PFADD 202211:user:245 49483
PFADD 202211:user:245 32714
PFADD 202211:user:245 49483

PFCOUNT 202211:user:245
-- 2

GEOADD user 50.07146286003341 14.414496454175485 142

GEOADD restaurant 50.07146286003341 14.414496454175485 ukalendu

GEOPOS restaurant ukalendu
-- longitude 50.07146286003341, latitude 14.414496454175485

GEOSEARCH restaurant fromlonlat 50.06824582815170288 14.41818466583587366 byradius 1 km
-- 1) "ukalendu"
