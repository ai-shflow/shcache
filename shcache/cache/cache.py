# -*- coding: utf-8 -*-


class CacheException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Cache(object):
    def __init__(self, config):
        if config is None:
            raise CacheException("config invalid")
        self._config = config

    def run(self):
        pass
