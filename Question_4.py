def grouping(lis,dict):
    #below code is used to create a dictionary that would store keys as tuples and values of keys as to whom it has found common element
    for i in range(len(lis)):
        for k in range(len(lis[i])):
            for j in range(i+1,len(lis)):
                if (lis[i][k] in lis[j]):
                    dict[lis[i]].append(lis[j])
    print(dict)
    #code to use the dictionary to create the desired output
    for i,j in dict.items():
        if not j:
            continue


if __name__=='__main__':
    lis=[('Pradnya','Anisha'),('Austin','Pradnya'),('Austin','Melburne'),('Vishal','Akash'),('Rahul','Pavan')]
    dict={keys:[] for keys in lis}
    grouping(lis,dict)

'''
# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None
# This function is in LinkedList class
# Function to insert a new node at the beginning
    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next =  new_node


    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data,)
            temp = temp.next


def groups(head1,head2):
    temp = head1
    while(temp):
        next_node = temp.next
        for i in len(temp.data):
            if temp.data[i] in next_node.data:
                head2=temp




# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    llist = LinkedList()

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.append(('Pradnya','Anisha'))
    llist.append(('Austin','Pradnya'))
    llist.append(('Austin','Melburne'))
    llist.append(('Vishal','Akash'))
    llist.append(('Rahul','Pavan'))

    sec_llist=LinkedList()
    groups(llist.head,sec_llist.head)
    print ('Created linked list is:',)
    llist.printList()
    '''
