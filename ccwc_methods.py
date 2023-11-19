import os


class Ccwc:
    """A selection of static methods used to operate on the file and return
    its characteristics.
    """

    @staticmethod
    def bytes_in_file(file):
        """Returns an int, if file not found an error message.

        The size of the file in bytes.
        """
        try:
            return os.path.getsize(file)
        except FileNotFoundError:
            return 'File not found'

    @staticmethod
    def lines_in_file(file):
        """Returns an int, if file not found an error message.

        The number of lines in the file.
        """
        line_count = 0
        try:
            with open(file, 'r') as curr_file:
                line_count = len(curr_file.readlines())
            return line_count
        except FileNotFoundError:
            return 'File not found'

    @staticmethod
    def words_in_file(file):
        """Returns an int, if file not found an error message.

        The number of words in the file.
        """
        word_count = 0
        try:
            with open(file, 'r') as curr_file:
                for line in curr_file:
                    word_count += len(line.split())
            return word_count
        except FileNotFoundError:
            return 'File not found'

    @staticmethod
    def ccwc_generic(file):
        """Returns a string, if file not found an error message.

        The number of lines, words and bytes in the file.
        """
        return (str(Ccwc.lines_in_file(file)) + ' ' + str(Ccwc.words_in_file(file)) +
                ' ' + str(Ccwc.bytes_in_file(file)))

    @staticmethod
    def chars_in_file(file):
        """Returns an int, if file not found an error message.

        The number of characters in the file.
        """
        char_count = 0
        try:
            with open(file, 'r') as curr_file:
                content = curr_file.read()
                char_count += len(content) + content.count('\n')
            return char_count
        except FileNotFoundError:
            return 'File not found'

    @staticmethod
    def st_output(file):
        """Prints file contents to standard output, if file not found returns an error message.
        """
        file_contents = ''
        try:
            with open(file, 'r') as curr_file:
                file_contents = curr_file.read()
            print(file_contents)
        except FileNotFoundError:
            return 'File not found'
