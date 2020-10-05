class MaxHeap:

	def __init__(self,items):
		self.heap=[0]
	
		for ele in items:
			self.heap.append(ele)
			self.floatup(len(self.heap)-1)
		
	def push_heap(self,ele):
		self.heap.append(ele)
		self.floatup(len(self.heap)-1)
	
	def peak(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
				
	def pop_heap(self):
		if len(self.heap)==1:
			return None
		elif len(self.heap)==2:
			return self.heap.pop()
		else:
			self.swap(1,len(self.heap)-1)
			value=self.heap.pop()
			self.bubbledown(1,len(self.heap))
			return value
		
	def swap(self,i,j):
		self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
	
	def floatup(self,index):
		parent=index//2
		
		if index==1:
			return None
		else:
			if self.heap[index]>self.heap[parent]:
				self.swap(index,parent)
				self.floatup(parent)
				
	def bubbledown(self,index,end):
		left=index*2
		right=index*2+1
		largest=index
		if left<end and self.heap[left]>self.heap[largest]:
			largest=left
		if right<end and self.heap[right]>self.heap[largest]:
			largest=right
		if index!=largest:
			self.swap(index,largest)
			self.bubbledown(largest,end) 
			
