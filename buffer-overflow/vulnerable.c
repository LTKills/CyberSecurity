#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/mman.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
	char buf[1024];
	mprotect((void*) 0xbffff880, 1024, PROT_READ | PROT_WRITE | PROT_EXEC);
	gets(buf);	
	printf("%s\n", buf);
	return 0;
}
