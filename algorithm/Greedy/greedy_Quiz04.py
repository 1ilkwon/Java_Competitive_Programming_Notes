n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for x in data :
    if target < x:
        break
    target += x

print(target)

'''
너무 어려웠다. 아직 익숙하지 않아서 그런 것 같다. 
일단 이번 문제는 생각한 것보다 원리가 간단하지만 떠올리기 쉽지 않았다.

해당 문제가 그리디 챕터에서 출제가 되었기에 그리디라고 가정을 하고 풀어보자 일단은
그리디 알고리즘은 현재 상태에서 매번 가장 좋아 보이는 것만을 선택하는 알고리즘이다.

target을 1로 지정해두고 우리는 1부터 target-1까지 모두 만들수 있는 상태를 현재상태라고 해보자
그렇다면 1부터 list에 있는 인덱스를 하나씩 비교해보자
만약에 인데스에 값이 target보다 크다고 생각해보자 
그렇다면 당연히 최소값은 target이 될 것이다.
(리스트를 오름차순 정렬했기 때문에)

하지만 이와 반대로 target에 값이 더 크다고 생각해보자.
그렇다면 target에 인덱스 값을 더해준다.
더해준 값은 현재상태가 된다. 만약에 더해준 값 이전에 최솟값이 있다면? 이라는 생각을 했을 것이다.
그렇다면 이미 인덱스 값이 target보다 큰 값일 것이기에 해당 target이 최솟값이 된다. 
'''