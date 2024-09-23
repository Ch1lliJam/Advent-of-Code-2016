def read_single_line_input_file(filename):
    """ Return the contents of a file that is all on one line. """
    with open(filename, "r") as input_file:
        return input_file.read().strip()


def read_multi_line_input_file(filename):
    """ Return the contents of a file that is all on multiple lines. """
    with open(filename, "r") as input_file:
        rawinput = input_file.read()
        lines = rawinput.strip().split('\n')
        return lines
