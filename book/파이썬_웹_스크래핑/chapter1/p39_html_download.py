import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, user_agent='wswp', num_retries=2):
    print(f'Downloading: {url}')

    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)

    try:
        html = urllib.request.urlopen(request).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print(f'Download error: {e.code} {e.reason}')
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries - 1)

    return html


print(download('https://httpstat.us/500'))
