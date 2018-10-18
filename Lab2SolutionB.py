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
        self.size =0
        
    def size(self):       #gets the length of the list. Does not update if items were removed from the list
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def append(self, Node):
        
        new_node = Node
        
        if self.head == None:    # If the heads empty, just make head this password.
            self.head = new_node
            self.size+=1
            
        else:
            current = self.head
            
            while current != None:
                
                if current.password == new_node.password:  # If it finds an identical password it adds 1 to appearance and breaks.
                    current.appear+=1
                    break
                
                elif current.next == None:      # If it hits end of the list append the node to the next spot
                    current.next = new_node
                    self.size+=1
                    break
                
                current = current.next
                
                
    def printList(self):    #print the entire list
        current = self.head
        
        while(current!= None):
            print(current.password ,"       Appears:", current.appear)
            print("-----------------------")
            current = current.next
            
    def swap(self, current, node1, node2, node3):   #Swaps Nodes for Improved Bubble Sort
        
        tmpNode = node1
        
        if node1 == self.head:      #This case is only for the head
            self.head = node2
            node2.next = tmpNode
            tmpNode.next = node3
        
        else:
            current.next = node2
            node2.next = tmpNode
            tmpNode.next = node3
            
          
            
    def fileInsert(self, file):
        
        for line in file:
        
            word=""
            characters =""
            i=0
            tabBool = False     #Checks if it has hit a tab
         
            while i < len(line) and len(line.strip()) != 0:   #Creates the first word once it hits a spce
                characters = line[i]
                
                if i == len(line)-1 and tabBool == True:
                    self.append(dictNode(word))
                    break

                if tabBool == True: #Starts putting the password together
                    word+=characters
                
                elif characters =="\t": # Each line is seperated by a username (a tab) then a password, this code ignores usernames.
                    tabBool = True
                    
                i+=1
    
        file.close()
        
             
def mergeSort(self):
    
        head1 = self
        middle = getSizeList(self)/2
        
        if(self == None or self.next == None):
            return self
        
        while(middle-1 > 0):        #finds the middle of the linked list
            head1 = head1.next;
            middle = middle-1
        
        head2 = head1.next
        head1.next = None
        head1 = self
        
        half1 = mergeSort(head1)
        half2 = mergeSort(head2)
        
        return mergeList(half1, half2)
    
def mergeList(half1, half2):    #compares both lists and merges them
    
    if half1 == None:
        return half2
    if half2 == None:
        return half1
    
    if half1.appear < half2.appear:
        sortedlist = half2
        sortedlist.next = mergeList(half1, half2.next)
        
    else:
        sortedlist = half1
        sortedlist.next = mergeList(half1.next, half2)

    return sortedlist
            
def getSizeList(dictList):
        
        size=0
        current = dictList
        while current!= None:
            size +=1
            current = current.next
        return size
    
            
def insertToDictionary(linkedList, dictionary):
    current = linkedList.head
        
    while current!= None:
        dictionary[current.password] = current
        current = current.next
    return dictionary

def printDictionary(dictionary):

    for item, value in dictionary.items():
        print(item,"   ", value.appear)
        
        
def fileInsert(nodeList, file):
        
        for line in file:
        
            word=""
            characters =""
            i=0
            tabBool = False     #Checks if it has hit a tab
         
            while i < len(line) and len(line.strip()) != 0:   #Creates the first word once it hits a space
                characters = line[i]
                
                if i == len(line)-1 and tabBool == True:
                    nodeList.append(word)
                    break

                if tabBool == True: #Starts putting the password together
                    word+=characters
                
                elif characters =="\t": # Each line is seperated by a username (a tab) then a password, this code ignores usernames.
                    tabBool = True
                    
                i+=1
    
        file.close()
def printTop20(self):
    i=0
    current = self   #print the top 20 appearances
    while current!=None and i<20:
        print(current.password, "      Appears: ", current.appear)
        print("-----------------------")
        current = current.next 
        i+=1


    
def main():
    
    myDictList = LinkedList()
    dictPasswords = {}
    
    #file = open("10-million-combos.txt","r")
    file = open("somepasswords.txt","r")
    
    myDictList.fileInsert(file)
    dictPasswords = insertToDictionary(myDictList, dictPasswords)
    
    print("----------------------------------------------------")
    print("-------------- Dictionary output -------------------")
    printDictionary(dictPasswords)
    
    
    print("------------------------------------------------------------------------------")
    print()
    print()
    print()
    print("                               Top 20 ")
    print("------------------------- Merge Sorted List ----------------------------------")
    print()
    
    sortedList = mergeSort(myDictList.head)
    printTop20(sortedList)
    
    
main()

        
