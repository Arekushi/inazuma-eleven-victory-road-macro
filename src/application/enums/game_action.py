from enum import Enum


class GameAction(str, Enum):
    CONFIRM = 'confirm'
    CONFIRM_TEAM = 'confirm_team'
    LIST_TEAMS = 'list_teams'
    KICK_OFF = 'kick_off'
    COMMANDER_MODE = 'commander_mode'
    C_CAMERA = 'cinematographic_camera'
    SKIP = 'skip'
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
