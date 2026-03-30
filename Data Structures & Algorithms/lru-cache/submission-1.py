from collections import defaultdict
class Node:
    def __init__(self,val=None,key=None,value=None,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = defaultdict(lambda: Node())
        self.Start = Node()
        self.End = Node()
        self.Start.next = self.End
        self.End.prev = self.Start
        self.counter = 0 

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1 
        else:
            #delete from cur position
            node = self.hmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            #add to end
            temp = self.End.prev
            self.End.prev = node
            temp.next = node
            node.prev = temp
            node.next = self.End
            return node.val
        

    def put(self, key: int, value: int) -> None:
        #update current node
        if key in self.hmap:
            node = self.hmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            self.counter += 1 
        self.hmap[key].key, self.hmap[key].val = key,value
        node = self.hmap[key]
        #put new node
        temp = self.End.prev
        self.End.prev = node
        temp.next = node
        node.prev = temp
        node.next = self.End
        

        if self.counter > self.capacity:
            node = self.Start.next
            self.Start.next = node.next
            node.next.prev = self.Start
            del self.hmap[node.key]
            self.counter -= 1 
        #node is deleted
        
