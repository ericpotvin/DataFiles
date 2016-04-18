""" Data File Module
"""
from os import path
from abc import ABCMeta


class DataFile:
    """ BinaryFile abstract class
    """
    __metaclass__ = ABCMeta

    BIN_EXT = ".bin"
    FIELD_DELIMITER = "|"
    NUMBER_RECORD_HEADER = 6
    SAVE_FOLDER = "bin/"
    SOURCE_FOLDER = "sources/"
    ZERO_FILL = 8

    def __init__(self, input_file):
        """ Constructor
        """
        self._input_file = input_file

    def get_bin_filename(self):
        filename = path.basename(self._input_file)
        filename = path.splitext(filename)[0]
        return filename + self.BIN_EXT
