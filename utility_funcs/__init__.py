import string

def strip_non_ascii(string):
    """Returns the string without non ASCII characters, L & R trim of spaces"""
    stripped = (c for c in string if c >=' ' and c<='~')
    return string.replace(''.join(stripped).strip(" \t\n\r"), "  ", " ")

