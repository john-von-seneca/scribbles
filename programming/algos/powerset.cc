#include <iostream>
#include <string>
#include <cmath>
#include <iomanip> // setw

using namespace std;

void rprint(int sz, int ix=0, bool* ba_present=nullptr)
{
	if(ix==0) {
		ba_present = new bool[sz];
		for(int jx=0; jx<sz; jx++) ba_present[jx] = false;
	}
	if(ix==sz) {
		cout << "{";
		for(int jx=0; jx<sz; jx++) {
			if(ba_present[jx])
				cout << char(int('A')+jx) << ",";
		}
		cout << "}" << std::endl;
		return;	  
	}
	for(int present=0; present<2; present++) {
		ba_present[ix] = (present==1);
		rprint(sz, ix+1, ba_present);
	}
	
	if(ix==0)
		delete(ba_present);
}

void rprint2(int sz, int ix=-2, bool* ba_present=nullptr)
{
	if(ix==-2) {
		ba_present = new bool[sz];
		for(int jx=0; jx<sz; jx++) ba_present[jx] = false;
		ix = sz-1;
	}
	if(ix==-1) {
		cout << "{";
			for(int jx=0; jx<sz; jx++) {
				if(ba_present[jx])
					cout << char(int('A')+jx) << ",";
			}
		cout << "}" << std::endl;
		return;	  
	}
	for(int present=0; present<2; present++) {
		ba_present[ix] = (present==1);
		rprint2(sz, ix-1, ba_present);
	}
	
	if(ix==(sz-1))
		delete(ba_present);
}


int main()
{
	int sz_set;
	cin >> sz_set;
	rprint(sz_set);
	rprint2(sz_set);
	return 1;
}
