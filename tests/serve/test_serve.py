# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.serve.serve import Serve, ServeException


def test_exception():
    exception = ServeException("exception")
    assert str(exception) == "exception"


def test_serve():
    try:
        _ = Serve(None)
    except ServeException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Serve(config)
    except ServeException as _:
        assert False
    else:
        assert True
