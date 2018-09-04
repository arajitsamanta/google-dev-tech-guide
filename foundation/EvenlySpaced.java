
import java.lang.Math;

class EvenlySpaced {

    public static void main(String[] args) {
        System.out.println(isEvenlySpaced(6,2,4));
    }

    static boolean isEvenlySpaced(int a, int b, int c) {
        // Find max
        int max = a > b ? a : b;
        max = c > max ? c : max;

        // Find min
        int min = a < b ? a : b;
        min = c < min ? c : min;

        int middle;
        if(a!=max && a !=min)
            middle=a;
        else if(b!=max && b !=min)
            middle=b;
        else
            middle=c;

        int sub1 = max - middle;
        int sub2 = middle - min;
        if (sub1 == sub2)
            return true;

        return false;
    }
}