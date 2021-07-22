import urllib.request
from urllib.error import ContentTooShortError, HTTPError, URLError

from lxml.html import fromstring, tostring


def download(url, num_retries=2, user_agent='wswp', charset='utf-8'):
    print(f'Downloading: {url}')

    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)

    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print(f'Download error: {e.reason}')
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)

    return html


tree = fromstring(download('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%BD%94%EB%A1%9C%EB%82%9819%EB%B0%B1%EC%8B%A0%ED%98%84%ED%99%A9'))
fixed_html = tostring(tree, pretty_print=True)
print(fixed_html)

inoculatePercent = tree.cssselect('#_cs_vaccine_info > div > div.main_tab_area > div > div > div > div:nth-child(1) > dl > dd > strong.value')[0]
value = inoculatePercent.text_content()
print(f'한국 1차 접종 퍼센트 : {value}')

