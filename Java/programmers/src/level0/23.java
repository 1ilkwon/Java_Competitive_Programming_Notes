class Solution {
    public int solution(int price) {
        int answer = 0;
        if(500000 <= price){
            answer = (int)(price * 0.8);
        }else if (price >= 300000){
            answer = (int)(price * 0.9);
        }else if (100000 <= price){
            answer = (int)(price * 0.95);
        }else{
            answer = price;
        }
        return answer;
    }
}