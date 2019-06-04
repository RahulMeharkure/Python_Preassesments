#NOTE: SORTING IS PERFORMED AS PER THE ASCII VALUES BECAUSE INPUT IS IN STRING FORMAT
#SORTING IS PERFORMED FOR ALL VALUES PRESENT IN ASCII TABLE

def sort_listtuple(lis):
    # merge sort works on divide and conquer technique hence list size should be greater than 1
    if len(lis)>1:
        # middle tuple of the list is find and that used to divide in two sub parts left and right
        mid=len(lis)//2
        # two sub parts left and right
        left=lis[:mid]
        right=lis[mid:]
        # recursive calls are made to sort first the left sub part and then right as known in merge sort
        sort_listtuple(left)
        sort_listtuple(right)

        i=j=k=0
        # Comparsion of left and right part for sorting in ascending order
        while i<len(left) and j<len(right):
            # here sorting is performed on the bases of ASCII value of last element of tuple as tuple input is in string format
            if ord(left[i][-1])<ord(right[j][-1]):
                lis[k]=left[i]
                i+=1
            else:
                lis[k]=right[j]
                j+=1
            k+=1
        # checnking if any element was left out
        while i<len(left):
            lis[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            lis[k]=right[j]
            j+=1
            k+=1

def printlist(lis):
    print(lis)


if __name__=='__main__':
    lis=[]
    #tuples size may vary user to user hence first is take no. of tuples as input
    l=int(input('No. of tuples you want to enter: '))
    # in loop string input is taken and typecasted in tuples which is then appended to list e.g : 1st tuple 123, 2nd tuple 4352
    for i in range(l):
        tup=tuple(input())
        lis.append(tup)
    #sortlisttuple is sorting algorithm here merge sort is used because its complexity is O(nlogn)
    sort_listtuple(lis)
    # printlist function is used to print the list
    printlist(lis)

