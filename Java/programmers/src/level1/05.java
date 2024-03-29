import java.util.Arrays;
import java.util.stream.Stream;

class Solution {
    public int[] solution(long n) {
        int[] arr = Stream.of(String.valueOf(n).split("")).mapToInt(Integer::parseInt).toArray();
        int[] answer = new int[arr.length];
        for(int i=0; i<arr.length; i++){
            answer[arr.length-i-1] = arr[i];
        }
        return answer;
    }
}