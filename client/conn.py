import requests
import urllib.parse


class Conn:

    def __init__(self, base_url):
        self._base_url = base_url

    def do_get(self, path, params=None, **kwargs):
        return requests.get(
            url=urllib.parse.urljoin(self._base_url, path),
            params=params,
            **kwargs
        )

    def do_post(self, path, data=None, **kwargs):
        return requests.post(
            url=urllib.parse.urljoin(self._base_url, path),
            json=data,
            **kwargs
        )
