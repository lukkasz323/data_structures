# type: ignore

from node import Node
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __str__(self):
        result = ''
        for x in self:
            result += f' {str(x)},'
        return f'LinkedList[{result[:-1]} ]'
        
    def __len__(self):
        return self.get_last_index() + 1
        
    def __getitem__(self, index: int):
        try:
            return self.head[index]
        except TypeError:
            raise IndexError('Index out of range')
        
    def get_last_index(self):
        return self.head.get_last_index()
        
    def add(self, data):
        if self.head is None:
            self.head = Node(0, data)
        else:
            self.head.push(data)