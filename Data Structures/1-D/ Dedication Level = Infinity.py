def func():
    n=int(input())
    list1=[]
    list2=[]
    for i in range(n):
        a,b=map(str,input().split())
        list1.append(a)
        list2.append(int(b))
    # Max Time Name
    max1=max(list2)
    index1=list2.index(max1)
    name1=list1[index1]
    list2.pop(index1)
    list1.pop(index1)
    # 2nd Max Time Name
    max2=max(list2)
    index2=list2.index(max2)
    name2=list1[index2]
    list2.pop(index2)
    list1.pop(index2)
    # 3rd Max Time Name
    max3=max(list2)
    index3=list2.index(max3)
    name3=list1[index3]
    list2.pop(index3)
    list1.pop(index3)
    print(name1)
    print(name2)
    print(name3)
func()