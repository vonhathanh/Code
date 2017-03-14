#include <vector>
#include <iostream>

std::vector<int> countSmallerToTheRight(std::vector<int> nums) {
    std::vector<int> v(nums.size(),0);
    std::cout<<nums.size() - 1;
    for(int i = 0; i < -1; i++)
    {
        for(int j = i + 1; j < nums.size(); j++)
            if (nums[j] < nums[i])
                v[i]++;
    }
    return v;
}

int main()
{
	std::vector<int> t;
	t = countSmallerToTheRight(t);
	for(auto i:t)
		std::cout<<i<<" ";
	return 0;
}
