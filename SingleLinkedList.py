class Node:
    #Creating Node
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Insert as head (beginning)
    def insertAtBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #insert after a node
    def insertAfterNode(self,prev_node,new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #Inserting node at end
    def insertAtEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    #Deleting a node by index/position
    def deleteNodeByPos(self,position):
        if self.head is None:
            return
        temp = self.head
        if position==0:
            self.head = temp.next
            temp = None
            return
        for i in range(position-1): #Finding the position
            temp = temp.next
            if temp is None:
                return
        if temp is None or temp.next is None:
            return
        next = temp.next.next
        temp.next=None
        temp.next = next

    def deleteNodebyVal(self,head,val):
        dummyHead = Node(None)
        head = Node(head)
        dummyHead.next = head
        node = dummyHead
        while node.next:
            if node.next.data == val:
                node.next = node.next.next
            else:
                node = node.next

        return dummyHead

    #Search an element by value
    def searchElement(self,key):
        if self.head is None:return
        current = self.head
        while current is not None:
            if current.data == key:return True
            current = current.next
        return False

    #Sorting the linked list
    def sortList(self,head):
        current = head
        index = Node(None)
        if head is None:return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data,index.data = index.data,current.data
                    index = index.next
                current = current.next

    #Printing the list
    def printList(self):
        temp = self.head
        while temp:
            print(f"{str(temp.data)}-->",end="")
            temp = temp.next
    
if __name__=='__main__':
    llist = LinkedList()
    llist.insertAtEnd(1) #Not there in list,as the list was empty.
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfterNode(llist.head.next,5)

    print("After inserting Elements:")
    llist.printList()

    llist.deleteNodebyVal(1,3)

    print("\nAfter deleting elements: ")
    llist.deleteNodeByPos(3)
    llist.printList()

    item_to_find = 3
    if llist.searchElement(item_to_find):
        print(f"\n{str(item_to_find)} is found")
    else:
        print(f"\n{str(item_to_find)} is not found")

    llist.sortList(llist.head)
    print("After sorting list:")
    llist.printList()