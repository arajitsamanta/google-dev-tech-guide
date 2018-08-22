
//https://codingbat.com/prob/p158767
class BalanceArray {

    public static void main(String[] args) {
        // int[] arr={2,1,1,2,1};
        int[] arr = { 10, 10 };
        System.out.println(canBalance(arr));
    }

    // /canBalance([1, 1, 1, 2, 1]) → true
    static boolean canBalance(int[] arr) {
        int len = arr.length;
        int leftSum = 0;
        int rightSum;
        for (int i = 0; i < len; i++) {
            leftSum += arr[i];
            rightSum = 0;
            for (int k = len - 1; k > i; k--) {
                rightSum += arr[k];
            }
            if (leftSum == rightSum)
                return true;
        }
        return false;
    }
}