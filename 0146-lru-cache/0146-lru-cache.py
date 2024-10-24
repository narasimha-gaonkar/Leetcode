class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = ListNode('head', 0)
        self.tail = ListNode('tail', 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        
        if key in self.mapping:
            value = self.mapping[key].value
            self.update_dll(key)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.update_dll(key)
            self.mapping[key].value = value
        else:
            if len(self.mapping) == self.capacity:
                self.remove_node(self.tail.prev.key)
            self.insert_node_start(key, value)
    
    def remove_node(self, key):
        node = self.mapping[key]
        del self.mapping[key]
        
        prev = node.prev
        nextt = node.next
        
        prev.next = nextt
        nextt.prev = prev
        
    def insert_node_start(self, key, value):
        new_node = ListNode(key, value)
        
        first = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first
        first.prev = new_node
        self.mapping[key] = new_node
    
    def update_dll(self, key) -> None:
        node = self.mapping[key]
        self.remove_node(key)
        self.insert_node_start(node.key, node.value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)