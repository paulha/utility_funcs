def strip_non_ascii(string):
    """Returns the string without non ASCII characters, L & R trim of spaces"""
    stripped = (c for c in string if ord(c) < 128 and c >=' ' and c<='~')
    return ''.join(stripped).strip(" \t\n\r").replace("  ", " ")

