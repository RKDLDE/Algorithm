import java.util.Arrays;
class Solution {
    public int[] solution(int[] num_list) {
        int numLength = num_list.length;
        int[] reverseList = new int[numLength];
        
        for(int i = 0; i < numLength; i++) {
            reverseList[i] = num_list[numLength-(i+1)];
        }
        
        return reverseList;
    }
}