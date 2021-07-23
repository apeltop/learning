# -l 1  탐색 depth 1
# -w 1  다운로드 간격 1초
# -no-parent 부모 디렉토리 크롤링하지 않음
# --restrict-file-names=nocontrol URL에 한국어 등이 포함되어 있을 경우 한국어 파일명으로 저장하게함

wget https://www.hanbit.co.kr/ -r --no-parent -w 1 -l 1 --restrict-file-names=nocontrol
