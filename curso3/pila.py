class EmptyStack(Exception):
   pass

class Stack(object):
   def __init__(self):
      self.head = StackBase()

   def top(self):
      return self.head

   def push(self, value):
      self.head = self.head.push(value)

   def pop(self):
      oldHead = self.head
      self.head = self.head.pop()
      return oldHead

   def len(self):
      return self.head.len()

   def isEmpty(self):
      return self.head.isEmpty()


class StackBase(object):
   def push(self, value):
      return StackItem(parent= self, value= value)

   def pop(self):
      return EmptyStack("Pila Vacia")

   def len(self):
      return 0

   def isEmpty(self):
      return True

class StackItem(object):
   def __init__(self, parent, value):
      self.parent = parent
      self.value = value

   def push(self, value):
      return StackItem(parent= self, value= value)

   def pop(self):
      return self.parent

   def len(self):
      return self.parent.len() + 1

   def isEmpty(self):
      return False