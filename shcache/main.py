# -*- coding: utf-8 -*-

import sys

from shcache.args.args import Args
from shcache.config.config import Config, ConfigException
from shcache.logger.logger import Logger
from shcache.serve.serve import Serve, ServeException


def main():
    _args = Args().parse(sys.argv)

    try:
        config = Config()
        config.config_file = _args.config_file
        config.listen_url = _args.listen_url
    except ConfigException as e:
        Logger.error(str(e))
        return -1

    Logger.info("running")

    try:
        s = Serve(config)
        s.run()
    except ServeException as e:
        Logger.error(str(e))
        return -2

    Logger.info("exiting")

    return 0
