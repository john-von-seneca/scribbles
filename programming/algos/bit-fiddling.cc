#include <iostream>

int main()
{
	for(unsigned int x=0; x<32; x++) {
		std::cout <<  "x: " << x; 
		std::cout <<  " (x & (x-1)): " << (x & (x-1)); 
		std::cout <<  " (x & ~(x-1)) " << (x & ~(x-1));
		std::cout <<  " (x ^ (x>>1)) " << (x ^ (x>>1));
		std::cout << "" << std::endl;
	}
	return 1;
}
