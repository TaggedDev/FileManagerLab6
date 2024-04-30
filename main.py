import os

from Console import Console
WORKING_DIRECTORY = None


def main():
    global WORKING_DIRECTORY
    try:
        with open('config.cfg') as file:
            text = file.read()
            first_line = text.split('\n')[0]
            WORKING_DIRECTORY = first_line
    except:
        with open('config.cfg', 'w') as file:
            file.write(os.getcwd())
        raise ConnectionError('File config.cfg first row must have path to working directory')

    console = Console(WORKING_DIRECTORY)
    console.input_new_command()


if __name__ == '__main__':
    main()
