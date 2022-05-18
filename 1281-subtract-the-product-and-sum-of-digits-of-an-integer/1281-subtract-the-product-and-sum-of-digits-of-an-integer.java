class Solution {
    public int subtractProductAndSum(int n) {
        //time = 0(log(n)) space = O(1)
        //n = 234
        int sum = 0;
        int product = 1;
        while (n > 0){
            //234
            //4
            int digit = n % 10;
            sum += digit;
            product *= digit;
            n /= 10;
            //n = 23
        }
        return product - sum;
    }
}