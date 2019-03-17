#  Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import collections
import operator


class HNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def create_tree(fr):
    q = []
    for k, v in fr.items():
        q.append((v, k))
    while len(q) > 1:
        q.sort(key=operator.itemgetter(0), reverse=True)
        l, r = q.pop(), q.pop()
        node = HNode(l, r)
        q.append((l[0] + r[0], node))
    return q.pop()


def get_dict_codes(node, prefix="", codes={}):
    if isinstance(node[1].left[1], HNode):
        get_dict_codes(node[1].left, prefix+"0", codes)
    else:
        codes[node[1].left[1]] = prefix+"0"
    if isinstance(node[1].right[1], HNode):
        get_dict_codes(node[1].right, prefix+"1", codes)
    else:
        codes[node[1].right[1]] = prefix+"1"
    return codes


def huffman_encode(p_str):
    fr = collections.Counter(p_str)
    root = create_tree(fr)
    cd = get_dict_codes(root)
    res = []
    for ch in p_str:
        res.append(cd[ch])
    return " ".join(res)


s = "beep boop beer!"
enc_str = huffman_encode(s)

print("Строка:")
for i in s:
    print("{0:b}".format(ord(i)), end=" ")
print()
print("Сжатая строка:")
print(enc_str)
