from datetime import datetime


from src.dsl.compiler import PipelineCompiler
from src.logging import LoggerFactory, LoggerConfig
from src.input.providers import InputProviderFactory
from src.input.controllers import InputController

from config.paths import Paths
from src.application import SystemOSDetector
from src.application.match import MatchCommandConfig
from src.application.enums import PipelineContextKeys
from src.pipeline.observers import PipelineLogger
from src.pipeline.observers.logger.handlers import (
    PipelineStartLogHandler,
    StepEnterLogHandler,
    PipelineEndLogHandler,
    PipelineResetLogHandler,
    StepTimeoutLogHandler
)


MATCH_MACRO_FILENAME = 'match'


class MatchCommandPipeline:
    def __init__(self, config: MatchCommandConfig):
        self.config = config
        self.pipeline = None

    def build(self):
        self.pipeline = PipelineCompiler.compile_file(
            Paths.macro_file(MATCH_MACRO_FILENAME)
        )

        self._configure_pipeline()
        self._configure_context()
        self._configure_observers()

        return self

    def run(self):
        if self.pipeline is None:
            raise RuntimeError()

        self.pipeline.run()

    def _configure_pipeline(self):
        self.pipeline.max_loops = self.config.max_loops

    def _configure_context(self):
        ctx = self.pipeline.context
        
        ctx.set(
            PipelineContextKeys.CONTROLLER,
            InputController(InputProviderFactory.create(SystemOSDetector.detect(), self.config.input_mode))
        )

    def _configure_observers(self):
        logger = self._get_logger()
        self.pipeline.logger = logger

        self.pipeline.add_observer(
            PipelineLogger(
                logger=logger,
                handlers=(
                    PipelineEndLogHandler(),
                    PipelineStartLogHandler(),
                    StepEnterLogHandler(),
                    StepTimeoutLogHandler(),
                    PipelineResetLogHandler()
                )
            )
        )

    def _get_logger(self):
        return LoggerFactory.get_logger(
            config=LoggerConfig(
                name='match_command',
                log_to_file=self.config.enable_log_file,
                log_filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S.%f')
            )
        )
