import os

from Commands.Command import Command


class AddFolderCommand(Command):
    """
    Adds folder to the working directory
    """
    def __init__(self, alias, commands_dict, working_directory):
        super().__init__(alias, commands_dict)
        self.__working_directory = working_directory

    def _execute(self, args):
        if len(args) == 0:
            raise Exception("No argument given")

        new_directory = rf'{self.__working_directory}\{args[0]}'
        os.mkdir(new_directory)

    def _on_finish(self):
        print(f'Directory created')
