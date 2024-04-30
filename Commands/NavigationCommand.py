import os.path

from Commands.Command import Command


class NavigationCommand(Command):
    def _execute(self, args):
        target = args[0]
        if target == '..':
            path = os.path.dirname(self._console.current_directory)

            # Prevent from leaving working directory
            if path == os.path.dirname(self._console.get_working_directory()):
                path = self._console.get_working_directory()
        else:
            path = os.path.join(self._console.current_directory, target)

        if os.path.exists(path):
            self._console.current_directory = path
            return 0
        else:
            print(f'{path} does not exist')
            return -1


