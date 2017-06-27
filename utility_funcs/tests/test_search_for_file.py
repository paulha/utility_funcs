from unittest import TestCase

from utility_funcs.search import *
from os import pathsep
import platform

class TestSearch_for_file(TestCase):
    def setUp(self):
        self.search_path = '/bin' + pathsep + '/usr/bin' + pathsep + '~/.ssh'  # ; on windows, : on unix
        self.profile_path = '/bin/xyzzy.txt' + pathsep + '/usr/bin/xyzzy.txt' + pathsep + '~/.ssh/id_rsa'  # ; on windows, : on unix
        if platform.system() == "Windows":
            self.known_hosts = "C:\\Users\\pfhanchx\\.ssh\\known_hosts"
        elif platform.system() == "macos":
            self.known_hosts = "/Users/paulhanchett/.ssh/known_hosts"
        else:
            self.known_hosts = "/Users/paulhanchett/.ssh/known_hosts"

    def test_find_known_hosts(self):
        find_file = search_for_file('known_hosts', self.search_path)
        self.assertEqual(find_file, self.known_hosts, "Did not locate 'known_hosts'")

    def test_find_known_hosts_call_function(self):
        def called(x, options):
            pass
            return 12345

        result = search_for_file('known_hosts', self.search_path, func=called)
        self.assertEqual(result, 12345, "Callback function was not called.")


