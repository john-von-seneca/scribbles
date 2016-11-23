#include <iostream>
#include <string>
#include <cmath>
#include <iomanip> // setw

using namespace std;

void print_set(int n, bool* ba_present)
{
	cout << "{";
		for(int jx=0; jx<n; jx++) {
			if(ba_present[jx])
				cout << char(int('A')+jx) << ",";
		}
	cout << "}" << endl;
}

bool* init_ba_present(int n)
{
	bool* ba_present = new bool[n];
	for(int jx=0; jx<n; jx++) ba_present[jx] = false;
	return ba_present;
}

void init_ba_present(int n, bool** ba_present)
{
	*ba_present = new bool[n];
	for(int jx=0; jx<n; jx++) (*ba_present)[jx] = false;
}

void rprint(int n, int r, int ix=0, int count=0, bool* ba_present=nullptr)
{
	if(ix==0) {
		// ba_present = init_ba_present(n);
		init_ba_present(n, &ba_present);
		// ba_present = new bool[n];
		// for(int jx=0; jx<n; jx++) ba_present[jx] = false;
	}
	if(count==r) print_set(n, ba_present);
	if((count==r) || (ix==n)) return;
	
	for(int present=0; present<2; present++) {
		ba_present[ix] = (present==1);
		count += present;
		rprint(n, r, ix+1, count, ba_present);
	}
	ba_present[ix] = false;
	
	if(ix==0)
		delete[](ba_present);
}

int main()
{
	int n, r;
	cout << "n r" << endl;
	cin >> n;
	cin >> r;
	rprint(n, r);
	return 1;
}
