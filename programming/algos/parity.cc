#include <iostream>

int main()
{
	unsigned int x, result=0;
	std::cin >> x;
	while(x) {
		result ^= (x & 1);
		x >>= 1;
	}
	std::cout << "x: " << x << " parity: " << result << std::endl;
	return 1;
}
