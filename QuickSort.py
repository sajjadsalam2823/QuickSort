"""
implementing QuickSort in three different approaches
"""
import csv


# first read a txt file containg the numbers
def read_txt_return_list(filename):
    """
        input: the name of the txt file
        output: a list containing the element of the array 
        in the txt file
    """
    array_lst = []
    with open(filename, "rt", newline = '') as csv_file:
        csv_read = csv.reader(csv_file)
        for row in csv_read:
            array_lst.append(int(row[0]))
        
    return array_lst

def pickmed(A):
    """
    this function determines the median in a list
    input a list
    output returns the list while the med has been moven to the first elemnt
    """
    if len(A)%2==0:
        lst = [A[0], A[len(A)//2-1], A[len(A)-1]]
        for item in range(3):
            if lst[item]!= min(lst) and lst[item]!= max(lst):
                lst[0], lst[item] = lst[item], lst[0]
                A[0], A[len(A)//2-1], A[len(A)-1] = lst[0], lst[1], lst[2]
    else:
        lst = [A[0], A[len(A)//2], A[len(A)-1]]
        for item in range(3):
            if lst[item]!= min(lst) and lst[item]!= max(lst):
                lst[0], lst[item] = lst[item], lst[0]
                A[0], A[len(A)//2], A[len(A)-1] = lst[0], lst[1], lst[2]

def quick_sort(A):
    """
    receives a list and spits out number of comparisons
    """
    if len(A) <= 1:
       return 0
    else:
#        pickmed(A)                             #comment out for the median element case
#        A[0], A[len(A)-1] = A[len(A)-1], A[0]  # comment out for the last elemnt case
        i = 1
        j = 0
        for idx in range(1, len(A)):
            j += 1
            if A[idx] < A[0]:
                A[idx], A[i] = A[i], A[idx]
                i += 1
        A[0], A[i-1] = A[i-1], A[0]
        j += quick_sort(A[:i-1]) + quick_sort(A[i:]) 

        return j
    



            
            

print(quick_sort(read_txt_return_list("data.txt")))
