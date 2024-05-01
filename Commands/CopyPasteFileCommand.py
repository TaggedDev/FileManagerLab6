import os
import shutil

from Commands.Command import Command


class CopyPasteFileCommand(Command):
    def _execute(self, args):
        if len(args) <= 1:
            print('Missing arguments: filename, new_path')
            return

        filename = args[0]
        new_path = args[1]

        path = self._console.current_directory
        source_path = os.path.join(path, filename)
        if not os.path.exists(source_path):
            print(f'File {source_path} does not exist')
            return

        destination_path = os.path.join(new_path, filename)
        if not os.path.exists(new_path):
            print(f'New path {new_path} does not exist')
            return

        shutil.copyfile(source_path, destination_path)
