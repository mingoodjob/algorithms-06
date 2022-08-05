"""
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""

n=1000
a = [True] * (n + 1)
a[0] = a[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        for j in range(i * 2, n + 1, i):
            a[j] = False
    
print([i for i in range(n + 1) if a[i]])
