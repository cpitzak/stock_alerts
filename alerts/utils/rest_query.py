import requests


class RestQuery:

    @staticmethod
    def query(url):
        with requests.Session() as s:
            s.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
            download = s.get(url)
        return download.content
