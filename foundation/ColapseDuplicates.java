
//https://codingbat.com/prob/p256268
class ColapseDuplicates {

    public static void main(String[] args) {
        collapseDuplicates("abbbcaaa");
    }

    static String collapseDuplicates(String a) {
        int i = 0;
        String result = "";

        while (i < a.length()) {
            char ch = a.charAt(i);
            result += ch;
            while (i + 1 < a.length() && a.charAt(i + 1) == ch) {
                i++;
            }
            i++;
        }
        return result;
    }
}