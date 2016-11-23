#include <iostream>
#include <string>
#include <cmath>
#include <iomanip> // setw

using namespace std;

char* str_bin(unsigned x, char *str_bit, int sz)
{
	
	for(int ix=0; ix<sz; ix++) str_bit[ix] = '0';
	str_bit[sz] = '\0';

	int ix=sz;
	while(x>0) {
		str_bit[--ix] = (x&1) ? '1' : '0';
		x >>= 1;
	}
	return str_bit;
}


int main()
{
	int num_max = 32;
	int sz = ceil(log(num_max)*1./log(2));
	int sz_decimal = log10(num_max)+1;
	char str_bit[sz+1];
	for(unsigned int x=0; x<num_max; x++) {
		std::cout << "#" << setw(sz_decimal) << x ;
		std::cout << " gray: " << setw(sz_decimal) << (x ^ (x>>1));
		std::cout << " bin: " << str_bin(x ^ (x>>1),str_bit,sz);
		cout << std::endl;
	}
	return 1;
}
