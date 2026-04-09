from datetime import datetime

from src.input.mappings.input_providers import INPUT_PROVIDERS
from src.dsl.compiler import PipelineCompiler
from src.logging import LoggerFactory, LoggerConfig

from src.application.match import MatchConfig
from src.application.enums import PipelineContextKeys
from src.pipeline.observers import PipelineLogger
from src.pipeline.observers.logger.handlers import (
    PipelineStartLogHandler,
    StepEnterLogHandler,
    PipelineEndLogHandler,
    PipelineResetLogHandler,
    StepTimeoutLogHandler
)


class MatchPipeline:
    def __init__(self, config: MatchConfig):
        self.config = config
        self.pipeline = None

    def build(self):
        self.pipeline = PipelineCompiler.compile_file(
            self.config.macro_path
        )

        self._configure_pipeline()
        self._configure_context()
        self._configure_observers()

        return self

    def run(self):
        if self.pipeline is None:
            raise RuntimeError('Pipeline não foi buildado')

        self.pipeline.run()

    def _configure_pipeline(self):
        self.pipeline.max_loops = self.config.max_loops

    def _configure_context(self):
        ctx = self.pipeline.context
        ctx.set(PipelineContextKeys.LANGUAGE, self.config.language)
        
        bundle = INPUT_PROVIDERS[self.config.input_mode]()
        ctx.set(PipelineContextKeys.CONTROLLER, bundle.controller)
        ctx.set(PipelineContextKeys.INPUT_RESOLVER, bundle.resolver)

    def _configure_observers(self):
        if not self.config.enable_log:
            return

        logger = self._create_logger()

        self.pipeline.logger = logger

        self.pipeline.add_observer(
            PipelineLogger(
                logger=logger,
                handlers=self._build_log_handlers()
            )
        )

    def _create_logger(self):
        return LoggerFactory.get_logger(
            config=LoggerConfig(
                name=f'{self.config.macro_path.stem}_command',
                log_filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S.%f')
            )
        )

    def _build_log_handlers(self):
        return (
            PipelineEndLogHandler(),
            PipelineStartLogHandler(),
            StepEnterLogHandler(),
            StepTimeoutLogHandler(),
            PipelineResetLogHandler()
        )
