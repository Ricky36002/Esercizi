def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())


import unittest

def anagram(s, t):
    return sorted(s) == sorted(t)

class TestAnagramFunction(unittest.TestCase):

    def read_input_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
        return lines[0], lines[1]

    def write_output_file(self, filename, result):
        with open(filename, 'w') as file:
            file.write(str(result))

    def test_anagram_case1(self):
        s, t = self.read_input_file('input1.txt')
        result = anagram(s, t)
        self.write_output_file('output1.txt', result)
        self.assertTrue(result)

    def test_anagram_case2(self):
        s, t = self.read_input_file('input2.txt')
        result = anagram(s, t)
        self.write_output_file('output2.txt', result)
        self.assertTrue(result)

    def test_anagram_case3(self):
        s, t = self.read_input_file('input3.txt')
        result = anagram(s, t)
        self.write_output_file('output3.txt', result)
        self.assertFalse(result)

    def test_anagram_case4(self):
        s, t = self.read_input_file('input4.txt')
        result = anagram(s, t)
        self.write_output_file('output4.txt', result)
        self.assertTrue(result)

    def test_anagram_case5(self):
        s, t = self.read_input_file('input5.txt')
        result = anagram(s, t)
        self.write_output_file('output5.txt', result)
        self.assertFalse(result)
    
if __name__ == '__main__':
    unittest.main()
