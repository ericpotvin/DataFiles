""" ZipCode Read module
"""
from ZipCode import ZipCode
from DataFileRead import DataFileRead


class ZipCodeRead(ZipCode):
    """ Phone read class
    """

    def __init__(self):
        super(ZipCodeRead, self).__init__()

    @staticmethod
    def read(binary_file, index):
        data_file = DataFileRead(binary_file)
        return data_file.read(index)
