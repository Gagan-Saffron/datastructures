class Queue():
	def __init__(self):
		self.que=[]

	def isEmpty(self):
		return len(self.que)==0

	def enque(self,data):
		self.que.append(data)

	def deque(self):
		if not self.isEmpty():
			return self.que.pop(0)

	def peak(self):
		if not self.isEmpty():
			return self.que[0].root


#-----------------------------------------------------------------------------
class BinSearchTree():

	def __init__(self,root):
		self.root=root
		self.left=None
		self.right=None

	def add_node(self,node):
		if node==self.root:
			pass
		elif node<self.root:
			if self.left:
				self.left.add_node(node)
			else:
				self.left=BinSearchTree(node)
				print("Added to left tree of {}..".format(self.root))
		elif node>self.root:
			if self.right:
				self.right.add_node(node)
			else:
				self.right=BinSearchTree(node)
				print("Added to right tree of {}..".format(self.root))

	def pre_order_trav(self,ele_lst=[]):
		if self.root:
			ele_lst.append(self.root)
			if self.left:
				self.left.pre_order_trav(ele_lst)
			if self.right:
				self.right.pre_order_trav(ele_lst)
		return ele_lst

	def post_order_trav(self,ele_lst=[]):
		if self.root:
			if self.left:
				self.left.post_order_trav(ele_lst)
			if self.right:
				self.right.post_order_trav(ele_lst)
			ele_lst.append(self.root)
		return ele_lst


	def in_order_trav(self,ele_lst=[]):
		if self.root:
			if self.left:
				self.left.in_order_trav(ele_lst)
			
			ele_lst.append(self.root)

			if self.right:
				self.right.in_order_trav(ele_lst)
		return ele_lst

	
	def lev_order_trav(self):
		lev_list=[]
		lev_que=Queue()
		if self.root:
			lev_que.enque(self)
			
			while not lev_que.isEmpty():
				node=lev_que.deque()
				lev_list.append(node.root)
				if node.left:
					lev_que.enque(node.left)
				if node.right:
					lev_que.enque(node.right)
		return lev_list


	def search_node(self,value):
		if self.root==value:
			return True;
		elif value<self.root:
			if self.left:
				return self.left.search_node(value)
			else:
				return False
		elif value>self.root:
			if self.right:
				return self.right.search_node(value)
			else:
				return False
		else:
			return False

	def findclosest(self,target,closest):

		if target==self.root:
			return target;

		if abs(closest-target)>abs(self.root-target):
			closest=self.root

		if target<self.root:
			if self.left:
				closest=self.left.findclosest(target,closest)
			else:
				return closest
		else:
			if self.right:
				closest=self.right.findclosest(target,closest)
			else:
				return closest

		return closest


#---------------------------------------------------------------

if __name__=="__main__":
	bst=BinSearchTree(5)
	bst.add_node(1)
	bst.add_node(2)
	bst.add_node(3)
	bst.add_node(4)
	bst.add_node(6)
	bst.add_node(7)
	bst.add_node(8)
	bst.add_node(9)
	bst.add_node(10)
	print(bst.pre_order_trav())
	print(bst.post_order_trav())
	print(bst.in_order_trav())
	print(bst.search_node(9))
	print(bst.search_node(15))
	print(bst.lev_order_trav())
	print(bst.findclosest(5.9,9999))


