import re
import urllib.request
from urllib.error import ContentTooShortError, HTTPError, URLError
from urllib.parse import urljoin


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


def link_crawler(start_url, link_regex):
    crawl_queue = [start_url]
    seen = set(crawl_queue)

    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        if not html:
            continue

        for link in get_links(html):
            if re.match(link_regex, link):
                abs_link = urljoin(start_url, link)

                if abs_link not in seen:
                    seen.add(abs_link)
                    crawl_queue.append(abs_link)


def get_links(html):
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    return webpage_regex.findall(html)


link_crawler('https://www.google.com', '(.*?)')
