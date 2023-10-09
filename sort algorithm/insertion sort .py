def Insertionsort( A ): 
    for i in range( 1 , len( A ) ):
        print("=====\ni=",i," ",A)
        temp = A[i] 
        k= i
        while k > 0 and temp< A[k-1]:
            print("\nk=",k," ",A)
            A[k] = A[k-1] 
            k -= 1
            A[k] =temp


            
A= [54,26,93,17,77,3 ,44,55,20] 
Insertionsort(A) 
print(A)