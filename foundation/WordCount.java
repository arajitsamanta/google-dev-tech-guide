
import java.util.Map;
import java.util.HashMap;


//https://codingbat.com/prob/p117630
class WordCount{
    public static void main(String[] args) {
        String[] input={"a","b","c","a"};
        wordCount(input);
    }

    public static Map<String, Integer> wordCount(String[] strings) {
        Map<String,Integer> result=new HashMap<String,Integer>();
        for(String temp:strings){
            Integer val=result.get(temp);
            if(null==val){
                result.put(temp, 1);
            }else{
                val++;
                result.put(temp, val);
            }          
        }
        return result;
    }
    
}