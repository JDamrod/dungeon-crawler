from commands import Command, DEFAULT_KEYS
from non_copyable import NonCopyable


class InputHandler(NonCopyable):
    def __init__(self, keys=None):
        if keys is None:
            keys = DEFAULT_KEYS
        self.__keys = dict(keys)

    def read(self):
        try:
            text = input("> ").strip().lower()
        except EOFError:
            return Command.QUIT
        if text == "":
            return Command.NONE
        return self.__keys.get(text[0], Command.NONE)
