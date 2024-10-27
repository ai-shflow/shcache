# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.vector.vector import Vector, VectorException


def test_exception():
    exception = VectorException("exception")
    assert str(exception) == "exception"


def test_evaluator():
    try:
        _ = Vector(None)
    except VectorException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Vector(config)
    except VectorException as _:
        assert False
    else:
        assert True
