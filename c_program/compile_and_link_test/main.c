#include <stdio.h>
#include "op.h"

int main(void)
{
    int a, b;
    printf("enter two numbers to add\n");
    scanf("%d%d", &a, &b);
    printf("sum of entered numbers = %d\n", add(a, b));

#ifdef TEST
    printf("Program End\n");
#endif

    return 0;
}


