""" ZipCode Write module
"""
from ZipCode import ZipCode
from DataFileWrite import DataFileWrite


class ZipCodeWrite(ZipCode):
    """ Phone write class
    """

    def __init__(self):
        super(ZipCodeWrite, self).__init__()

    def save(self):

        data_file = DataFileWrite(self.get_source_filename())
        data_file.save()
