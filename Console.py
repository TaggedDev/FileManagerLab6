from Commands.AddFolderCommand import AddFolderCommand
from Commands.NavigationCommand import NavigationCommand
from Commands.RemoveFileOrFolderCommand import RemoveFileOrFolderCommand
from Commands.PeekFilesCommand import PeekFilesCommand
from Commands.CreateNewFileCommand import CreateNewFileCommand
from Commands.WriteInFileCommand import WriteInFileCommand

available_commands = dict()


class Console:
    def __init__(self, working_directory):
        self.__working_directory = working_directory
        self.current_directory = working_directory
        self.__register_new_commands()

    def get_working_directory(self):
        return self.__working_directory

    def execute_command(self, raw_input):
        try:
            command, *args = raw_input.split()
            return available_commands[command].process_command(args)
        except:
            return -1

    def input_new_command(self, raw_input=None):
        if raw_input is None:
            raw_input = input(f'{self.current_directory}: >>> ')
            raw_input = raw_input.strip()

        self.execute_command(raw_input)
        self.input_new_command()

    def __register_new_commands(self):
        available_commands['mkdir'] = AddFolderCommand('mkdir', available_commands, self)
        available_commands['rm'] = RemoveFileOrFolderCommand('rm', available_commands, self)
        available_commands['go'] = NavigationCommand('go', available_commands, self)
        available_commands['cat'] = PeekFilesCommand('cat', available_commands, self)
        available_commands['touch'] = CreateNewFileCommand('touch', available_commands, self)
        available_commands['write'] = WriteInFileCommand('write', available_commands, self)
