#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char *argv[]) {
    char buf[4];
    char larger[1024];

    scanf("%s", larger);
    strcpy(buf, larger);
    printf("%s\n", buf);

    return 0;
}
