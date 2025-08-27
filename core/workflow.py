class Node():
    def __init__(self, data: dict={}, next: any=None): 
        self.data = data 
        self.next = next 
    

class Workflow(): 
    def __init__(self, head: Node): 
        self.head = head
    
    def add_task(self, data: dict) -> None: 
        if self.head is None: 
            self.head = Node(data=data)
            return 
        
        current = self.head 

        while current.next: 
            current = current.next 
        
        current.next = Node(data=data)
    
    def detect_circular_dependencies(self) -> bool: 
        slow = self.head 
        fast = self.head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                return True 
        
        return False 