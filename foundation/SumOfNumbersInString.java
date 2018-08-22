
//https://codingbat.com/prob/p121193
public class SumOfNumbersInString {

    public static void main(String[] args) {
        // sumNumbers("abc123xyz");
        sumNumbers("7 11");
    }

    static int sumNumbers(String str) {
        char[] arr = str.toCharArray();
        int len = arr.length;
        int sum = 0;
        int j;
        for (int i = 0; i < len; i++) {
            if (Character.isDigit(arr[i])) {
                StringBuilder buf = new StringBuilder();
                for (j = i; j < len; j++) {
                    if (Character.isDigit(arr[j])) {
                        buf.append(arr[j]);
                    } else {
                        int number = Integer.parseInt(buf.toString());
                        sum += number;
                        i = j;
                        break;
                    }
                }
                if (j == len) {
                    sum += Integer.parseInt(buf.toString());
                    i = j;
                }
            }
        }
        return sum;
    }

}
