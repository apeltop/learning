SET hello newval NX
-- null

SET hello newval XX

GET hello
-- newval


SET counter 100

INCR counter
-- 101

INCR counter
-- 102

INCRBY counter 50
-- 152

MSET a 10 b 20 c 30

MGET a b c
-- 1) "10"
-- 2) "20"
-- 3) "30"


LPUSH mylist E
-- 1

RPUSH mylist B
-- 2

LPUSH mylist D A C B A
-- 7

LRANGE mylist 0 -1
-- 1) "A"
-- 2) "B"
-- 3) "C"
-- 4) "A"
-- 5) "D"
-- 6) "E"
-- 7) "B"

LRANGE mylist 0 3
-- 1) "A"
-- 2) "B"
-- 3) "C"
-- 4) "A"

LPOP mylist
-- A

LPOP mylist 2
-- 1) "B"
-- 2) "C"

LRANGE mylist 0 -1
-- 1) "A"
-- 2) "D"
-- 3) "E"
-- 4) "B"

LTRIM mylist 0 1

LRANGE mylist 0 -1
-- 1) "A"
-- 2) "D"


