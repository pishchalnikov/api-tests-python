from .conn import Conn


class BaseEndpoint:

    def __init__(self, conn: Conn):
        self._conn = conn
