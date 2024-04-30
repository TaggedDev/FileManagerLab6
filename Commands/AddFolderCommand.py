import os

from Commands.Command import Command


class AddFolderCommand(Command):
    """
    Adds folder to the working directory
    """

    def _execute(self, args):
        if len(args) == 0:
            print('No argument given')
            return -1

        args[0] = args[0].replace('/', '\\')
        if '.' in args[0]:
            print('Folder name with dot are not allowed')
            return -1

        new_directory = rf'{self._console.current_directory}\{args[0]}'
        # os.mkdir - create single folder
        # os.makedirs - recursively create inner folders
        os.makedirs(new_directory)
        return 0
