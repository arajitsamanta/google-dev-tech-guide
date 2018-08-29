import java.util.Map;
import java.util.HashMap;

//https://codingbat.com/prob/p238573
class EncodeStrings{

    public static void main(String[] args) {
        String[] raw={"a","b","a"};
        String[] codes={"1", "2", "3", "4"};
        encoder(raw,codes);
        // o/p → ["1", "2", "1"]
    }

    public static String[] encoder(String[] raw, String[] code_words) {
        Map<String,String> freq=new HashMap<String,String>();
        int n=raw.length;
        String key,code;
        for(int i=0;i<n;i++){
            key=raw[i];
            code=code_words[i];
            if(!freq.containsKey(key)){
                freq.put(key, code);
            }
            raw[i]=freq.get(key);
        }
        return raw;
    }
    
}