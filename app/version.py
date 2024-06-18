from io import open


def read_version(filename):
    """
    Read the version from the file.

    :param filename: The file to read the version from.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "0.0.0"

__version__ = read_version(".version").strip()

if __name__ == "__main__":
    print(__version__)
