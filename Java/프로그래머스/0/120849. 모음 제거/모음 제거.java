class Solution {
    public String solution(String my_string) {
        String[] alArr = {"a", "e", "i", "o", "u"};
        
        for (int i = 0; i < alArr.length; i++){
            my_string = my_string.replace(alArr[i], "");
        }

        return my_string;
    }
}