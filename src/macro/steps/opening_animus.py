from config.paths import Paths

from src.enums import Key
from src.pipeline.specs import StepSpec

from src.macro.rules import passives_are_valid
from src.macro.actions import focus_window, key_hold, key_press, mouse_click, \
    send_notification, stop_pipeline


OPENING_ANIMUS_STEPS: list[StepSpec] = [
    {
        'name': 'Focar na tela',
        'actions': [lambda: focus_window('INAZUMA ELEVEN: Victory Road')],
        'delay_after': 0.1
    },
    {
        'name': 'Selecionar Animus',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1
    },
    {
        'name': 'Invocar Jogador',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1
    },
    {
        'name': 'Mover para (sim)',
        'actions': [lambda: key_press(Key.LEFT)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar (sim)',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 4
    },
    {
        'name': 'Próximo',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1.5
    },
    {
        'name': 'Ir para outra aba [01/02]',
        'actions': [lambda: key_press(Key.E)],
        'delay_after': 0.5
    },
    {
        'name': 'Ir para outra aba [02/02]',
        'actions': [lambda: key_press(Key.E)],
        'delay_after': 0.5
    },
    {
        'name': 'Verificar passivas',
        'rules': [
            {
                'when': lambda ctx: passives_are_valid(
                    criteria=ctx.get('criteria'),
                    passives=ctx.get('passives')
                ),
                'actions': [
                    lambda: send_notification(
                        title='Sucesso!',
                        message='O Animus foi encontrado!'
                    ),
                    lambda: stop_pipeline()
                ],
                'interval': 0.5
            }
        ],
        'timeout': 3.0
    },
    {
        'name': 'Confirmar [01/02]',
        'actions': [lambda: key_press(Key.E)],
        'delay_after': 1.5
    },
    {
        'name': 'Confirmar [02/02]',
        'actions': [lambda: key_press(Key.E)],
        'delay_after': 1.5
    },
]
