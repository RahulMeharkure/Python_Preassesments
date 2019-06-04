def binarySearch(arr,low,high,key):
    # low should always be less than high for search to occur
    if(low<high):
        #mid is used to get the middle element inorder to divide the arr in two parts
        mid=low+int((high-low)/2)
        #If middle element is the key then return mid
        if arr[mid]==key:
            return mid
        #check if key lies in which part of arr on the right side of middle or left
        if (arr[mid]<key):
            return binarySearch(arr,mid+1,high,key)
        else:
            return binarySearch(arr,0,mid-1,key)
    return -9999


if __name__=='__main__':
    #input list considered to be sorted in ascending order if not sorted then sorting algorithm has to be applied
    arr=[10,20,30,40,50]
    key=30
    pos=binarySearch(arr,0,len(arr)-1,key)
    try:
        print('Position of key %d is %d' % (arr[pos],pos))
    except IndexError:
        print('Element not Found!')
