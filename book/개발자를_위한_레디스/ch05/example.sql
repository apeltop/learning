SET a 100

EXPIRE a 60

TTL a

INCR a

TTL a
-- 37

RENAME a apple

TTL apple
-- 30

SET b 100

EXPIRE b 60

TTL b
-- 56

SET b banana

TTL b
-- -1


