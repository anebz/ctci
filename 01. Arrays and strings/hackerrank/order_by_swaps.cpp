/*

# Minimum Swaps 2

https://www.hackerrank.com/challenges/minimum-swaps-2/problem

You are given an unordered array consisting of consecutive integers

[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array arr = [7,1,3,2,4,5,6] we perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

It took 5 swaps to sort the array.
*/

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the minimumSwaps function below.
int minimumSwaps2(vector<int> arr)
{
    int swaps = -1;
    vector<bool> vis(arr.size(), false);
    for (size_t i = 0; i < arr.size(); i++)
    {
        if (vis[i] || arr[i] == i + 1)
        {
            vis[i] = true;
            continue;
        }
        int val = arr[i];
        while (!vis[val - 1])
        {
            vis[val - 1] = true;
            val = arr[val - 1];
            swaps++;
        }
    }
    return swaps;
}

// numbers don't necessarily need to be consecutive, could be 1,2,3,77,88,6
int minimumSwaps(vector<int> arr){
    int first = 0;
    int last = arr.size() - 1;
    int swaps = 0;
    while (first < last){
        while (arr[first] == first + 1 && first < last){
            first++;
        }
        if (first < last){
            int temp = arr[arr[first] - 1];
            arr[arr[first] - 1] = arr[first];
            arr[first] = temp;
            swaps++;
        }
    }
    return swaps;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int res = minimumSwaps(arr);

    fout << res << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string)
{
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ')
    {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos)
    {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
