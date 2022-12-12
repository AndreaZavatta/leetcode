class Solution {
    public boolean isPalindrome(int x) {
        int r,temp, sum=0;   
        int n = x;
        while (n>0){
            r = n%10;
            sum = sum*10 + r;
            n = n/10;
        }
        return sum == x;
    }
}