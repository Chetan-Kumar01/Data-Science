// #include <iostream>
// using namespace std;

// // check if there exists a subsequence of size k
// // whose median >= x
// bool canHaveMedian(vector<int>& a, int k, int x) {
//     int cnt = 0;
//     for (int i=0;i<a.size();i++) {
//         if (a[i] >= x) cnt++;
//     }
//     // median >= x possible if we can place x at median position
//     return cnt >= (k + 1) / 2;
// }

// vector<int> findMinMaxMedian(vector<int>& values, int k) {
//     sort(values.begin(), values.end());
//     int n = values.size();

//     // ---------- minimum median ----------
//     int low = values[0], high = values[n - 1];
//     int minMedian = values[n - 1];

//     while (low <= high) {
//         int mid = low + (high - low) / 2;
//         if (canHaveMedian(values, k, mid)) {
//             minMedian = mid;
//             high = mid - 1;
//         } else {
//             low = mid + 1;
//         }
//     }

//     // ---------- maximum median ----------
//     low = values[0], high = values[n - 1];
//     int maxMedian = values[0];

//     while (low <= high) {
//         int mid = low + (high - low) / 2;
//         if (canHaveMedian(values, k, mid)) {
//             maxMedian = mid;
//             low = mid + 1;
//         } else {
//             high = mid - 1;
//         }
//     }

//     return {minMedian, maxMedian};
// }

// int main() {
//     vector<int> values = {10, 20, 30, 40};
//     int k = 3;

//     auto ans = findMinMaxMedian(values, k);

//     cout << "Minimum Median: " << ans[0] << endl;
//     cout << "Maximum Median: " << ans[1] << endl;

//     return 0;
// }
#include <iostream>
 using namespace std;

vector<int> findMinMaxMedian(vector<int>& values, int k) {
    int n = values.size();
    
    // Step 1: sort the array
    sort(values.begin(), values.end());

    // Step 2: median index for subsequence of size k (0-based)
    int mid = (k - 1) / 2;

    // Step 3: minimum and maximum median
    int minMedian = values[mid];
    int maxMedian = values[n - (k - mid)];

    return {minMedian, maxMedian};
}

int main() {
    vector<int> values = {10, 20, 30, 40};
    int k = 3;

    vector<int> ans = findMinMaxMedian(values, k);

    cout << "Minimum Median: " << ans[0] << endl;
    cout << "Maximum Median: " << ans[1] << endl;

    return 0;
}
