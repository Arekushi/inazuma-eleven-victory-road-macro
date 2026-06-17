from src.input.controllers import InputController
from src.application.enums import GameAction, PipelineContextKeys
from src.pipeline.classes import PipelineContext


def press(
    ctx: PipelineContext,
    action: GameAction,
):
    controller: InputController = ctx.get(PipelineContextKeys.CONTROLLER)
    controller.press(action)
