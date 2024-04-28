from Commands.AddFolderCommand import AddFolderCommand
from Commands.RemoveFileOrFolderCommand import RemoveFileOrFolderCommand

available_commands = dict()


class Console:
    def __init__(self, working_directory):
        self.__working_directory = working_directory
        self.__register_new_commands()

    def input_new_command(self):
        raw_input = input('>>> ')
        raw_input = raw_input.strip()
        command, *args = raw_input.split()
        available_commands[command].process_command(args)

    def __register_new_commands(self):
        available_commands['mkdir'] = AddFolderCommand('mkdir', available_commands, self.__working_directory)
        available_commands['rm'] = RemoveFileOrFolderCommand('rm', available_commands, self.__working_directory)
        available_commands['']

