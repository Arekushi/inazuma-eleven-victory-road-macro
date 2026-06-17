from src.input.controllers import InputController
from src.application.enums import GameAction, PipelineContextKeys
from src.pipeline.classes import PipelineContext


def hold(
    ctx: PipelineContext,
    action: GameAction,
    duration_seconds: float
):
    controller: InputController = ctx.get(PipelineContextKeys.CONTROLLER)
    controller.hold(action, duration_seconds)
