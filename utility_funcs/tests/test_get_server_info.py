from unittest import TestCase
import unittest.mock

from utility_funcs.search import *

from os import pathsep

print
print(__name__)
print

class TestGetServerInfo(TestCase):
    yaml_text = """#
    # -- Change to enable server dependent stuff to be saved in the authentication file:
    #
    servers:
        jira-t2:
            host:     'This is a funky name'
            verify:   'IntelSHA256RootCA-Base64.crt'
            username: 'pfhanchx'
            password: 'xxxxxxxxxx'

        jira01:
            host:     'https://jira01.devtools.intel.com'
            verify:   'IntelSHA256RootCA-Base64.crt'
            username: 'pfhanchx'
            password: 'xxxxxxxxxx'

        jira-stg:
            host:     'http://jira-stg.ostc.intel.com:8080'
            verify:   'IntelSHA256RootCA-Base64.crt'
            username: 'pfhanchx'
            password: 'xxxxxxxxxx'

    """

    def setUp(self):
        pass

    # -- Check that get_server_info raises FileNotFoundError is the configuration file is not located.
    @unittest.mock.patch('utility_funcs.search.search_for_profile')
    def test_get_server_info_no_file(self, mock_search):
        mock_search.return_value = None
        with unittest.mock.patch('builtins.open', unittest.mock.mock_open(), create=True) as mocked_open:
            mocked_open.side_effect = FileNotFoundError()
            section = self.assertRaises(FileNotFoundError, get_server_info, "no_server" )
            self.assertIsNone( section )

    # -- Check that correct server section and values are returned
    @unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data=yaml_text))
    @unittest.mock.patch('utility_funcs.search.search_for_profile')
    def test_get_server_info(self, mock_search):
        # (pretend we found a file)
        mock_search.return_value = "dummy"
        section = get_server_info("jira-t2")
        self.assertDictEqual(section,
                             {'config_directory': '',
                              'host': 'This is a funky name',
                              'password': 'xxxxxxxxxx',
                              'username': 'pfhanchx',
                              'verify': 'IntelSHA256RootCA-Base64.crt'},
                             "Did not read expected values")

