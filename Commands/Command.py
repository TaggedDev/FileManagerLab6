class Command:
    def __init__(self, alias: str, commands_dict: dict, console):
        self.__alias = alias
        self._console = console
        commands_dict[alias] = self

    def process_command(self, args):
        self._execute(args)
        self._on_finish()

    def _execute(self, args):
        pass

    def _on_finish(self):
        print('Command executed')
