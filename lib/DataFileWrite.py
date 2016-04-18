""" Data File Writer

    The file contains 3 sections:
    - header
    - index
    - data

    The "header" section is static and always use the same amount of space.
    This sections contains:
    - number of records
    - index when data starts at
    - min id
    - max id

    The "index" section contains the list of valid indexes

    The "index_data" section contains the search keys.
    It contains the following data:
    - key
    - start position
    - length

    The "data" section contains the data using custom format.
"""
import csv
import operator

from DataFile import DataFile
from Files import Files
from Util import zerofill


class DataFileWrite(DataFile):

    def __init__(self, file_name):
        super(DataFileWrite, self).__init__(file_name)

        self._raw_data = None

        self._index = ""

        self._index_data = []
        self._index_data_start = 0
        self._index_data_len = 0

        self._data = []
        self._data_start = 0

        self._import_csv()

        # setup the index and data list
        self._build_data()

        self._set_data_start()

    def _import_csv(self):
        """ Import CSV file to a list
        """

        if not Files.file_exists(self._input_file):
            return ""

        with open(self._input_file, 'rb') as data:
            self._raw_data = list(csv.reader(data))

        self._raw_data.sort(key=operator.itemgetter(0))

    def _set_data_start(self):
        """ Set the start data index
        """
        header_size = self.NUMBER_RECORD_HEADER * self.ZERO_FILL + 1
        index_size = len(self._index[0]) * len(self._index)
        size = + header_size + index_size
        self._data_start = zerofill(size)

    def _build_data(self):
        """ Build the file index and data
        """
        current_position = 0
        index = []
        for key in self._raw_data:
            index.append(str(key[0]))

            index_data = self.FIELD_DELIMITER.join(
                [str(key[0]), zerofill(current_position),
                 zerofill(len('|'.join(key)))])

            data = str(key[0]) + self.FIELD_DELIMITER + \
                DataFile.FIELD_DELIMITER.join(key[1:])

            self._index_data.append(index_data)
            self._data.append(data)

            current_position += len(data)

        self._index = self.FIELD_DELIMITER.join(index)

    def _get_header(self):
        """ Get the file header
            :return string
        """
        number_record = len(self._index.split(self.FIELD_DELIMITER))
        index_length = len(self._index)
        index_list = self._index.split(self.FIELD_DELIMITER)
        index_start = zerofill(self.NUMBER_RECORD_HEADER * self.ZERO_FILL)
        data_length = len(''.join(self._index_data))

        return "%s" * self.NUMBER_RECORD_HEADER % (
            zerofill(number_record),
            zerofill(index_length),
            zerofill(index_start),
            zerofill(data_length),
            zerofill(min(index_list)),
            zerofill(max(index_list))
        )

    def save(self):
        data = self._get_header() + \
               self._index + \
               ''.join(self._index_data) + \
               ''.join(self._data)

        Files.write_binary(data, self.get_bin_filename(), DataFile.SAVE_FOLDER)
