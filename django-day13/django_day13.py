# #시간/공간 복잡도
# #n을 입력받아 1~n까지 연속된 숫자에 대한 제곱의 합을 출력하는 프로그램을 작성
#
#
# n=int(input())
# cnt=0
# for i in range(1,n+1):
#
#     cnt+=i*i
# print(cnt)
# #시간복잡도? O() 위 for 문은 시간복잡도가 O(n)
#
# #n=5 #밑에 코드는 시간복잡도 1
# print(int((n*(n+1)*(2*n+1))/6))
#
# n=[24,25,13,55,9,61]
# res=n[0]
# for i in n:
#     if i<res:
#         res=i
# print(res)
import re

# def hi():
#     print("hi")
#     hi()
# hi()

# def fact(n):
#     if n<=1:
#         return 1
#     return n*fact(n-1) #여기서 함수가 먼저 실행되므로 5*fact(4) 4*fact(3) ...fact(1) 1
# print(fact(5))
#
# a=10
# def hap(n):
#     if n<=1:
#         return 1
#     return n+hap(n-1)
# print(hap(a))

# def recursion_max(myList):
#     if len(myList) == 1:
#         return myList[0]
#     return max(myList[0], recursion_max(myList[1:]))
#
# print(recursion_max([37,24,56,15,16,23,100,12,13]))
# def recursion_max(myList):
#     if len(myList)==1:
#         return myList[0]
#     myList.remove(min(myList[0],myList[1]))
#     return recursion_max(myList)
# print(recursion_max([37,24,56,15,16,23,100,12,13]))



# 3. 재귀호출을 이용하여 풀어보세요.
# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
#
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
#
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
#
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.
#
# 예제 입력 1
# 10
# 예제 출력 1
# 55


def fibo(x):
    if x<=2:
        if x==0:
            return 0
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(17))