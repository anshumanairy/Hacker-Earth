# Timeout on Half Cases
# def func():
#     N=int(input())
#     list1=list(map(int,input().split()))
#     list2=list(map(int,input().split()))
#     count=0
#     list3=[]
#     for i in range(len(list1)-1):
#         for j in range(i+1,len(list1)):
#             if(list1[j]>list1[i]):
#                 list3.append(list1[i])
#                 list3.append(list1[j])
#     for j in range(len(list2)):
#         for k in range(0,len(list3),2):
#             if(list2[j]>list3[k] and list2[j]>list3[k+1]):
#                 count+=1
#     print(count)
# func()

def func():
    N=int(input())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    count=0
    list3=[]
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if(list1[j]>list1[i]):
                list3.append(list1[j])
    list3.sort()
    list2.sort(reverse=True)
    list4=list(set(list3))
    list5=[]
    for i in range(len(list4)):
        list5.append(list3.count(list4[i]))
    for j in range(len(list2)):
        check=0
        for k in range(len(list4)):
            if(list2[j]>list4[k]):
                count+=list5[k]
                check+=1
        if(check==0):
            break
    print(count)
func()