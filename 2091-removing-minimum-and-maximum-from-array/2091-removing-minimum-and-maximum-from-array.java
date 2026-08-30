class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;
        int idxmx = 0, idxmn = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[idxmx]) idxmx = i;
            if (nums[i] < nums[idxmn]) idxmn = i;
        }

        int a = Math.max(idxmx, idxmn) + 1;
        int b = n - Math.min(idxmx, idxmn);
        int c = idxmx + 1 + n - idxmn;
        int d = idxmn + 1 + n - idxmx;

        return Math.min(Math.min(a, b), Math.min(c, d));
    }
}