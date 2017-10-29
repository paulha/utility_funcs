from unittest import TestCase

from utility_funcs.dot_access import DotDict

class Test_dot_access(TestCase):
    def setUp(self):
        pass

    def test_can_access_as_dict(self):
        item = {}
        item['one'] = 1
        test1 = DotDict(item)
        self.assertEqual(test1.one, item['one'], "wrong value for item['one'] = %s" % item['one'])

    def test_can_update_as_dict(self):
        item = {}
        item['one'] = 1
        test1 = DotDict(item)
        test1.one = 2
        self.assertEqual(test1.one, 2, "wrong value for item['one'] = %s, should be 2" % item['one'])
        # -- Expect item to have been set, too:
        self.assertEqual(item['one'], 2, "wrong value for item['one'] = %s, should be 2" % item['one'])

    def test_can_create_new_entry(self):
        item = {}
        item['one'] = 1
        test1 = DotDict(item)
        test1.three = 3
        self.assertEqual(test1.three, 3, "wrong value for test1,three = %s, should be 3" % test1.three)
        # -- Expect item to have been set, too:
        self.assertEqual(item['three'], 3, "wrong value for item['three'] = %s, should be 3" % item['three'])

