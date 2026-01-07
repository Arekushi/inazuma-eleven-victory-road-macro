class DirectoryException(Exception):
    pass


class DirectoryNotFoundException(DirectoryException):
    pass


class NotADirectory(DirectoryException):
    pass


class DirectoryAlreadyExists(DirectoryException):
    pass
