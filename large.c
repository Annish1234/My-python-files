#include<stdio.h>
int main() {
	int num1, num2, num3;
	printf("Enter the value for num1, num2, num3\n");
	scanf("%d %d %d ",& num1, & num2, &num3);
	if ((num1>num2)&&(num1>num3))
		printf("\n number1 is greater");
	else if ((num2>num3)&&(num2>num1))
		printf(" number2 is greater");
	else 
            printf("\n number3 is greater");
}
