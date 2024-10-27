# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.generator.generator import Generator, GeneratorException


def test_exception():
    exception = GeneratorException("exception")
    assert str(exception) == "exception"


def test_evaluator():
    try:
        _ = Generator(None)
    except GeneratorException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Generator(config)
    except GeneratorException as _:
        assert False
    else:
        assert True
