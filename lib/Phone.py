""" Phone File Module
"""
from DataFileRead import DataFileRead


class Phone(object):
    """ BinaryFile abstract class
    """

    SOURCE_FILENAME = "phone/nanpa.csv"

    def __init__(self):
        """ Constructor
        """
        pass

    def get_source_filename(self):
        return DataFileRead.SOURCE_FOLDER + self.SOURCE_FILENAME
