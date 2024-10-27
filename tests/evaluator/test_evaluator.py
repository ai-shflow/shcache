# -*- coding: utf-8 -*-

import os

from shcache.config.config import Config
from shcache.evaluator.evaluator import Evaluator, EvaluatorException


def test_exception():
    exception = EvaluatorException("exception")
    assert str(exception) == "exception"


def test_evaluator():
    try:
        _ = Evaluator(None)
    except EvaluatorException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(
        os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
    )

    try:
        _ = Evaluator(config)
    except EvaluatorException as _:
        assert False
    else:
        assert True
