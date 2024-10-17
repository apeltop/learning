
PUBLISH hello world


-- 원형 큐 (Circular Queue) 예제
LPUSH clist A

LPUSH clist B

LPUSH clist C

LRANGE clist 0 -1
-- 1) "C"
-- 2) "B"
-- 3) "A"

RPOPLPUSH clist clist
-- "A"

LRANGE clist 0 -1
-- 1) "A"
-- 2) "C"
-- 3) "B"

XADD Email * subject "first" body "hello"

XREAD BLOCK 0 STREAMS Email 0

-- 전체 조회
XRANGE Email - +
