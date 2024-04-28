import os

from Commands.Command import Command


class AddFolderCommand(Command):
    """
    Adds folder to the working directory
    """

    def _execute(self, args):
        if len(args) == 0:
            raise Exception("No argument given")

        args[0] = args[0].replace('/', '\\')
        new_directory = rf'{self._console.current_directory}\{args[0]}'
        # os.mkdir - create single folder
        # os.makedirs - recursively create inner folders
        os.makedirs(new_directory)

    def _on_finish(self):
        print(f'Directory created')
