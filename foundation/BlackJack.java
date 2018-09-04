
//https://codingbat.com/prob/p117019
class BlackJack {

  public static void main(String[] args) {
    System.out.println(blackjack(19, 22));
  }

  public static int blackjack(int a, int b) {
    int target = 21;
    int result;
    int diffA = target - a;
    int diffB = target - b;

    if (diffA < 0 && diffB < 0) {
      result = 0;
    } else if (diffA < 0) {
      result = b;
    } else if (diffB < 0) {
      result = a;
    } else {
      if (diffA >= 0 && diffA < diffB) {
        result = a;
      } else {
        result = b;
      }
    }
    return result;
  }

}