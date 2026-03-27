class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l=nums.size();

        for(int i=0; i<l;i++)
        {
          if(target == nums[i]){
            return i;
          }
          else if((nums[i] < target) && ( (i+1)>l-1 )){
            return i+1;
          }
          else if((nums[i] < target) && (nums[i+1]>target)){
            return i+1;
          }
        }
        return 0;
    }
};