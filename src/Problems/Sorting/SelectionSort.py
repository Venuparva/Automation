'''

In order to sort given elements of array using selection sort
----
Algm:
-----
1.Find Min Element of given array of elements
2.Swap it with current element
3.Repeat the steps until all elements are sorted
'''
def SelectionSort(A):
    for i in range(len(A)):
        # set first element as Min
        least = i
        # compare first element with remaining elements in list and find MIN from that remaining elements list
        for k in range(i + 1,len(A)):
            if A[k] < A[least]:
                least = k
        swap(A,least,i)
        print("after sort",A)

def swap( A, x, y ):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

A = [54,26,93,17,77,31,44,55,20]
SelectionSort(A)
print(A)
