def func():
    N,X=map(int,input().split())
    j=0
    count=0
    list2=list(map(int,input().split()))
    for i in range(N):
        R=list2[i]
        if(R<=X):
            j+=1
        else:
            if(count==1):
                break
            else:
                count+=1
    print(j)
func()

# Wrong Understanding of the Question
# def func():
#     N,X=map(int,input().split())
#     list1=[0]
#     j=0
#     count=0
#     list2=list(map(int,input().split()))
#     for i in range(N):
#         R=list2[i]
#         if(R<=X):
#             list1[j]+=1
#         else:
#             if(count==1):
#                 list1.append(0)
#                 j+=1
#                 count=0
#             else:
#                 count+=1
#     print(max(list1))
# func()