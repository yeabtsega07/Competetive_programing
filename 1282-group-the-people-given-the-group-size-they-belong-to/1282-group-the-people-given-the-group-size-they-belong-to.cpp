class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> answer;
        for (int i = 0; i < groupSizes.size(); i++) {
            if (groupSizes[i] == 0) continue;
            else {
                vector<int> subvec;
                int elem = groupSizes[i];
                int count = elem;
                for (int j = i; j < groupSizes.size(); j++) {
                    if (groupSizes[j] == elem) {
                        subvec.push_back(j);
                        groupSizes[j] = 0;
                        count--;
                    }
                    if (count == 0) break;
                }
                answer.push_back(subvec);
            }
        }
        return answer;
    }
};
