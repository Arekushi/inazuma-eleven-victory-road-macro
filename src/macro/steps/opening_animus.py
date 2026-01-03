from src.enums import Key
from src.pipeline.specs import StepSpec

from src.macro.rules import passives_are_valid, has_no_spirit_left
from src.macro.actions import focus_window, key_hold, key_press, \
    send_notification, stop_pipeline, register_spirit_opened, \
    log_line_break


OPENING_ANIMUS_STEPS: list[StepSpec] = [
    {
        'name': 'Focar na tela',
        'actions': [lambda: focus_window('INAZUMA ELEVEN: Victory Road')],
        'delay_after': 0.1
    },
    {
        'name': 'Selecionar Modo Crônica',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 3
    },
    {
        'name': 'Selecionar Rota Crônica',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 7
    },
    {
        'name': 'Apertar ALT',
        'actions': [lambda: key_hold(Key.ALT_LEFT, 1)],
        'delay_after': 0.5
    },
    {
        'name': 'Apertar Clube',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 0.5
    },
    {
        'name': 'Descer até a opção (Animus)',
        'actions': [lambda: key_press(Key.DOWN)],
        'delay_after': 0.5,
        'repeat': 3
    },
    {
        'name': 'Selecionar opção Animus',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1.5
    },
    
    
    {
        'name': 'Ir para Inazuma Eleven 1',
        'actions': [lambda: key_press(Key.C)],
        'delay_after': 1
    },
    {
        'name': 'Descer até o Kurimatsu',
        'actions': [lambda: key_press(Key.DOWN)],
        'delay_after': 0.5,
        'repeat': 23
    },
    {
        'name': 'Ir para a direita até o Kurimatsu',
        'actions': [lambda: key_press(Key.RIGHT)],
        'delay_after': 0.5,
        'repeat': 2
    },
    
    
    {
        'name': 'Selecionar Animus',
        'label': 'start',
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
        'name': 'Ir para outra aba',
        'actions': [lambda: key_press(Key.E)],
        'delay_after': 0.5,
        'repeat': 2
    },
    {
        'name': 'Verificar passivas',
        'rules': [
            {
                'when': lambda ctx: passives_are_valid(pipeline_ctx=ctx),
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
        'actions': [
            lambda: key_press(Key.ENTER),
            lambda ctx: register_spirit_opened(ctx)
        ],
        'delay_after': 1.5
    },
    {
        'name': 'Confirmar [02/02]',
        'actions': [
            lambda: key_press(Key.ENTER),
            lambda ctx: log_line_break(ctx)
        ],
        'delay_after': 1.5
    },
    {
        'name': 'Verificar rota',
        'rules': [
            {
                'when': lambda ctx: has_no_spirit_left(ctx),
                'goto': 'reset',
                'interval': 1
            }
        ],
        'timeout': 1,
        'delay_after': 1.5,
        'goto': 'start'
    },
    
    
    {
        'name': 'Voltar menu [01/02]',
        'label': 'reset',
        'actions': [lambda: key_press(Key.ESC)],
        'delay_after': 1
    },
    {
        'name': 'Voltar menu [02/02]',
        'actions': [lambda: key_press(Key.ESC)],
        'delay_after': 1
    },
    {
        'name': 'Subir opção para Salvar',
        'actions': [lambda: key_press(Key.UP)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar opção Salvar',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1
    },
    {
        'name': 'Descer para opção de voltar a Tela de Título',
        'actions': [lambda: key_press(Key.DOWN)],
        'delay_after': 0.5,
        'repeat': 2
    },
    {
        'name': 'Selecionar opção para voltar a Tela de Título',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 0.5
    },
    {
        'name': 'Mover para (sim)',
        'actions': [lambda: key_press(Key.LEFT)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar para voltar a Tela de Título',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 5
    }
]
