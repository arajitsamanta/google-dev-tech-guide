
//https://codingbat.com/prob/p183562
class MakeBricks {

    public static void main(String[] args) {
        System.out.println(makeBricks(7, 1, 11));
    }

    static boolean makeBricks(int small, int big, int goal) {
        int bigLimit = big * 5;
        for (int i = 0; i <= bigLimit; i += 5) {
            for (int j = 0; j <= small; j++) {
                if (i + j == goal) {
                    return true;
                }
            }
        }
        return false;
    }
}