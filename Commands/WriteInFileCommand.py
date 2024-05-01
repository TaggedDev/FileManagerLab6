import os.path

from Commands.Command import Command


class WriteInFileCommand(Command):
    def _execute(self, args):
        if len(args) == 0:
            print('Missing argument: filename')
            return
        path = os.path.join(self._console.current_directory, args[0])
        if not os.path.exists(path):
            print(f'No such file {path}')
            return

        raw_input = input('New file content: ')
        with open(path, 'w') as file:
            file.write(raw_input)
