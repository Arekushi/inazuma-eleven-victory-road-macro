from src.helpers.obj import require
from src.input.classes.input_resolver import InputResolver
from src.input.abc.press_capability import PressCapability
from src.application.enums import GameAction, PipelineContextKeys
from src.pipeline.classes import PipelineContext


def press(
    ctx: PipelineContext,
    action: GameAction
):
    controller = ctx.get(PipelineContextKeys.CONTROLLER)
    resolver: InputResolver = ctx.get(PipelineContextKeys.INPUT_RESOLVER)
    
    press_capability = require(controller, PressCapability)
    binding = resolver.resolve(action)
    
    press_capability.press(binding)
