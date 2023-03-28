# type: ignore

class Node:
    def __init__(self, index, data) -> None:
        self.index = index
        self.data = data
        self.next = None
        
    def __getitem__(self, index):
        if index == self.index:
            return self.data
        else:
            try:
                return self.next[index]
            except TypeError:
                raise IndexError('Index out of range')
            
    def get_last_index(self):
        if self.next is None:
            return self.index
        else:
            return self.next.get_last_index()
        
    def push(self, data):
        if self.next is None:
            self.next = Node(self.index + 1, data)
        else:
            self.next.push(data)