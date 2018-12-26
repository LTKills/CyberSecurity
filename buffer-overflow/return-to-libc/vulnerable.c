#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[]) {
    char buf[1024];

    if(argc != 2) {
        printf("usage: %s [string]\n", argv[0]);
        return 1;
    }

    strcpy(buf, argv[1]);
    printf("%s\n", buf);

    return 0;
}
