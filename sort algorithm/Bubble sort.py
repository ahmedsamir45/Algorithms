def swap(A,x,y):
    A[x], A[y]=A[y], A[x]
def bubbleSortR(A):
    for i in range(len(A)):
        print("===============\ni=",i,A)
        for k in range(len(A)-1,i,-1):
            print("K=",k,A)
            if (A[k]< A[k-1]):
                swap(A,k,k-1)
                #print("K=",k,A)

def bubbleSortL(A):
    for i in range(len(A)):
        print("i=",i,A)
        for k in range(0,len(A)-i-1):
            print("K=",k,A)
            if (A[k]> A[k+1]):
                swap(A,k,k+1)
                #print("K=",k,A)
list1=[12,31,2,12,2,31,31,23,1,3,0]
bubbleSortL(list1)
print(list1)