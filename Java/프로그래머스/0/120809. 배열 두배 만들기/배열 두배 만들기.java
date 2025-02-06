class Solution {
    public int[] solution(int[] numbers) {
        int i;
        for(i = 0; i < numbers.length; i++){
            numbers[i] = numbers[i] * 2;
        }
      
        return numbers;
    }
}