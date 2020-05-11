from .conn import Conn


class APICli:

    def __init__(self, host, port):
        self._schema = "https" if port == 443 else "http"
        self._base_url = f"{self._schema}://{host}:{port}"
        self._conn = Conn(base_url=self._base_url)
