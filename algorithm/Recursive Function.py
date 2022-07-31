"""
재귀함수
 - 자기 자신을 다시 호출하는 함수
 - 단순한 재귀 함수 예제
  ->
  def recursive_function():
    print('재귀를 호출')
    recursive_function()

  recursive_function()

 - 재귀 함수를 문제 풀이에서 사용할 때에는 재귀 함수의 종료 조건을 반드시 명시
 - 종료 조건을 제대로 명시하지 않으면 무한 루프
  ->
    def recursive_function(i):
    if i == 100:
        :return
    print(i, '번째 재귀에서', i + 1, '번째 재귀함수를 호출한다')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다')

  recursive_function(1)
"""

"""
팩토리얼 구현 예제
 -> 수학적으로 0!과 1!의 값은 1이다.
 -> n! = 1 x 2 x 3 x (n-1) x n
"""