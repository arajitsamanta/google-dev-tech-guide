import java.util.Map;
import java.util.HashMap;

//https://codingbat.com/prob/p117630
class PairsMap{

    public static void main(String[] args) {
        String[] input={"code","bug"};
        pairs(input);
    }


    public static Map<String, String> pairs(String[] strings) {
       int len=0;
       Map<String,String> result=new HashMap<String,String>();
       for(String temp:strings){
            len=temp.length();
            result.put(temp.substring(0, 1), temp.substring(len-1));
       }
       return result;
    }

 }
