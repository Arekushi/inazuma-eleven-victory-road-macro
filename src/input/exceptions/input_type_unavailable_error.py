class InputTypeUnavailableError(RuntimeError):
    '''Raised when the requested input type is not available.'''

    def __init__(self):
        super().__init__(
            'The input type is not available on this system. Try Changing to desktop or gamepad.'
        )
