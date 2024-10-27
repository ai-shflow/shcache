# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.llm.llm import Llm, LlmException


def test_exception():
    exception = LlmException("exception")
    assert str(exception) == "exception"


def test_evaluator():
    try:
        _ = Llm(None)
    except LlmException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Llm(config)
    except LlmException as _:
        assert False
    else:
        assert True
