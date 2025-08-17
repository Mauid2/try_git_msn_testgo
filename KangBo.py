import time
def maopao(arry):
    start = time.time()
    for i in range(n):
        i=0
        flag=False
        for j in range(i+1,n-i):
            if arry[i]>arry[j]:
                flag=True
                tmp=arry[i]
                arry[i]=arry[j]
                arry[j]=tmp
            i+=1
        if flag is False:
            break
    end = time.time()
    return arry,start-end


arry=[20,2,7,12,15,1,6,8]
#maopao

n=high=len(arry)
low=0


def swap(a,b):
    tmp=b
    b=a
    a=tmp

def divideArea(arry,low,high):
    i=low-1
    brench_num=arry[high-1]
    for j in range(low,high):
        if arry[j]<brench_num:
            i+=1
            arry[i],arry[j]=arry[j],arry[i]
    arry[i+1],arry[high-1]=arry[high-1],arry[i+1]
    return i+1


def QuickQueue(arry,low,high):
    if low < high:
        p=divideArea(arry,low,high)
        QuickQueue(arry,low,p-1)
        QuickQueue(arry,p+1,high)
    # return arry

QuickQueue(arry,low,high)
print(arry)
# print(new)

