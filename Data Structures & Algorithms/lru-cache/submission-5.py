class Node:
    def __init__(self,key=None,value=None,prev=None,next=None):
        self.key=key
        self.value=value
        self.prev=prev
        self.next=next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.count = 0
        self.start=self.exit=Node()
        self.hmap = {}
    def get(self, key: int) -> int:
        if key in self.hmap:
            node=self.hmap[key]
            if node.prev:
                node.prev.next,node.next.prev = node.next,node.prev
                node.next,self.start.prev=self.start,node
                self.start=node
            return self.hmap[key].value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        #update(1/2)
        if key in self.hmap:
            node = self.hmap[key]
            if node!=self.start:
                node.prev.next,node.next.prev = node.next,node.prev
            else:
                self.start = node.next
                node.next.prev=None
            self.count-=1
      #add
        self.hmap[key] = Node(key,value,None,self.start)
        self.start.prev=self.hmap[key]
        self.start=self.hmap[key]
        self.count+=1
        #delete
        if self.count>self.capacity:
            del self.hmap[self.exit.prev.key]
            self.exit.prev.prev.next,self.exit.prev=self.exit,self.exit.prev.prev
            self.count-=1
            

        
