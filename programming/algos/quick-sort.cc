#include <iostream>
#include <string>
#include <cmath>
#include <iomanip> // setw
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

int* get_array(int &n)
{
	cout << "n: "; cin >> n;
	int* elements = (int*)calloc(n, sizeof(int));
	srand (time(NULL));
	for(int ix=0; ix<n; ix++)
		elements[ix] = rand() % (3*n);
	return elements;
}
void print_elements(int n, int* elements, int ix_start=-2, int ix_end=-2, int ix_pivot=-2, string str_prefix="")
{
	ix_start = (ix_start==-2) ? 0   : ix_start;
	ix_end   = (ix_end==-2)   ? n-1 : ix_end;
	cout << str_prefix << "[";
	for(int ix=0; ix<=ix_end; ix++) {
		cout << ((ix_pivot==ix) ? "*" : "") << elements[ix] << ", ";
	}
	cout << "}" << std::endl;
}

	void swap(int *elements, int ix1, int ix2)
{
	int tmp = elements[ix1];
	elements[ix1] = elements[ix2];
	elements[ix2] = tmp;
}

int quicksort(int n, int *elements, int ix_start=0, int ix_end=-2, string str_prefix="")
{
	ix_end = (ix_end==-2) ? n-1 : ix_end;
	if(ix_start >= ix_end) return 0;

	cout << str_prefix << ": " << ix_start << " -> " << ix_end << endl;
	int num_calls = 1;
	
	// pivot: first element
	// swap first and last elements
	int sz_current = ix_end-ix_start+1;
	int ix_pivot = rand() % sz_current + ix_start;

	swap(elements, ix_pivot, ix_end);
	int pivot = elements[ix_end];
	// points to the head/start of the bigger ones
	int head=ix_start;
	for(int ix_ptr=ix_start; ix_ptr<ix_end; ix_ptr++) {
		if(elements[ix_ptr] <= pivot) {
			swap(elements, head, ix_ptr);
			++head;
		}
	}
	swap(elements, head, ix_end);
	print_elements(n, elements, ix_start, ix_end, head, str_prefix);
	num_calls += quicksort(n, elements, ix_start, head-1, str_prefix + "  ");
	num_calls += quicksort(n, elements, head+1,   ix_end, str_prefix + "  ");
	return num_calls;
}

int main()
{
	int n;
	int *elements = get_array(n);
	srand(time(NULL));
	print_elements(n, elements);
	int num_calls = quicksort(n, elements);
	cout << endl << endl;
	cout << "num-calls: " << num_calls << endl;
	print_elements(n, elements);

	cout << endl;
	free(elements);
	return 1;
}
