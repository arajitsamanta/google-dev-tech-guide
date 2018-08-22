

public class RemoveStrings{

    public static void main(String[] args){
        //System.out.println(withoutString("Hello there","Llo"));
        //System.out.println(withoutString("Hello there","e"));
        //System.out.println(withoutString("This is a FISH","IS"));
        System.out.println(withoutString("xxx","xx"));
    }

    static String withoutString(String base,String remove){
        String lowerRemove=remove.toLowerCase();
        int idx=-1;
        int removeLength=remove.length();
        while(true){
            String lowerBase=base.toLowerCase();
            idx=lowerBase.indexOf(lowerRemove);
            if(idx<0)
                break;
            else{
               String temp=findAndCut(base,idx, removeLength);
                base=temp;
                if(base.equalsIgnoreCase(remove)){
                    base="";
                }
            }
        }

        return base;

    }

    static String findAndCut(String base,int startIndex,int removeLength){
        StringBuilder temp=new StringBuilder();
        temp.append(base.substring(0, startIndex)).append(base.substring(startIndex+removeLength));

       if(temp.length()==0)
        temp.append(base);

       return temp.toString();
    }
}