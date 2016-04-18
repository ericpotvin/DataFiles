""" ZipCode File Module
"""
from DataFileRead import DataFileRead


class ZipCode(object):
    """ BinaryFile abstract class
    """

    SOURCE_FILENAME = "zip_codes/zip_code_database.csv"

    def __init__(self):
        """ Constructor
        """
        pass

    def get_source_filename(self):
        return DataFileRead.SOURCE_FOLDER + self.SOURCE_FILENAME
