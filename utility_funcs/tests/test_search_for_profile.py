from unittest import TestCase

from utility_funcs.search import *

from os import pathsep

class TestFileSearch(TestCase):

    def setUp(self):
        self.search_path = '/bin' + pathsep + '/usr/bin' + pathsep + '~/.ssh'  # ; on windows, : on unix
        self.profile_path = '/bin/xyzzy.txt' + pathsep + '/usr/bin/xyzzy.txt' + pathsep + '~/.ssh/id_rsa'  # ; on windows, : on unix


    def test_find_profile(self):
        profile = search_for_profile(self.profile_path)
        self.assertEqual(profile, "/Users/paulhanchett/.ssh/id_rsa", "Did not locate profile 'id_rsa'")


