# -*- coding: utf-8 -*-

import sys

from shcache.cmd.argument import Argument
from shcache.config.config import Config, ConfigException


def main():
    argument = Argument()
    arg = argument.parse(sys.argv)

    try:
        config = Config()
        config.config_file = arg.config_file
    except ConfigException as e:
        return -1

    return 0
