#include <iostream>
#include <sstream> // ostringstream
#include <string>
#include <cmath>
#include <iomanip> // setw

using namespace std;

int str_to_int(string str_in)
{
	int n=0, sz_str=str_in.size(), curr_val, char_val;
	for(int ix=0; ix<sz_str; ix++) {
		cout << str_in[ix] << ": " << int(str_in[ix]) << ", ";
		char_val = int(str_in[ix]);
		if(char_val<48 || char_val>57) {
			ostringstream ss_err;
			ss_err << "char val " << char_val << " of '" << str_in[ix] << "' in position " << ix << " not in range [48,57]";
		}
		curr_val = char_val-48;
		n *= 10;
		n += curr_val;
	}
	cout << endl;
	return n;
}


int main()
{
	string str_in;
	cout << "enter the str: " << endl;
	cin >> str_in;
	int n = str_to_int(str_in);
	cout << "n: " << n << endl;
	return 1;
}
