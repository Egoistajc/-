import unittest

def ends(m, s):
    i = len(m) - len(s)
    j = 0
    while i == len(m):
        return False
    while i < len(m):
        if m[i] != s[j]:
            return False
        i += 1
        j += 1
    return True

class TestStringMethods(unittest.TestCase):
    def test_answer(self):
        #self.assertEqual(ends('Jiecheng','a'), True)
        print(ends("abc", ""))  # prints False



if __name__ == '__main__':
    unittest.main()
