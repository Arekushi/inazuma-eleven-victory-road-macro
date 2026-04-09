from src.helpers.obj import require
from src.input.classes.input_resolver import InputResolver
from src.input.abc.press_capability import PressCapability
from src.application.enums import GameAction, PipelineContextKeys
from src.pipeline.classes import PipelineContext


def hold(
    ctx: PipelineContext,
    action: GameAction,
    duration_seconds: float
):
    controller = ctx.get(PipelineContextKeys.CONTROLLER)
    resolver: InputResolver = ctx.get(PipelineContextKeys.INPUT_RESOLVER)
    
    press_capability = require(controller, PressCapability)
    binding = resolver.resolve(action)
    
    press_capability.hold(binding, duration_seconds)
