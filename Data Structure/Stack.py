"""
스택
 - 먼저 들어 온 데이터가 나중에 나가는 형식의 자료구조
 - 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.
 - 리스트를 활용
"""

stack = []

# 삽입 : append , 삭제 : pop
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 역으로 출력(상단부터)
print(stack) # 최하단 원소부터 출력


