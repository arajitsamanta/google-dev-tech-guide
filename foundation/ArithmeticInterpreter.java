
//https://codingbat.com/prob/p294185
class ArithmeticInterpreter {

    public static void main(String[] args) {
        String[] commands={"?","+","*","-"};
        int[] args1 = { 1,3,2 };
        interpret(0,commands,args1);
    }

    public static int interpret(int val, String[] commands, int[] args) {
        int n = commands.length;
        int result = val;
        for (int i = 0; i < n; i++) {
            switch (commands[i]) {
            case "+":
                result += args[i];
                break;
            case "-":
                result -= args[i];
                break;
            case "*":
                result *= args[i];
                break;
            default:
                return -1;
            }
        }
        return result;
    }
}