import math

class Median:
    def __init__(self):
        self.max_array = list()
        self.min_array = list()

    def left(self, el):
        return el*2 + 1

    def right(self, el):
        return el*2 + 2

    def parent(self, el):
        return round(el/2)-1

    def add_element(self, value):
        print("this is ")
        print(self.max_array)
        print(self.min_array)
        if len(self.min_array) == 0 and len(self.max_array) == 0:
            self.max_heap_insert(value)
            self.build_max_heap()

        elif value < self.max_array[0]:
            self.max_heap_insert(value)
            self.build_max_heap()
        else:
            self.min_heap_insert(value)
            self.build_min_heap()

        if len(self.min_array) - len(self.max_array) > 1:
            self.max_array.append(self.heap_extract_min())

        elif len(self.max_array) - len(self.min_array) > 1:
            self.min_array.append(self.heap_extract_max())

        self.build_max_heap()
        self.build_min_heap()

    def get_median(self):
        if len(self.max_array) == len(self.min_array) and len(self.max_array) + len(self.min_array) > 1:
            return (self.max_array[0], self.min_array[0], )

        elif len(self.max_array) > len(self.min_array):
            return self.max_array[0]
        else:
            return self.min_array[0]



    def get_maxheap_elements(self):
        return self.max_array

    def get_minheap_elements(self):
        return self.min_array


    def max_heapify(self, el):

        l = self.left(el)
        r = self.right(el)

        if l < len(self.max_array) and self.max_array[l] > self.max_array[el]:
            largest = l
        else:  ###
            largest = el

        if r < len(self.max_array) and self.max_array[r] > self.max_array[largest]:
            largest = r

        if largest != el:
            temp = self.max_array[el]
            self.max_array[el] = self.max_array[largest]
            self.max_array[largest] = temp
            self.max_heapify(largest)


    def build_max_heap(self): ###0

        for el in range(len(self.max_array) // 2, -1, -1):
            self.max_heapify(el)

    def min_heapify(self, el):
        l = self.left(el)
        r = self.right(el)

        if l < len(self.min_array) and self.min_array[l] < self.min_array[el]:
            smallest = l
        else: ###
            smallest = el

        if r < len(self.min_array) and self.min_array[r] < self.min_array[smallest]:
            smallest = r

        if smallest != el:
            temp = self.min_array[el]
            self.min_array[el] = self.min_array[smallest]
            self.min_array[smallest] = temp
            self.min_heapify(smallest)

    def build_min_heap(self):
        for el in range(round(len(self.min_array)/2)-1, -1, -1):
            self.min_heapify(el)



    def heap_increase_key(self, el, key):
        if key < self.max_array[el]:
            raise Exception("New key is smaller")  # should be error
        self.max_array[el] = key
        while el > 0 and self.max_array[self.parent(el)] < self.max_array[el]:
            temp = self.max_array[el]
            self.max_array[el] = self.max_array[self.parent(el)]
            self.max_array[self.parent(el)] = temp
            el = self.parent(el)

    def max_heap_insert(self, key):
        self.max_array.append(-math.inf)
        self.heap_increase_key(len(self.max_array)-1, key)

    def heap_extract_max(self):
        if len(self.max_array) < 1:
            raise Exception("Heap underflow")
        max = self.max_array[0]
        self.max_array = self.max_array[1:]
        self.max_heapify(0)
        return max



    def heap_decrease_key(self, el, key):
        if key > self.min_array[el]:
            raise Exception("The new key is bigger than the existing element")
        self.min_array[el] = key

        while el > 0 and self.min_array[self.parent(el)] > self.min_array[el]:
            temp = self.min_array[el]
            self.min_array[el] = self.min_array[self.parent(el)]
            self.min_array[self.parent(el)] = temp
            el = self.parent(el)



    def min_heap_insert(self, key):
        self.min_array.append(math.inf)
        self.heap_decrease_key(len(self.min_array)-1, key)

    def heap_extract_min(self):
        if len(self.min_array) < 1:
            raise Exception("Heap underflow")
        min = self.min_array[0]
        self.min_array = self.min_array[1:]
        self.min_heapify(0)
        return min




a = Median()
a.add_element(9)
a.add_element(8)
a.add_element(6)
a.add_element(5)
a.add_element(4)
a.add_element(2)

a.max_heapify(0)
a.min_heapify(0)
print("__________")

print(a.get_maxheap_elements())
print(a.get_minheap_elements())
print(len(a.max_array))
print(len(a.min_array))
print(a.get_median())
print(a.heap_extract_min())
print(a.heap_extract_max())