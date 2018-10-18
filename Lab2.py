'''
Created on Oct 11, 2018

@author: Joseph Baca
'''


class Node:
    def __init__ (self, password):
        self.password = password
        self.appear = 1
        self.next = None
        
class LinkedList:
    def __init__ (self):
        self.head = None
        self.size =0
        
    def size(self):       #gets the length of the list.
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def append(self, password):
        
        new_node = Node(password)
        
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
            
            
    def bubbleSort(self,length):    #Improved bubble sort algorithm helped by recursion
        
        index =0
        current = self.head
        
        if self.size <= 1:
            return self
        
        if self.size == 2 and current.appear < current.next.appear:
            return self.swap(None, current, current.next, None)
        
        while  current.next.next!= None and index < length:
            
            if current == self.head and current.appear < current.next.appear:  #Properly Swaps the Head
                self.swap(None, current, current.next, current.next.next)
                current = self.head
                index+=1
            
            if current.next.next.next != None and current.next.appear < current.next.next.appear:  #Properly Swaps everything in the middle
                self.swap(current, current.next, current.next.next, current.next.next.next)
                index+=1
        
            if current.next.next.next == None and current.next.appear < current.next.next.appear: #Properly Swaps the last Nodes
                self.swap(current, current.next, current.next.next, None)
                return self.bubbleSort(length-1)
            
            elif current.next.next.next == None:
                return self.bubbleSort(length-1)  #recursivly shortens the length of the List to improve bubble sort
            
            current = current.next #iterator
            
    def fileInsert(self, file):
        
        for line in file:
        
            word=""
            characters =""
            i=0
            tabBool = False     #Checks if it has hit a tab
         
            while i < len(line) and len(line.strip()) != 0:   #Creates the first word once it hits a spce
                characters = line[i]
                
                if i == len(line)-1 and tabBool == True:
                    self.append(word)
                    break

                if tabBool == True: #Starts putting the password together
                    word+=characters
                
                elif characters =="\t": # Each line is seperated by a username (a tab) then a password, this code ignores usernames.
                    tabBool = True
                    
                i+=1
    
        file.close()
        
    def printTop20(self):
        i=0
        current = self.head   #print the top 20 appearances
        while self.isEmpty() == False and i < 20 and current.next!= None:
            print(current.password, "      Appears: ", current.appear)
            print("-----------------------")
            current = current.next 
            i+=1
                    
    def fileInsertLine(self, file):
        
        for line in file:
            self.append(line)
        file.close()
        
        
#-----------------------------------------------------------------------------------------------


def main():
            
    myList = LinkedList()   #Initiallizing the LinkedList

    
    #file = open("10-million-combos.txt","r")
    file = open("somepasswords.txt","r")

    
    myList.fileInsert(file)
    myList.printList()
    
    print("------------------------------------------------------------------------------")
    print()
    print()
    print()
    print("                               Top 20 ")
    print("---------------------------- Bubble Sort ------------------------------------------------")
    
    myList.bubbleSort(myList.size)
    myList.printTop20()
    
   
main()