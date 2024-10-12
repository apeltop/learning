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

DEL mylist

RPUSH mylist A B C D

LRANGE mylist 0 -1

LINSERT mylist BEFORE B E

LRANGE mylist 0 -1
-- 1) "A"
-- 2) "E"
-- 3) "B"
-- 4) "C"
-- 5) "D"


LSET mylist 2 F

LRANGE mylist 0 -1
-- 1) "A"
-- 2) "E"
-- 3) "F"
-- 4) "C"
-- 5) "D"

LINDEX mylist 3
-- C

HSET Product:123 Name "Happly Hacking"

HSET Product:123 TypeID 35

HSET Product:123 Version 2002

HSET Product:234 Name "Track Ball" TypeID 32

HGET Product:123 TypeID
-- 35

HMGET Product:234 Name TypeID
-- 1) "Track Ball"
-- 2) "32"

HGETALL Product:234
-- 1) "Name"
-- 2) "Track Ball"
-- 3) "TypeID"
-- 4) "32"

SADD myset A

SADD myset A A A C B D D E F F F F G
-- 6

SMEMBERS myset
-- 1) "A"
-- 2) "B"
-- 3) "C"
-- 4) "D"
-- 5) "E"
-- 6) "F"
-- 7) "G"

SREM myset B

SPOP myset
-- E

ZADD score:220817 100 user:B

ZADD score:220817 150 user:A 150 user:C 200 user:F 300 user:E

ZRANGE score:220817 1 3 WITHSCORES
-- 1) "user:A" 150
-- 2) "user:C" 150
-- 3) "user:F" 200

ZRANGE score:220817 1 3 WITHSCORES REV
-- 1) "user:F" 200
-- 2) "user:C" 150
-- 3) "user:A" 150

ZRANGE score:220817 100 150 BYSCORE WITHSCORES
-- 1) "user:A" 150
-- 2) "user:C" 150
-- 3) "user:B" 100

ZRANGE score:220817 100 (150 BYSCORE WITHSCORES
-- 1) "user:B" 100

ZRANGE score:220817 200 +inf BYSCORE WITHSCORES
-- 1) "user:F" 200
-- 2) "user:E" 300

ZRANGE score:220817 +inf 200 BYSCORE WITHSCORES REV
-- 1) "user:E" 300
-- 2) "user:F" 200


SETBIT mybitmap 2 1

GETBIT mybitmap 2
-- 1

BITFIELD mybitmap SET u1 6 1 SET u1 10 1 SET u1 14 1
-- 1
-- 1
-- 1

BITCOUNT mybitmap


