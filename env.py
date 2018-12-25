# -*- coding:utf-8 -*-
#
# File      : env.py
# This file is part of RT-Thread RTOS
# COPYRIGHT (C) 2006 - 2018, RT-Thread Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Change Logs:
# Date           Author          Notes
# 2018-5-28      SummerGift      Add copyright information
#

import os
import sys
import argparse
import platform

from cmds import *
from vars import Export

__version__ = 'rt-thread packages v1.0.0'


def init_argparse():
    print("In init argparse")
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers()
    print("===> 1")

    parser.add_argument('-v', '--version',
                        action='version', version=__version__)

    print("===> 2")
    cmd_system.add_parser(subs)
    print("===> 3")
    cmd_menuconfig.add_parser(subs)
    print("===> 4")
    cmd_package.add_parser(subs)
    print("===> 5")

    return parser


def main():
    print("In env main()")
    bsp_root = os.getcwd()
    script_root = os.path.split(os.path.realpath(__file__))[0]
    env_root = os.getenv("ENV_ROOT")
    if env_root == None:
        if platform.system() != 'Windows':
            env_root = os.path.join(os.getenv('HOME'), '.env')
        else:
            env_root = os.path.join(os.getenv('USERPROFILE'), '.env')

    sys.path = sys.path + [os.path.join(script_root)]

    print("env root: %s"%env_root)

    Export('env_root')
    Export('bsp_root')

    # parser = init_argparse()
    # print("===> 6.1")
    # args = parser.parse_args()
    # print("===> 6.2")
    # args.func(args)
    # print("===> 6")


if __name__ == '__main__':
    main()

