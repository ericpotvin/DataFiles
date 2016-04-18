#!/usr/bin/python

""" Main program
"""
import argparse
from lib import Params

source = None
action = None
search = None
binary_file = None


def parse_arg():
    """ Get arguments list
        :return args
    """

    global source, action, binary_file, search

    parser = argparse.ArgumentParser(description="Website2jSonDB")
    parser.add_argument("--source",
                        default="",
                        type=str,
                        nargs=1,
                        help='The source file to process',
                        required=True)
    parser.add_argument("--action",
                        default="",
                        type=str,
                        metavar="[ write, read ]",
                        nargs=1,
                        help='Action to perform',
                        required=True)
    parser.add_argument("--search",
                        default="",
                        type=str,
                        nargs=1,
                        help='The index/key to read',
                        required=False)
    parser.add_argument("--bin_file",
                        default="",
                        type=str,
                        nargs=1,
                        help='The binary/data file',
                        required=False)

    arguments = parser.parse_args()

    source = arguments.source[0]
    action = arguments.action[0]

    if arguments.search != "":
        search = arguments.search[0]

    if arguments.bin_file != "":
        binary_file = arguments.bin_file[0]

if __name__ == '__main__':
    parse_arg()
    Params.execute(source, action, binary_file, search)
