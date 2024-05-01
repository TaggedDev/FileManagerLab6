import os

from Commands.Command import Command


class MoveFileCommand(Command):
    def _execute(self, args):
        if len(args) <= 1:
            print('Missing argument: filename, new_path')
            return

        filename = args[0]
        new_path = args[1]

        path = self._console.current_directory
        full_path_before = os.path.join(path, filename)
        if not os.path.exists(full_path_before):
            print('File does not exist')
            return

        if not os.path.exists(new_path):
            print('Target path does not exist')
            return

        full_path_after = os.path.join(self._console.get_working_directory(), new_path, filename)
        os.rename(full_path_before, full_path_after)
