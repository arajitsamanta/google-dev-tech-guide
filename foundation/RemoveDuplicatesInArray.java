import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

import com.sun.javafx.collections.SortableList;

//https://codingbat.com/prob/p262890
class RemoveDuplicatesInArray {

    public static void main(String[] args){
        int[] a={1,2,2};
        sort(a);
    }

    static int[] sort(int[] a) {
        List<Integer> resultList = new ArrayList<>();
        int n = a.length;
        for (int i = 0; i < n; i++) {
            if(!resultList.contains(a[i])){
                resultList.add(a[i]);
            }
        }
        int resultSize=resultList.size();
        int[] result=new int[resultSize];
        for(int i=0;i<resultSize;i++){
            result[i]=resultList.get(i);
        }
        return  result;
    }

}
