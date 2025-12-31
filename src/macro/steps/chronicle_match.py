from config.paths import Paths

from src.enums import Key, Language
from src.pipeline.specs import StepSpec

from src.macro.actions import focus_window, key_hold, key_press, mouse_click
from src.macro.rules import is_image_on_screen


MATCH_DIR = Paths.match_assets(Language.PT_BR)

CHRONICLE_MATCH_STEPS: list[StepSpec] = [
    {
        'name': 'Focar na tela',
        'actions': [lambda: focus_window('INAZUMA ELEVEN: Victory Road')],
        'delay_after': 0.1
    },
    {
        'name': 'Listar times',
        'actions': [lambda: key_press(Key.V)],
        'delay_after': 1
    },
    {
        'name': 'Confirmar time',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1.5
    },
    {
        'name': 'Subir dificuldade [01/02]',
        'actions': [lambda: key_press(Key.UP)],
        'delay_after': 0.5
    },
    {
        'name': 'Subir dificuldade [02/02]',
        'actions': [lambda: key_press(Key.UP)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar dificuldade',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1.0
    },
    {
        'name': 'Confirmar jogo',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar jogo',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 0.5
    },
    {
        'name': 'Iniciar partida',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar após loading',
        'rules': [
            {
                'when': lambda: is_image_on_screen(
                    image_path=MATCH_DIR / 'start-validator.png',
                    confidence=0.8,
                    grayscale=True,
                    region=(750, 900, 500, 150)
                ),
                'actions': [lambda: key_press(Key.ENTER)],
                'interval': 1.0
            }
        ],
        'delay_after': 3.0,
        'timeout': 10.0
    },
    {
        'name': 'Confirmar formação',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1.5
    },
    {
        'name': 'Pular introdução [01/02]',
        'actions': [lambda: key_hold(Key.V, seconds=2)],
        'delay_after': 0.5
    },
    {
        'name': 'Pular introdução [02/02]',
        'actions': [lambda: key_hold(Key.V, seconds=2)],
        'delay_after': 0.5
    },
    {
        'name': 'Confirmar visualização da formação [01/02]',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1.0
    },
    {
        'name': 'Confirmar visualização da formação [02/02]',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 4.0
    },
    {
        'name': 'Passe inicial',
        'actions': [lambda: mouse_click(10, 10)],
        'delay_after': 0.5
    },
    {
        'name': 'Iniciar Modo Comandante',
        'actions': [lambda: key_press(Key.U)],
        'delay_after': 0.5,
    },
    {
        'name': 'Ativar Câmera Cinematográfica',
        'actions': [lambda: key_press(Key.C)],
        'delay_after': 0.5,
    },
    {
        'name': 'Verificar se o primeiro tempo acabou ou se será vitória por vantagem',
        'rules': [
            {
                'when': lambda: is_image_on_screen(
                    image_path=MATCH_DIR / 'end-first-half-validator.png',
                    confidence=0.8,
                    grayscale=True,
                    region=(150, 950, 600, 100)
                ),
                'actions': [lambda: key_press(Key.ENTER)],
                'interval': 5.0
            },
            {
                'when': lambda: is_image_on_screen(
                    image_path=MATCH_DIR / 'end-second-half-validator.png',
                    confidence=0.8,
                    grayscale=True,
                    region=(1500, 900, 450, 200)
                ),
                'actions': [lambda: key_press(Key.ENTER)],
                'goto': 'end',
                'interval': 5.0
            }
        ],
        'delay_after': 0.5,
        'timeout': 500
    },
    {
        'name': 'Verificar se o segundo tempo acabou',
        'rules': [
            {
                'when': lambda: is_image_on_screen(
                    image_path=MATCH_DIR / 'end-second-half-validator.png',
                    confidence=0.8,
                    grayscale=True,
                    region=(1500, 900, 450, 200)
                ),
                'actions': [lambda: key_press(Key.ENTER)],
                'interval': 5.0
            }
        ],
        'delay_after': 0.5,
        'timeout': 500
    },
    {
        'name': 'Próximo',
        'label': 'end',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1
    },
    {
        'name': 'Próximo',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 1
    },
    {
        'name': 'Finalizar',
        'actions': [lambda: key_press(Key.ENTER)],
        'delay_after': 5.0
    },
]
