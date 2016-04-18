""" Data File Reader
"""
from DataFile import DataFile
from Files import Files


class DataFileRead(DataFile):

    def __init__(self, file_name):
        super(DataFileRead, self).__init__(file_name)

    def read(self, index):
        """ Get the record for an key
            :param index: The index
            :return: list
        """

        header = self._get_binary_header(index)

        if not header:
            return ""

        index_length = int(header[1])
        index_start = int(header[2])

        index_position = self._get_index_position(index, index_start,
                                                  index_length)

        if index_position is None:
            return False

        index_data_start = index_length + index_start
        index_data = self._get_index_data(index, index_data_start,
                                          index_position)

        position = index_data_start + index_data[1] + header[3]

        if not index_data:
            return ""

        data = Files.read_binary_file(
            self._input_file,
            position,
            index_data[2]
        )

        return data.split(self.FIELD_DELIMITER)

    def _get_binary_header(self, index):

        data = Files.read_binary_file(
            self._input_file,
            0,
            self.NUMBER_RECORD_HEADER * self.ZERO_FILL
        )
        chunks, chunk_size = len(data), len(data) / self.NUMBER_RECORD_HEADER

        header = map(int, [data[i:i + chunk_size] for i in range(
            0, chunks, chunk_size)])

        if header[0] == 0:
            return False

        if index < header[4] or index > header[5]:
            return ""

        return header

    def _get_index_position(self, index, start, length):
        data = Files.read_binary_file(
            self._input_file,
            start,
            length
        )

        data = [int(x) for x in data.split(self.FIELD_DELIMITER)]

        if index not in data:
            return None

        return data.index(index)

    def _get_index_data(self, index, start, index_position):
        length = len(str(index)) + 2 + (self.ZERO_FILL * 2)

        data = Files.read_binary_file(
            self._input_file,
            start + (index_position * length),
            length
        )

        if not data:
            return False

        data = data.split(self.FIELD_DELIMITER)

        for (key, value) in enumerate(data):
            data[key] = int(value)

        return data
