class MinHeap:
	
	def __init__(self,items):
		self.heap=[0]
		
		for ele in items:
			self.heap.append(ele)
			self.floatup(len(self.heap)-1)															
	
	def push_heap(self,ele):
		self.heap.append(ele)
		self.floatup(len(self.heap)-1)
		
	def peak_heap(self):
		if self.heap[1]:
			return self,heap[1]
		else:
			return False

	def pop_heap(self):
		if len(self.heap)==2:
			return self.heap.pop()
		elif len(self.heap)>2:
			self.swap(1,len(self.heap)-1)
			value=self.heap.pop()
			self.bubbledown(1)
			return value
		else:
			return False
	
	def swap(self,i,j):
		self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
		
	def floatup(self,index):
		parent=index//2
		
		if index==1:
			return None
		else:
			if self.heap[parent]>self.heap[index]:
				self.swap(index,parent)
				self.floatup(parent)
				
	def bubbledown(self,index):
		left=index*2
		right=index*2+1
		smallest=index
		
		if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
			smallest=left
		if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
			smallest=right
		if smallest!=index:
			self.swap(index,smallest)
			self.bubbledown(smallest)
			

if __name__=="__main__":
