
class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    # -- FIXME: This does NOT work as expected!

    def __getattr__(*args):
        val = dict.get(*args)
        return DotDict(val) if type(val) is dict else val

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__


"""
# -- Another implementation I found...
>>> class dotdict(dict):
...     """dot.notation access to dictionary attributes"""
...     __getattr__ = dict.get
...     __setattr__ = dict.__setitem__
...     __delattr__ = dict.__delitem__
... 
>>> mydict = {'val':'it works'}
>>> nested_dict = {'val':'nested works too'}
>>> mydict = dotdict(mydict)
>>> mydict.val
'it works'
>>> mydict.nested = dotdict(nested_dict)
>>> mydict.nested.val
'nested works too'
"""