import os

from Commands.Command import Command


class PeekFilesCommand(Command):
    def _execute(self, args):
        if len(args) > 0:
            self.display_file_content(args[0])
        else:
            self.display_whole_directory()

    def display_whole_directory(self):
        print(f'Available files: {os.listdir(self._console.current_directory)}')

    def display_file_content(self, filename):
        path = os.path.join(self._console.current_directory, filename)
        if not os.path.isfile(path):
            print('Specified path is not a file')
            return
        try:
            with open(path, 'r') as file:
                print(file.read())
        except Exception as e:
            print(f'Cant read file: {e}')
