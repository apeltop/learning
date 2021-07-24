wget https://wikibook.co.kr/list/ -O ./html/book-list.html

cat ./html/book-list.html | grep '<a class="book-url"'

cat ./html/book-list.html | grep '<a class="book-url"' | sed -E 's/<[^>]*>//g' | sed -E 's/^\s*//'