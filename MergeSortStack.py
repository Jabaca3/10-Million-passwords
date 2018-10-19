'''
Created on Oct 13, 2018
 
@author: Joseph Baca
'''
        
class dictNode:
    def __init__ (self, password):
        self.password = password
        self.appear = 1
        self.next = None
        
class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None       
    def appendtoList(self, Node):
        
        new_node = Node
        
        if self.head == None:    # If the heads empty, just make head this password.
            self.head = new_node
            self.tail = new_node
            
        else:
            current = self.head
            
            while current != None:
                
                if current.password == new_node.password:  # If it finds an identical password it adds 1 to appearance and breaks.
                    current.appear+=1
                    break
                
                elif current.next == None:      # If it hits end of the list append the node to the next spot
                    current.next = new_node
                    self.tail = new_node
                    break
                
                current = current.next
                
                
    def printList(self):    #print the entire list
        current = self.head
        
        while(current!= None):
            print(current.password ,"       Appears:", current.appear)
            print("-----------------------")
            current = current.next
 
    def fileInsert(self, file):
        
        for line in file:
        
            word=""
            characters =""
            i=0
            tabBool = False     #Checks if it has hit a tab
         
            while i < len(line) and len(line.strip()) != 0:   #Creates the first word once it hits a spce
                characters = line[i]
                
                if i == len(line)-1 and tabBool == True:
                    self.appendtoList(dictNode(word))
                    break

                if tabBool == True: #Starts putting the password together
                    word+=characters
                
                elif characters =="\t": # Each line is seperated by a username (a tab) then a password, this code ignores usernames.
                    tabBool = True
                    
                i+=1
    
        file.close()
             
#------------------------------------------------------------------------------------------------------------------------------------------

def getSizeList(linkedList):
        
        size=0
        current = linkedList.head
        
        while current!= None:
            size +=1
            current = current.next
        return size


def printTop20(self):
    i=0
    current = self.head   #print the top 20 appearances
    while current!=None and i<20:
        print(current.password, "      Appears: ", current.appear)
        print("-----------------------")
        current = current.next 
        i+=1
   
#-------------------------------------------------------------------------------------------------------------------------------------------

def lengthList(self):
    
    current = self.head
    size=0
    while current!=None:
        size+=1
        current = current.next
    return size  

def appendto(self, Node):
        
        new_node = Node
        
        if self.head == None:    # If the heads empty, just make head this password.
            self.head = new_node
            self.tail = new_node
            
        elif self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            
def isEmpty(self):
    return self == []

def isSorted(self):
    current = self.head
    
    while current.next != None:
        if current.appear < current.next.appear:
            return False
        current = current.next
    return True

def splitList(linkedList):
    
    
    linkedList2 = LinkedList()
    middle = lengthList(linkedList)/2
    current = linkedList.head
    
    
    while(middle-1 > 0):        #finds the middle of the linked list
            current = current.next;
            middle = middle-1
            
    head2 = current.next
    current.next = None
    
    head1 = linkedList.head
    linkedList.head = head1
    linkedList2.head = head2
    '''
    print("Half 1: ")
    linkedList.printList()
    print("Half 2: ")
    linkedList2.printList()
    print("----------------------------------------")
    '''
    return linkedList, linkedList2
            

def merge(half1 , half2):
    
    current1 = half1.head
    current2 = half2.head
    
    if current1 == None:
        return half2
    if current2 == None:
        return half1
    
    if lengthList(half1) == 2 and current1.appear < current1.next.appear:   #If the size of the list differ 1-2 or  2-1 sort the side with 2 
        temp = current1
        half1.head = current1.next
        current1.next = temp
        
    if lengthList(half2) == 2 and current2.appear < current2.next.appear:
        temp = current2
        half2.head = current2.next
        current1.next = temp
    
    else:
        mergedList = LinkedList()
        current1= half1.head
        current2= half2.head
        
        while current1 != None and current2 != None:
            
                if current1.appear >= current2.appear:
                    appendto(mergedList,current1)
                    current1 = current1.next
                    
                elif current1.appear < current2.appear:
                    appendto(mergedList,current2)
                    current2 = current2.next
                    
        while current1 != None and current2 == None:  #Both whiles dump the rest of the Nodes into the list when the opposite is full
            appendto(mergedList,current1)
            current1 = current1.next
            
        while current1 == None and current2 != None:
            appendto(mergedList,current2)
            current2 = current2.next
            
    return mergedList
                    
def mergeSortStack(linkedList):
    
    finalList = LinkedList()
    stack = []
    stack.append(linkedList)
    
    while (isEmpty(stack) == False): #chekcing if the stack is empty
        
        linkedList = stack.pop()
        half1, half2 = splitList(linkedList)
            
        if (isSorted(half1) and isSorted(half2)) or ((lengthList(half1) == 1) or (lengthList(half2) == 1)):
            finalList = merge(finalList, merge(half1, half2))
                
        else:
            stack.append(half1)
            stack.append(half2)
            
    return finalList

def main():
    
    linkedList = LinkedList()
    file = open("somepasswords.txt","r")
    linkedList.fileInsert(file)
    print("Regular List: ")
    linkedList.printList()
    
    '''
    #******************Debugging Purposes:**********************
    
    half1, half2 = splitList(linkedList)
    print("----------------------------------------")
    print("half 1 : ")
    half1.printList()
    print("-----------------------------------------")
    print("half 2: ")
    half2.printList()
    print("-----------------------------------------")
    
    
    mergedList = merge(half1, half2)
    print()
    print("Merged List: ")
    
    mergedList.printList()
    
    #**********************************************************
    '''
    
    print()
    print("-----------------------------------------")
    print("Stacked Sorted: ")
    stacksort = mergeSortStack(linkedList)
    stacksort.printList()
    print("-----------------------------------------")
    print("TOP 20")
    printTop20(stacksort)
    
    
main()