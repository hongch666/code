#include <stdio.h>
#include <stdlib.h>
int fib(int n)
{
    /* 求fib数 */
    if(n==1||n==2)
        return 1;
    return fib(n-2)+fib(n-1);
}
int main()
{
    char a;
    a =':';
    printf("%d\n",fib(6));
    return 0;
}
// 666