public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> dictionary = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            int secondValue = target - nums[i];

            if (dictionary.ContainsKey(secondValue))
            {
                int[] arr = new int[2];
                arr[0] = i;
                arr[1] = dictionary[secondValue];
                return arr;
            }
            else if (!dictionary.ContainsKey(nums[i]))
            {
                dictionary.Add(nums[i], i);
            }

        }
        return null;
    }
}