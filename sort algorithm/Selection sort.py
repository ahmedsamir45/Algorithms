def swap(A,x,y):
    A[y], A[x]=A[x],A[y]
def SelectionSort( A ): 
    for i in range( len( A ) ):
        print("===============\ni=",i," ",A)
        least = i
        for k in range( i + 1 , len( A)):
            print("\n k=",k," ",A)
            if A[k] < A[least]:
                least = k
        swap( A, least, i )


A= [54,26,93,17,77,31,44,55,20]
print( SelectionSort (A) ) 
print(A)

