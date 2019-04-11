#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int maxSubArraySum(vector<int> a, int size)
{
  int max_so_far = 0, max_ending_here = 0;
  for(int i = 0; i<size; i++){
    max_ending_here = max_ending_here + a[i];
    if(max_ending_here < 0) max_ending_here = 0;
    else if(max_so_far < max_ending_here) max_so_far = max_ending_here;
  }
  return max_so_far;
}

int main()
{
  unsigned int testcases, n = 0;
  cin >> testcases;
  while(testcases--){
    cin >> n;
    vector<int> x(n);
    int cont = 0, noncont = 0, negmaxpos, negmax = 0;
    for(size_t i = 0; i<n; ++i){
      cin >> x[i];
      if(x[i] > 0) noncont += x[i];
      if(x[i] < negmax){
        negmaxpos = i;
        negmax = x[i];
      } 
    }
    if(n == 1){
      cont = x[0]; noncont = cont;
    }else if(negmax == 0) cont = noncont; // all positive
    else if(noncont == 0){  // all negative
      sort(x.begin(),x.end());
      cont = x[n-1]; noncont = cont;
    }else cont = maxSubArraySum(x,n);
    cout << cont << " " << noncont << endl;
  }
  return 0;
}
