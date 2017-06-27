#!/bin/env python
from os.path import exists, join, abspath, expanduser
from os import pathsep
import yaml


def search_for_file(filename, search_list, **options):
    """Given a file and a search path, find file if it's on the path returning the absolute path and filename. 
    If a path component starts with '~' resolves to the user's home directory.
    """
    options['filename']=filename
    return search_for_profile(search_list, options=options)


def search_for_profile(search_list, func=None, options={}):
    """Given a search list of files, find the file if it's there, returning the absolute path and filename.
    If a path component starts with '~' resolves to the user's home directory.
    """
    paths = search_list.split(pathsep)
    filename = options['filename'] if 'filename' in options else None
    func = func if 'func' not in options else options['func']
    for path in paths:
        test_name = expanduser( join(path, filename) if filename != None else path )
        if exists(test_name):
            fname = abspath(test_name)
            return fname if func == None else func( fname, options )
    return None


def get_server_info( server_name, path_list="./config.yaml"+pathsep+"~/.jira/config.yaml" ):
        """
        Load Configuration from config.yaml

        Configuration may be held in either ~/.jira/config.yaml or ./config.yaml
        """
        # -- Locate the file
        file_path = search_for_profile( path_list )
        if file_path is None:
            raise FileNotFoundError
            return none

        # file_path None results in same error as "file not found"

        # -- Read the configuration
        with open( file_path, 'r') as file:
            # possible exception here if file can't be read...
            config = yaml.load( file )

        # -- New format, multiple servers
        section = {}
        if 'servers' in config:
            # Read from the servers subsection
            if server_name in config['servers']:
                section = config['servers'][server_name]
            else:
                raise KeyError("Name '%s' not found in servers" % server_name )
        else:
            raise KeyError("Missing 'servers' section")

        return section

#if __name__ == '__main__':

