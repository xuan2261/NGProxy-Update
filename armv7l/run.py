#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import sys

from core_ext import debug, main


parser = argparse.ArgumentParser(
    description='NGProxy - NextGen Proxy')
parser.add_argument(
    '--debug', help='Debug device and get information', action='store_true')
args = parser.parse_args()

if __name__ == "__main__":
    if args.debug:
        debug()
        sys.exit(0)

    main()
