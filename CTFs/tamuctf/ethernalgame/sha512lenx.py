import hashlib


def len_xtend(orig_msg, orig_hash, append_msg, keylen):
    pass




if __name__ == '__main__':
    orig_msg = 'a'
    key_len = None
    orig_hash = ''
    append_msg = 'b'

    print('Result message: ' + orig_msg + append_msg)

    if key_len == None:
        for i in range(20000):
            print(i, len_xtend(orig_msg, orig_hash, append_msg, i))
