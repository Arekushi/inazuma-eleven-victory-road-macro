from abc import ABC, abstractmethod
from .pipeline_event import PipelineEvent


class PipelineObserver(ABC):

    @abstractmethod
    def notify(self, event: PipelineEvent) -> None:
        pass
