/* Let’s find the minimum of f(x) = (x – 1)2 using gradient descent */

#include <stdio.h>
#include <iostream>

float alpha=0.4, x=0.1, y ;
int iter=0 ;

float f(float x) 
{
	//return (x-1)*(x-1) ;
	return (x*x) + (2*x) - 3;
}
float derivative(float x) 
{
	//return 2 * (x-1) ;
	return (2*x) + 2;
}

int main(int argc, char **argv) 
{
	do 
	{
		iter++ ;
		y = f(x) ;
		printf ( "%5d x=%6.3f y=%6.3f\n", iter, x, y ) ;
		x -= alpha * derivative(x) ;
	} 
	while (iter < 20) ;
	
	return 0;
}