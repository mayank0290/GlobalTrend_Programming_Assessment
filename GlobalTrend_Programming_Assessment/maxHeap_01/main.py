class MaxHeap: 

    # heap initialization
    def __init__(self):
        self.heap = []

    # insert operations (appending an element in the end while maintaining the property)
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)

    # delete operations
    def delete(self, val):
        if len(self.heap) == 0:  # to check whether the list is empty before trying to delete the value 
            return 
        ind = self.heap.index(val)  # finding the index of the value to be deleted
        self._swap(ind, len(self.heap) - 1)  # swapping the element with the last element to avoid disrupting the heap structure, for this we use _swap method
        self.heap.pop()  # removing the element which is now at the end of the list 
        self._heapify_down(ind)  # to swap back the element which was in the end of the list to maintain the heap property

    # to get the max element
    def get_max(self):
        if len(self.heap) == 0:
            return None 
        return self.heap[0]  # returning the max element which is root node with the index 0

    # to use heapify_up method after insertion 
    def _heapify_up(self, ind):
        parent_ind = (ind - 1) // 2  # to find the parent node position 

        if ind <= 0:  # if the current node is the root node (index = 0), then there's no parent node to compare with
            return

        if self.heap[parent_ind] < self.heap[ind]:  # to check if the parent node is smaller than the current node, if yes then it needs to be swapped
            self._swap(parent_ind, ind)  # swapping the parent and current node 
            self._heapify_up(parent_ind)  # heaping up the parent node recursively 

    # to use heapify_down after deletion 
    def _heapify_down(self, ind):
        left_child_ind = 2 * ind + 1  # evaluating the indices of left and right child nodes
        right_child_ind = 2 * ind + 2 
        largest = ind  # let's assume current node is the largest in the heap

        # now to check if the left child node is in the range of the heap and bigger than the current node 
        if left_child_ind < len(self.heap) and self.heap[left_child_ind] > self.heap[largest]:
            largest = left_child_ind

        # similarly we go for right child 
        if right_child_ind < len(self.heap) and self.heap[right_child_ind] > self.heap[largest]:
            largest = right_child_ind

        # if the largest value is not the current node then it will be swapped with the largest child and heapify down 
        if largest != ind:
            self._swap(largest, ind)
            self._heapify_down(largest)

    def _swap(self, i, j):
        # utilizing the swap method to swap the values at indices at position i and j 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example is as follows
# inserting elements
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
max_heap.insert(25)
max_heap.insert(15)

print("Heap after insertions:", max_heap.heap)  # print the heap list
print("Max element:", max_heap.get_max())  # print 25

# deleting an element
max_heap.delete(20)
print("Heap after deleting 20:", max_heap.heap)  # print the heap list without 20
print("Max element:", max_heap.get_max())  # print the new max element
