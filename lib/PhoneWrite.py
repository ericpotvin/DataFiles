""" Phone Write module
"""
from Phone import Phone
from DataFileWrite import DataFileWrite


class PhoneWrite(Phone):
    """ Phone write class
    """

    def __init__(self):
        super(PhoneWrite, self).__init__()

    def save(self):

        data_file = DataFileWrite(self.get_source_filename())
        data_file.save()
