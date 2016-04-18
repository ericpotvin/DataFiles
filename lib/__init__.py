""" Lib module
"""
from os import listdir
from DataFile import DataFile
from Files import Files, ERROR_FILE_NOT_FOUND

ACTION_READ = "read"
ACTION_WRITE = "write"
ERROR_INVALID_ACTION = "Invalid Action"
ERROR_INVALID_SOURCE = "Invalid Source"


class Params(object):
    """ Params object
    """
    generated_folder = None
    download_folder = None
    image_folder = None

    @staticmethod
    def execute(source, action, binary_file, search):
        """ Execute the action for a site
            :param source: the source
            :param action: the action
            :param binary_file: the binary/data file
            :param search: the index/key to search for
        """

        if not Params.valid_action(action):
            print ERROR_INVALID_ACTION
            return

        if not Params.is_valid_source(source):
            print ERROR_INVALID_SOURCE
            return

        if not Files.file_exists(binary_file):
            print ERROR_FILE_NOT_FOUND % binary_file
            return

        if source == "phone":

            if action == ACTION_READ:
                from lib.PhoneRead import PhoneRead
                print PhoneRead.read(binary_file, int(search))

            elif action == ACTION_WRITE:
                from lib.PhoneWrite import PhoneWrite
                phone = PhoneWrite()
                phone.save()

    @staticmethod
    def is_valid_source(source):
        """ Check if the site is valid
            :param source: The source
            :return boolean
        """
        sources = listdir(DataFile.SOURCE_FOLDER)
        return source in sources

    @staticmethod
    def valid_action(action):
        """ Check if the action provided is valid
            :param action: The action
            :return boolean
        """
        if action == ACTION_READ or action == ACTION_WRITE:
            return True
        return False
