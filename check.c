#include<stdio.h>
void main()
{
	int num;
	printf("Enter a number\n");
	scanf("%d",&num);
	if(num>0)
		printf("%d is postive number:\n",num);
	else if (num<0)
		printf("%d is negative number:\n",num);
        else
            printf ("number is 0");
}
