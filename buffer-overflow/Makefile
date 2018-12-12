all:
	gcc vulnerable.c -o vulnerable -fno-stack-protector -std=c99 -m32 -g -z execstack
	gcc asm.c -o asm -fno-stack-protector -std=c99 -m32 -g -z execstack
