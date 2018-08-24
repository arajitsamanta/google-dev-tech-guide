import java.util.Map;
import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

//https://codingbat.com/prob/p148813
class MapShare {

    public static void main(String[] args) {
        Map<String, String> input = new HashMap<>();
        //input.put("a", "aaa");
        input.put("b", "xyz");
        input.put("c", "ccc");

        MapShare obj = new MapShare();

        Map<String, String> op = obj.mapShare(input);
        op.forEach((k, v) -> {
            System.out.println(k + " " + v);
        });
    }

    public Map<String, String> mapShare(Map<String, String> map) {
        Map<String, String> resultMap = new HashMap<>();
        for (String key : map.keySet()) {
            switch (key) {
            case "a":
                String val = map.get(key);
                resultMap.put(key, val);
                if (null != val) {
                    resultMap.put("b", val);
                }
                break;
            case "b":
                if(!resultMap.containsKey(key))
                    resultMap.put(key, map.get(key));
                break;
            case "c":
                break;
            default:
                resultMap.put(key, map.get(key));
            }
        }
        return resultMap;
    }
}