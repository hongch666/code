#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 7;
int n, a[N], dp[N], INF = 0x3f3f3f3f;
vector<int> ans;

int main()
{
    memset(dp, INF, sizeof(dp));
    dp[0] = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= 540; j++)
        {
            if (dp[j] < a[i])
                dp[j ^ a[i]] = min(dp[j ^ a[i]], a[i]);
        }
    }
    for (int i = 0; i <= 540; i++)
    {
        if (dp[i] != INF)
            ans.push_back(i);
    }
    cout << ans.size() << endl;
    for (int i : ans)
        cout << i << " ";
    return 0;
}