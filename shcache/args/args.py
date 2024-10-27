# -*- coding: utf-8 -*-

import argparse

from shcache.__version__ import __version__


class Args(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="gpt cache")
        self._add()

    def _add(self):
        self._parser.add_argument(
            "--config-file",
            action="store",
            dest="config_file",
            help="config file (.yml)",
            required=True,
        )
        self._parser.add_argument(
            "--listen-url",
            action="store",
            default="",
            dest="listen_url",
            help="listen url (host:port)",
            required=True,
        )
        self._parser.add_argument(
            "-v", "--version", action="version", version=__version__
        )

    def parse(self, argv):
        return self._parser.parse_args(argv[1:])
