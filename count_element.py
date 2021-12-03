# Write a function that counts the number of times a given int occurs in a Linked List

# Given a singly linked list and a key, count the number of occurrences of the given key in the linked list. For example, if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4.

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )
    
    def countElement ( self , data ) :
        temp = self.head
        counter = 0
        while ( temp ) :
            if temp.data == data : counter += 1
            temp = temp.next
        print ( counter )

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 1 )
llist.add ( 1 )
llist.add ( 5 )
llist.add ( 1 )
llist.countElement( 1 )