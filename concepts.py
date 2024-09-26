# NOTE: ----------------------------------VARIABLES------------------------------------
#   - Variables in python are dynamically typed. This means that we don't need to 
#     declare types in variable declerations, and any variable can become any type.
#   - Types are determined at runtime in python
#   - Python allows for multiple variable assignment as well: a, b = 0, "hello"
#   - Incramenting in python is simple: n += 1 || n = n + 1
#   - Null in python in the None keyword
def variables():
    n = 1200
    print("n = ", n)
    n = "I am now a string type"
    print("n = ", n)

    x, y, z = 213, False, 3.14195
    print("x = ", x)
    print("y = ", y)
    print("z = ", z)

    empty = None
    print("empty = ", empty)


# NOTE: --------------------------------IF STATEMENTS----------------------------------
#   - Python uses indentation for if statements as it's block
#   - You need to add parenthenses for multiline conditions
#   - Else if statements are used with the elif keyword: elif x == y:
#   - Logical AND in python is and rather than &&
#   - Logical OR in python is or rather than ||
def if_statements():
    n, m = 1, 2

    if ((n > 2) and 
        (n != m) or n == m):
        n += 1

    print("n = ", n)
    print("m = ", m)

    if n == m:
        print("equal")
    elif n > m:
        print("n is greater")
    else:
        print("m is greater")


# NOTE: ------------------------------------LOOPS--------------------------------------
#   - While loops in python are used with the while keyword => while n != 5:
#   - For loops are used with the range function => for i in range(5):
#   - The range function takes in a stop number, start & stop number, or start, stop and incrament number
#   - Range example: range(5) => 0, 1, 2, 3, 4
#   - Range example: range(1, 5) => 1, 2, 3, 4
#   - Range example: range(2, 10, 2) => 2, 4, 6, 8 
#   - Range example: range(5, 0, -1) => 5, 4, 3, 2, 1
def loops():
    n = 0
    while n < 5:
        print("n = ", n)
        n += 1

    for i in range(2, 10, 2):
        print("i = ", i)


# NOTE: ------------------------------------LISTS--------------------------------------
#   - To initialize a new array: arr = [1, 2, 3]
#   - Arrays in python are dynamic by default
#   - To add a new value to the end of the list: arr.append(4) => [1, 2, 3, 4]
#   - To remove the last value from a list: arr.pop() => [1, 2, 3]
#   - To insert a new value at specified position: arr.insert(1, 7) => [1, 7, 2, 3]
#   - To access the array elements: arr[3] => 3
#   - The follow statement initializes an array of size 5 with all 1's: arr = [1] * 5
#   - To get the length of an array: len(arr)
#   NOTE: Array index is different in python as negative indecies wrap to the back of the array
#   - For example arr[-1] gets the last element in the array (-2 would be second last element and so on ...)
#   - Unpacking is a technique where we can take the all the individual elements of an array: a, b, c = [1, 2, 3]
#   - Unpacking is useful when you want to go through a list of pairs
#   NOTE: If the variables on the left side doesnt equal the number of elements and error is thrown: a, b = [1, 2, 3]
def lists():
   arr1 = [1, 2, 3, 4, 5, 6, 7]
   print("arr1 = ", arr1)

   arr1.append(10)
   arr1.pop()

   arr2 = [1] * 10
   print("arr2 = ", arr2)

   nums = [121, 1413, 124, 12, 8746, 478, 76, 8, 653, 87, 3586]

   # looping though an array with an index
   for i in range(len(nums)):
       print(nums[i])
   
   # looping through an array without indexing
   for num in nums:
       print(num)

   # looping through an array with index and value
   for i, num in enumerate(nums):
       print(f"index: {i} value: {num}")

   # reversing an array
   nums.reverse()
   # sorting an array, in ascending order by default
   nums.sort()
   # sorintg an array in reverse order
   nums.sort(reverse=True)


# NOTE: -----------------------------------SLICING-------------------------------------
#   - List slicing in python takes a slice of an existing list and creates a new list 
#     with the sliced indexes
#   - Given an array with values arr = [1, 2, 3, 4, 5, 6, 7, 8]
#   - To slice elements with use: arr[1:3] => [2, 3]
#   - Slices start from the index and stop and the last index (not including its value)
def list_slicing():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sub_list = arr[2:6] # => [3, 4, 5, 6]
    print("arr = ", arr)
    print("sub_list = ", sub_list)


# NOTE: ------------------------------LIST COMPREHENSION-------------------------------
#   - List comprehension offers a shorter syntax when you want to create a new list
#     based on the values of an existing list.
#   - For example: [`operation` for `x` in `array`]
def list_comprehension():
    vec = [-4, -2, 0, 2, 4]
    print("vec = ", vec)

    # create an array with the values doubled in vec
    doubled = [x*2 for x in vec]
    print("vec doubled = ", doubled)

    # fliter the array to include positive numbers only
    positive = [x for x in vec if x >= 0]
    print("vec positive nums = ", positive)

    # create an array with values 1-20
    arr = [x for x in range(1, 21)]
    print("array from 1 - 20: ", arr)


# NOTE: -----------------------------------STRINGS-------------------------------------
#   - Strings can be sliced the same way as arrays in python
#   - Strings use "" and ''
#   - Strings in python are immutable, meaning we can not modify them
#   - Strings can be converted to integers with the int() function
#   - We can also ge the ascii value of a char using the ord() function
def strings():
    letters = "abcd"
    letters += "efg"

    ascii_a = ord(letters[0])
    print("ascii value of a = ", ascii_a)

    # we can join a list of strings with the join function
    arr = ["These", "letters", "are", "in", "an", "array"]
    sentence = " ".join(arr)
    print(sentence)


# NOTE: ------------------------------------QUEUES-------------------------------------
#   - Queues in python are double ended by default (elements can be added/removed from head or tail)
#   - They are imported using the collections library: from collections import deque
#   - The append() function adds values to the right side of the queue
#   - You can pop from the left of the queue in constant time O(1) with the popleft() function
#   - Since the queue is double ended we can also add values to the left of the queue: appendleft()
#   - We can pop from the right side of the queue with the pop() function
def queues():
    from collections import deque

    queue = deque()
    queue.append(1)
    queue.append(2)
    print("queue = ", queue)

    queue.popleft()
    print(queue)

    queue.appendleft(32)
    print(queue)

    queue.pop()
    print(queue)


# NOTE: -----------------------------------HASH SETS-----------------------------------
#   - Hashsets are useful because we can search them in constant time O(1)
#   - You can define a hash set with the set() function
#   - To add a value to the hash set use the add function
#   - Hashsets cannot contain any duplicate values
#   - We can get the length of a hashset with len(hashset)
#   - We can search the hashset with the in operator: 1 in hashset (returns a boolean)
#   - We can remove values also in constant time with the remove() function
#   - To initialize a hash set with multiple values we can use a list: vals = set([1, 2, 3, 45, 5])
#   - We can also do set comprehension just like with lists: mySet = {x for x in range(5)}
def hash_sets():
    hash_set = set()

    hash_set.add(1)
    hash_set.add(2)
    print(hash_set)

    length = len(hash_set)

    exists = 2 in hash_set
    exists = 3 in hash_set


# NOTE: -----------------------------------HASH MAPS-----------------------------------
#   - Hash maps are the datastructure we will be using the most
#   - Hash maps take a key and a value to create
#   - Just like with hash sets we cant have duplicate keys
#   - Getting the length is the same with len()
#   - We can search if a key exists in the map with the in operator: "Luka" in myMap (returns boolean value)
#   - Removing a key from the hash map: myMap.pop("Luka")
#   - We can also use hash map comprehension: myMap = {i: 2*1 for i in range(5)}
#   - Looping through a hashmap=> for key in map: OR we can directly iterate through the values=> for val in myMap.values():
#   - Using unpacking we can iterate through the keys and the values=> for key, val in myMaps.items():
def hash_maps():
    myMap = {}
    myMap["alice"] = 90
    myMap["John"] = 91
    myMap["Luka"] = 92
    print(myMap)

    newMap = {0: "A", 1: "B", 2: "C", 3: "D"}
    print("map = ", newMap)

    graph = {i: i*2 for i in range(5)}
    print("graph = ", graph)


# NOTE: ------------------------------------TUPLES-------------------------------------
#   - Tuples are similar to array but they are immutable
#   - Tuples will mainly be used as keys for a hash maps/sets
#   - You must use tuples as hash maps/sets keys because lists are not able to be
def tuples():
    tup = (1, 2, 3)
    print("tup = ", tup)

    # using tuple as a key for hash map/sets
    graph = {(0, 0): "A", (0, 1): "B", (0, 2): "C"}
    print("graph = ", graph)

# NOTE: ------------------------------------HEAPS--------------------------------------
#   - Heaps are a common data structure to find the min and max of a set of values frequently
#   - Under the hood they are implemented with arrays in python
#   - To use heaps import the heapq library
#   - To push values to the heap with use heapq.heappush(minHeap, 3)
#   - By default heaps in python are min heaps
#   - To get the length of a heap use the len() function 
#   - To pop values from the heap use heappop() 
#   - Python does not have max heaps by deafult. The work around is to multiply each value that 
#     we push by -1
#   - To build a heap from an existing array we use the heapify() function which builds the heap in 
def heaps():
    import heapq

    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 965)
    #print("minheap = ", minHeap)

    #print("min value = ", minHeap[0])

    # Max heap example 
    heapList = [12, 342, 235, 13, 0, -123, 412, 41, 124, 523, 1234, 3214, 11123, 5517]
    #print(f"Max heap (before) = {heapList}")
    heapq._heapify_max(heapList)
    #print(f"Max heap (after) = {heapList}")

        

# NOTE: ----------------------------------------MAPS---------------------------------------------
#   - The map function applies a function to every item in a list, and returns a new list
#   - Map return a map object which is an iterator
def maps():
    def square(n):
        return n * n

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums_squared = list(map(square, nums))

    print('nums = ', nums)
    print('nums_squared = ', nums_squared)


# NOTE: Dictionaries
def dicts():
    # define a dictionary
    ex = {"k1": "v1", "k2": "v2", "k3": 900}

    # to loop through the dictionary, call the method .items()
    # this turns it into a list of tuples containing the k/v pairs
    for key, value in ex.items():
        print(str(key) + ": " + str(value))



def main():
    # variables()
    # if_statements()
    # loops()
    # lists()
    # list_slicing()
    # list_comprehension()
    # strings()
    # queues()
    # hash_sets()
    # hash_maps()
    # tuples()
    # heaps()
    # maps()
    dicts()


# Main function 
if __name__ == "__main__":
    main()
