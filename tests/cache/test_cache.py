# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.cache.cache import Cache, CacheException


def test_exception():
    exception = CacheException("exception")
    assert str(exception) == "exception"


def test_cache():
    try:
        _ = Cache(None)
    except CacheException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Cache(config)
    except CacheException as _:
        assert False
    else:
        assert True
