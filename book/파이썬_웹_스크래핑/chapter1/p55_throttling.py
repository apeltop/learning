import time
import urllib.request
from urllib.error import ContentTooShortError, HTTPError, URLError
from urllib.parse import urlparse


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


class Throttle:

    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (time.time() - last_accessed)
            if sleep_secs > 0:
                time.sleep(sleep_secs)

        self.domains[domain] = time.time()