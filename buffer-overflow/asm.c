#include <stdio.h>
#include <stdlib.h>



void main() {
	__asm__("xor %eax, %eax");
	__asm__("movl %eax, (%esp)");
	__asm__("int $0x80");
}
