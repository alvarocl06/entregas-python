'''
Created on 9 nov 2024

@author: alvar
'''

if __name__ == '__main__':
    pass

class ColaDePrioridad[str, int]():
    def __init__(self):
     
        self._elements = []
        self._priorities = []

    def size(self):
        
        return len(self._elements)

    def is_empty(self):
        
        return len(self._elements) == 0

    def elements(self):
        
        return self._elements

    def add(self, e, priority):      
        index = self.index_order(priority)
        
        
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def add_all(self, ls):
        for e, priority in ls:
            self.add(e, priority)

    def remove(self):
        assert len(self._elements) > 0, 'El agregado está vacío'
    
        return self._elements.pop(0)

    def remove_all(self):
        assert not self.is_empty(), 'El agregado está vacío'
        removed_elements = self._elements[:]
        self._elements.clear()
        self._priorities.clear()
        return removed_elements

    def index_order(self, priority):
        for i, p in enumerate(self._priorities):
            if priority < p:
                return i
        return len(self._elements)  

    def decrease_priority(self, e, new_priority):
        if e in self._elements:
            index = self._elements.index(e)
            old_priority = self._priorities[index]
            if new_priority < old_priority:
                
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)


