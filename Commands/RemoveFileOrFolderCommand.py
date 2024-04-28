from Commands.Command import Command
import os


class RemoveFileOrFolderCommand(Command):
    """
    Removes folder or file from working directory
    """
    def __init__(self, alias, commands_dict, working_directory):
        super().__init__(alias, commands_dict)
        self.__working_directory = working_directory

    def _execute(self, args):
        path = rf'{self.__working_directory}\{args[0]}'
        try:
            self.remove_path(path)
        except PermissionError:
            path = path.replace('/', '\\')
            try:
                self.remove_path(path)
            except:
                print(f'Не найдено: {path}')

    def remove_path(self, path):
        if path[-1] == '\\':
            try:
                os.rmdir(path)
            except FileNotFoundError:
                print(f'Folder "{path}" was not found')
        else:
            try:
                os.remove(path)
            except FileNotFoundError:
                print(f'File "{path}" was not found')
