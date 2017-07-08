#!/usr/local/bin/python3
import unittest
import huffman

class huffman_ut(unittest.TestCase):

    def test_string2freq(self):
        test_string = 'aaaabbbc'
        test_dict = [(4, 'a'), (3, 'b'), (1, 'c')]
        sample = huffman.string2freq(test_string)
        self.assertCountEqual(sample, test_dict)

    def test_encodeString(self):
        test_string = 'aaaabbbc'
        test_t = {'a':'0', 'b':'10', 'c':'11'}
        test_answer = '000010101011'
        sample = huffman.encodeString(test_string, test_t)
        self.assertEqual(test_answer, sample)

    def test_decodeString(self):
        test_codebook = {'a':'0', 'b':'10', 'c':'11'}
        test_encoding = '000010101011'
        test_original_msg = 'aaaabbbc'
        sample = huffman.decodeString(test_encoding, test_codebook)
        self.assertEqual(test_original_msg, sample)

    def test_huffmanEncode(self):
        test_string = 'aaaabbbc'
        test_codebook = {'a':'0', 'b':'10', 'c':'11'}
        sample = huffman.huffmanEncode(huffman.string2freq(test_string))
        self.assertEqual(test_codebook, sample)

if __name__ == "__main__":
    unittest.main()




