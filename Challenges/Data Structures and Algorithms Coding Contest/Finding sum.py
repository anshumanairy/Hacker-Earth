# numpy.prod not good for big integer results as it gives output in float
# import numpy
# def func():
#     N=int(input())
#     list1=list(map(int,input().split()))
#     answer=0
#     j=0
#     while(j!=(len(list1)-(N//2)+1)):
#         k=j+(N//2)
#         list2=list1[j:k]
#         j+=1
#         # print(list2)
#         answer+=numpy.prod(list2)
#     print(answer%1000000007)
# func()

# This will give time limit error for half cases because of high complexity
# from operator import mul
# from functools import reduce
# def func():
#     N=int(input())
#     list1=list(map(int,input().split()))
#     answer=0
#     j=0
#     if(N%2==0):
#         while(j!=((N//2)+1)):
#             k=j+(N//2)
#             answer+=reduce(mul, list1[j:k], 1)
#             j+=1
#     else:
#         while(j!=((N//2)+2)):
#             k=j+(N//2)
#             answer+=reduce(mul, list1[j:k], 1)
#             j+=1
#     print(answer%1000000007)
# func()

# Less Time consuming approach but still TLE
# from operator import mul
# from functools import reduce
# def func():
#     N=int(input())
#     list1=list(map(int,input().split()))
#     answer=0
#     j=1
#     p=reduce(mul, list1[0:(N//2)], 1)
#     q=list1[0]
#     answer+=p
#     if(N%2==0):
#         while(j!=((N//2)+1)):
#             k=j+(N//2)
#             p=p//q
#             p=p*list1[k-1]
#             q=list1[j]
#             answer+=p
#             j+=1
#     else:
#         while(j!=((N//2)+2)):
#             k=j+(N//2)
#             p=p//q
#             p=p*list1[k-1]
#             q=list1[j]
#             answer+=p
#             j+=1
#     print(answer%1000000007)
# func()

