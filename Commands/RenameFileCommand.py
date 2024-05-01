import os

from Commands.Command import Command


class RenameFileCommand(Command):
    def _execute(self, args):
        if len(args) <= 1:
            print('Missing argument: filename, new_name')
            return

        filename = args[0]
        new_filename = args[1]

        path = self._console.current_directory
        full_path_before = os.path.join(path, filename)
        if not os.path.exists(full_path_before):
            print('File does not exist')
            return

        full_path_after = os.path.join(path, new_filename)
        os.rename(full_path_before, full_path_after)


