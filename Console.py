from Commands.AddFolderCommand import AddFolderCommand
from Commands.NavigationCommand import NavigationCommand
from Commands.RemoveFileOrFolderCommand import RemoveFileOrFolderCommand

available_commands = dict()


class Console:
    def __init__(self, working_directory):
        self.__working_directory = working_directory
        self.current_directory = working_directory
        self.__register_new_commands()

    def get_working_directory(self):
        return self.__working_directory

    def input_new_command(self):
        raw_input = input(f'{self.current_directory}: >>> ')
        raw_input = raw_input.strip()
        command, *args = raw_input.split()
        available_commands[command].process_command(args)
        self.input_new_command()

    def __register_new_commands(self):
        available_commands['mkdir'] = AddFolderCommand('mkdir', available_commands, self)
        available_commands['rm'] = RemoveFileOrFolderCommand('rm', available_commands, self)
        available_commands['go'] = NavigationCommand('go', available_commands, self)

