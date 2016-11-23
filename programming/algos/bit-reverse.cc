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

unsigned int reverse_bits(int x, int sz)
{
	int y=0;
	for(int ix=0; ix<sz; ix++) {
		y |= (x & 1);
		x >>= 1;
		y <<= 1;
	}
	return y;
}

int main()
{
	int num_max = 32;
	int sz = ceil(log(num_max)*1./log(2));
	int sz_decimal = log10(num_max)+1;
	char str_bit[sz+1];
	unsigned int int_r;
	for(unsigned int x=0; x<num_max; x++) {
		std::cout << "#" << setw(sz_decimal) << x ;
		std::cout << "  bin: " << str_bin(x,str_bit,sz);
		int_r = reverse_bits(x,sz-1);
		std::cout << " r:" << setw(sz_decimal) << int_r;
		std::cout << " binr: " << str_bin(int_r,str_bit,sz);
		cout << std::endl;
	}
	return 1;
}
