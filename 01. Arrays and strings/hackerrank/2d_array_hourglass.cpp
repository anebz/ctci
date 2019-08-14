#include <bits/stdc++.h>

using namespace std;

int hourglass(vector<vector<int>> arr, int init_i, int init_j){
    int hourglass = 0;
    for (size_t i = init_i-1; i <= init_i+1; i++) {
        for (size_t j = init_j-1; j <= init_j+1; j++){
            if(i == init_i && (j != init_j)) continue;
            hourglass += arr[i][j];
        }
    }
    return hourglass;
}

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    int max_hourglass = -999;
    int res = 0;
    for (size_t i=1; i < arr.size(); i++){
        for (size_t j = 1; j < arr[0].size(); j++){
            res = hourglass(arr, i, j);
            if (res > max_hourglass) max_hourglass = res;
        }
    }
    return max_hourglass;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++)
    {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++)
        {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
