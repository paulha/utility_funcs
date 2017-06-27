from unittest import TestCase

from utility_funcs.search import *

from os import pathsep
import platform

class TestFileSearch(TestCase):

    def setUp(self):
        self.search_path = '/bin' + pathsep + '/usr/bin' + pathsep + '~/.ssh'  # ; on windows, : on unix
        self.profile_path = '/bin/xyzzy.txt' + pathsep + '/usr/bin/xyzzy.txt' + pathsep + '~/.ssh/id_rsa'  # ; on windows, : on unix
        if platform.system() == "Windows":
            self.id_rsa = "C:\\Users\\pfhanchx\\.ssh\\id_rsa"
        elif platform.system() == "macos":
            self.id_rsa = "/Users/paulhanchett/.ssh/id_rsa"
        else:
            self.id_rsa = "/Users/paulhanchett/.ssh/id_rsa"


    def test_find_profile(self):
        profile = search_for_profile(self.profile_path)
        self.assertEqual(profile, self.id_rsa, "Did not locate profile 'id_rsa'")


