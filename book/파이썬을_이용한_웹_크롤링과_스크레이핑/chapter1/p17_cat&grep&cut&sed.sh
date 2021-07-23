cat ./csv/books.csv

cat ./csv/books.csv | grep 파이썬

# -d 구분할 문자
# -f 열의 번호
cat ./csv/books.csv | cut -d , -f 1,2

# s/<regx>/<치환할 문자>/<options>
# s/,/ /g  => 모든(g) ,를 공백으로 치환해서 출력
cat ./csv/books.csv | sed 's/,/ /g'

