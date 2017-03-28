#include <iostream>

int isqrt(int num) {
    int res = 0;
    int bit = 1 << 30; // The second-to-top bit is set: 1 << 30 for 32 bits

    std::cout << "bit: " << bit << std::endl; 
    // "bit" starts at the highest power of four <= the argument.
    while (bit > num)
        bit >>= 2;
        
    std::cout << "bit: " << bit << std::endl; 
    
    while (bit != 0) {
        if (num >= res + bit) {
            std::cout << "num " << num << " >= res+bit " << res + bit << std::endl;
            num -= res + bit;
            res = (res >> 1) + bit;
        }
        else {
            std::cout << "num " << num << " < res+bit " << res + bit << std::endl;
            res >>= 1;
        }
        bit >>= 2;
        std::cout << "num " << num << ", res: " << res << ", bit: " << bit << std::endl;
    }
    return res;
}

int main(int args, char* argv[])
{
  std::cout << "#args: "  << args <<  "  -- " << argv[0] << ", " << argv[1] << std::endl;
  int num = std::atoi(argv[1]);
  std::cout << "sqrt(" << num << ") = " << isqrt(num) << std::endl;
  return 0;
}

