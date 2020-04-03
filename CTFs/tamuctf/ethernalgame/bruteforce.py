import hashlib
import sys
import threading

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 'a17b713167841563563ac6903a8bd44801be3c0fb81b086a4816ea457f8c829a6d5d785b49161972b7e94ff9790d37311e12b32221380041a99c16d765e8776c'

def tryhard(key, size, end):
    if len(key) == size:
        if hashlib.sha512((key+end).encode()) == ans:
            print('FOUND!!!!', end=': ')
            print(hashlib.sha512(key+end))
            print(key)
            sys.exit(0)
        print(key)
        return

    for c in alphabet:
        tryhard(key+str(c), size, end)

if __name__ == '__main__':
    max_size = 11

    sys.setrecursionlimit(100)

    for i in range(1, max_size):
        x = threading.Thread(target=tryhard, args=('', i, '1'))
        x.start()
