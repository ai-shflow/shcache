# -*- coding: utf-8 -*-


class GeneratorException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Generator(object):
    def __init__(self, config):
        if config is None:
            raise GeneratorException("config invalid")
        self._config = config

    def run(self):
        pass
