class Solution {
    public int solution(int n) {
        String m = n+"";
        int sum = 0;
        
        for(int i = 0; i < m.length(); i++) {
            sum += Character.getNumericValue(m.charAt(i));
        }
        
        return sum;
    }
}