"""
큐 자료구조
 - 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조
 - 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.
 - 큐룰 파이썬에서 활용하고자 할 때, 'deque'라이브러리를 황용
 - from collections import deque
"""

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 변환
print(queue) # 나중에 들어온 순서대로 출력

