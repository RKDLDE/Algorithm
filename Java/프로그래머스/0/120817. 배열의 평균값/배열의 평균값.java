class Solution {
    public double solution(int[] numbers) {
        double answer = 0.0;
        int length = numbers.length;
        for(int i = 0; i<length; i++){
            answer += numbers[i];
        }
        return answer/length;
    }
}