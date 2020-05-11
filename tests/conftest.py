import pytest

import config

from client.cli import APICli


@pytest.fixture(scope="module")
def api():
    _api = APICli(
        host=config.staging["host"],
        port=config.staging["port"]
    )
    return _api
