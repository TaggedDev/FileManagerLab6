import os.path

from FileManagerLab6.Commands.Command import Command


class CreateNewFileCommand(Command):
    def _execute(self, args):
        if len(args) == 0:
            return
        filename = args[0]
        path = os.path.join(self._console.current_directory, filename)
        with open(path, 'w') as file:
            pass
