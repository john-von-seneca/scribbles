#include <iostream>
#include <string>
#include <cmath>
#include <iomanip> // setw
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

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
	int n; cout << "n: "; cin >> n;
	srand(time(NULL));
	
	return 1;
}
