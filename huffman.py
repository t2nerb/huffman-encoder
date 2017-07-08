#!/usr/local/bin/python3
from math import log as lg

# For debugging, set to true to see all prints, otherwise set to false
verbose = False

class Node(object):
    """
    Object representing a node with left and right children
    """
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class PriorityQ(object):
    """
    Object containing our priority queue with methods deletemin and
    insert that cost O(logn)
    """
    def __init__(self, mylist=[]):
        self.list = mylist
        self.length = 0

    def insert(self, item):
        """
        Push item onto heap, maintaining the heap invariant.
        : param item: element to insert into our heap
        """
        for i in range(self.length):
            if item[0] <= self.list[i][0]:
                self.list.insert(i, item)
                if (verbose): print('inserted: ', item, ' at index', i)
                self.length += 1
                return
        self.list.append(item)
        if (verbose): print('appended: ', item, ' at index ', len(self.list)-1)
        self.length += 1

    def deletemin(self):
        """
        Delete and return the highest priority element.
        """
        low = self.list.pop(0)
        self.length -= 1
        return low

def build_codebook(node, charset, prefix="", code={}):
    """
    Build the huffman codebook given root node in a huffman
    tree
    : param node: <class> object representing a node with left/right children
    : param charset: set containing all characters to encode
    : param prefix: <string> path to the current node in huffman tree
    : param code: <dict> Contains the dictionary where each key is the letter,
                  and each value is the huffman encoding.

    : return: <dict> Each key is a letter and value is the letter's frequency.
    """
    # If current node is a leaf node, add prefix to code dictionary
    if node[1] in charset:
        code[node[1]] = prefix
        if len(code) == len(charset):
            return code

    # if current node is non-leaf node, recurse on children nodes
    # and append to prefix to reflect traversal through the tree
    else:
        prefixl = prefix + '1'
        prefixr = prefix + '0'
        code = build_codebook(node[1].left, charset, prefixl, code)
        code = build_codebook(node[1].right, charset, prefixr, code)

    return code


def string2freq(x):
    """
    Return letters and their frequency from the string 'x'
    : param x: <string> ASCII string to find letters and frequencies
    : return: List of tuples indicating letter and it's frequency
    """
    lettercounts = {}
    for ch in x:

        # if ch exists as key in lettercounts, increment by 1
        if ch in lettercounts: lettercounts[ch] += 1

        # if ch doesn't exist as key in lettercounts, initilize key as 1
        else: lettercounts[ch] = 1

    # return list of tuples in format (frequency, character)
    return [(lettercounts[y], y) for y in lettercounts]

def encodeString(x, t):
    """
    Given an ASCII string x and codebook T, return the huffman encoding
    of x using t.
    : param x: <string> our ASCII string to encode
    : param t: <dict> the dictionary codebook to encode x
    : return: <str> containing huffman encoded x using codebook t
    """
    enc = ''
    # for each character in x, append the encoding of the char to enc
    for ch in x:
        enc += t[ch]
    return enc

def decodeString(enc_message, codebook):
    """
    Given an encoded binary string, decode the message with the code given by
    codebook.
    : param enc_message: <string> Contains the huffman encoded string to decode
    : param codebook: <HashObject> Contains the codebook where each key is a
                      letter and each value corresponds to the letter's huffman
                      encoding.
    : return: <str> The decoding of the encoded string. 
    """
    chunk = ''
    dec_message = ''
    for char in enc_message:
        chunk += char
        for key, value in codebook.items():
            if chunk == value:
                dec_message += key
                chunk = ''
    return dec_message

def huffmanEncode(lc):
    """
    Return dictionary T that represents Huffman encoding book for each
    character in lc
    : param lc: <list> list containing tuples of format (frequency, letter)
    : return: <dict> Huffman encoding codebook with letter and frequency given
              by param lc
    """

    priority_q = PriorityQ()

    # insert each element in our list containing letters and frequencies
    # into our priorityQ object
    for freq, ch in lc:
        priority_q.insert((freq, ch))

    # Loop until all nodes have been merged into a root node
    while priority_q.length > 1:

        # get two smallest elements in our priority queue
        i, j = priority_q.deletemin(), priority_q.deletemin()

        # merge two smallest elements into single node
        new_node = Node(i, j)

        # add our new node and the total freq count into priority queue
        priority_q.insert((i[0]+j[0], new_node))

    # get root node
    root = priority_q.deletemin()

    # create set so we can ensure we find encoding path for each char
    charset = set(x[1] for x in lc)
    codebook = build_codebook(root, charset)

    return codebook

if __name__ == "__main__":
    # read in our data file consisting of Frost poem
    with open('data.txt', 'r') as myfile:
        data=myfile.read().replace('\n', ' ').lower()

    codebook = huffmanEncode(string2freq(data))
    encoded_string = encodeString(data, codebook)
    decoded_string = decodeString(encoded_string, codebook)

    print('\nOriginal message:\n{}\n'.format(data))
    print('Codebook: \n{}\n\nEncoded string:\n{}\n'.format(codebook, encoded_string))
    print('Length of encoded string:\n{}\n'.format(len(encoded_string)))
    print('Decoded string:\n{}\n'.format(decoded_string))














