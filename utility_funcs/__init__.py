def strip_non_ascii(string):
    """Returns the string without non ASCII characters, L & R trim of spaces"""
    stripped = (c for c in string if c >=' ' and c<='~')
    return ''.join(stripped).strip(" \t\n\r")replace("  ", " ")

