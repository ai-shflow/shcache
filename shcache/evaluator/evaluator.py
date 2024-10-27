# -*- coding: utf-8 -*-


class EvaluatorException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Evaluator(object):
    def __init__(self, config):
        if config is None:
            raise EvaluatorException("config invalid")
        self._config = config

    def run(self):
        pass
