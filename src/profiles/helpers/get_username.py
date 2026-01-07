import getpass
import os


def get_username() -> str:    
    try:
        return getpass.getuser()
    except Exception:
        return os.environ.get('USERNAME') or os.environ.get('USER') or 'unknown'
