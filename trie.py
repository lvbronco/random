_end = '_end_'

def make_trie(word, root=dict()):
    current_dict = root
    for letter in word:
        current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
    return root

trie = dict()
print make_trie('foo', trie)
print make_trie('bar', trie)
print make_trie('baz', trie)
print make_trie('barz', trie)