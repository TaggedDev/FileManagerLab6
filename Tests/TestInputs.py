import os
import unittest

from Console import Console


def clear_path(cwd, path):
    real_path = str(os.path.join(cwd, path))
    for root, dirs, files in os.walk(real_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


class AddFolderTester(unittest.TestCase):

    def setUp(self):
        working_directory = os.getcwd()
        self.console = Console(working_directory)

    def test_incorrect_command(self):
        self.assertEqual(self.console.execute_command('_ Pathes'), -1)

    def test_add_folder(self):
        cwd = self.console.get_working_directory()
        self.console.execute_command('mkdir Pathes')
        new_path = self.console.get_working_directory() + r'\Pathes'
        exists = os.path.exists(new_path)

        clear_path(cwd, 'Pathes')
        self.assertEqual(exists, True)

    def test_add_inner_folder(self):
        cwd = self.console.get_working_directory()
        self.console.execute_command('mkdir Pathes/Path')
        new_path = self.console.get_working_directory() + r'\Pathes\Path'
        exists = os.path.exists(new_path)

        clear_path(cwd, 'Pathes')
        self.assertEqual(exists, True)

    def test_add_inner_folder_with_file(self):
        self.assertEqual(self.console.execute_command('mkdir Pathes/Path/p.txt'), -1)

    def test_incorrect_inner_folder(self):
        self.assertEqual(self.console.execute_command('mkdir Pathes/Pa.th'), -1)

    def test_incorrect_inner_folder_with_file(self):
        self.assertEqual(self.console.execute_command('mkdir Pathes/Pa.th/test.txt'), -1)


class RemoveFolderTester(unittest.TestCase):
    def setUp(self):
        working_directory = os.getcwd()
        self.console = Console(working_directory)

    def test_remove_folder(self):
        cwd = self.console.get_working_directory()
        os.makedirs(os.path.join(cwd, 'Pathes/InnerPathes/Inner'))
        was_created = os.path.exists(os.path.join(cwd, 'Pathes/InnerPathes/Inner'))

        self.console.execute_command('rm Pathes/InnerPathes/Inner')
        does_exist = os.path.exists(os.path.join(cwd, 'Pathes/InnerPathes/Inner'))
        clear_path(cwd, 'Pathes')
        self.assertEqual(was_created, not does_exist)

    def test_try_remove_missing_folder(self):
        return_code = self.console.execute_command('rm Pathes/InnerPathes/Inner2')
        clear_path(cwd, 'Pathes')
        self.assertEqual(return_code, -1)

    def test_remove_folder_out_of_scope(self):
        return_code = self.console.execute_command(r'rm Z:\test.txt')
        self.assertEqual(return_code, -1)

    def test_remove_inner_folder(self):
        cwd = self.console.get_working_directory()
        os.makedirs(os.path.join(cwd, 'Pathes/InnerPathes/Inner'))
        was_created = os.path.exists(os.path.join(cwd, 'Pathes/InnerPathes/'))

        self.console.execute_command('rm Pathes/InnerPathes/')
        still_created = os.path.exists(os.path.join(cwd, 'Pathes/InnerPathes/'))

        clear_path(cwd, 'Pathes')
        self.assertEqual(was_created, not still_created)

    def test_go_then_remove(self):
        cwd = self.console.get_working_directory()
        os.makedirs(os.path.join(cwd, 'Pathes/InnerPath'))
        self.console.execute_command('go Pathes')
        was_created = os.path.exists(os.path.join(cwd, 'Pathes/InnerPath/'))

        self.console.execute_command('rm InnerPath/')
        exists = os.path.exists(os.path.join(cwd, 'Pathes/InnerPath/'))
        clear_path(cwd, 'Pathes')
        self.assertEqual(was_created, not exists)

    def test_add_then_remove(self):
        cwd = self.console.get_working_directory()

        self.console.execute_command('mkdir Pathes/InnerPath')
        was_created = os.path.exists(os.path.join(cwd, 'Pathes/InnerPath/'))

        self.console.execute_command('rm InnerPath/')
        exists = os.path.exists(os.path.join(cwd, 'Pathes/InnerPath/'))
        clear_path(cwd, 'Pathes')
        self.assertEqual(was_created, exists)


if __name__ == '__main__':
    unittest.main()
