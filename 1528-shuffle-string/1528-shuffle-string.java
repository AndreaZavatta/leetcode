class Solution {
    public String restoreString(String s, int[] indices) {
        char[] arr = new char[indices.length];
        String temp="";
        for(int i=0;i<indices.length;i++){
            arr[indices[i]] = s.charAt(i);
        }
        for(char i: arr){
            temp+=i;
        }
        
        return temp;
    }
}