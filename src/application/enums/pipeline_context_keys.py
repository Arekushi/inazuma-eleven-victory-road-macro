from enum import Enum


class PipelineContextKeys(str, Enum):
    CONTROLLER = 'controller'
    INPUT_RESOLVER = 'input_resolver'
    LANGUAGE = 'language'
