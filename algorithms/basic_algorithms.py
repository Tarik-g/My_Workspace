# best O(1), average/ worst O(log n)
def binary_search(sorted_list, target):
    right = len(sorted_list) -1
    left = 0
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_list[mid] == target:
            return mid
        elif target < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Trie insert and search O(m) (m is wordlength)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    

# Insertion/Deletion: O(log n)
# Accessing Min/Max: O(1)
import heapq

# Min-Heap example
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 15)

# Get the smallest element
min_element = heapq.heappop(heap)

# Max-Heap can be implemented by pushing negative values
heap = []
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)
heapq.heappush(heap, -15)

# Get the largest element by popping and negating
max_element = -heapq.heappop(heap)
