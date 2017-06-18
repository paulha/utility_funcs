#!/bin/env python
from os.path import exists, join, abspath, expanduser
from os import pathsep

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

#if __name__ == '__main__':

