class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> noDuplicate = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if (noDuplicate.contains(nums[i])){
                return true;
            } else {
                noDuplicate.add(nums[i]);
            }
            
        }
        return false;
    }
}