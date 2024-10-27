# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.adapter.adapter import Adapter, AdapterException


def test_exception():
    exception = AdapterException("exception")
    assert str(exception) == "exception"


def test_adapter():
    try:
        _ = Adapter(None)
    except AdapterException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Adapter(config)
    except AdapterException as _:
        assert False
    else:
        assert True
