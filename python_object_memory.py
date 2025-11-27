# Python Object Memory Management Deep Dive

# Let's explore Python's object creation and memory management
import psutil
print("=== DEMONSTRATING OBJECT CREATION ===")

# Example 1: Integer object creation
x = 1
print(f"x = 1, id: {id(x)}")

x = x + 1
print(f"x = x + 1 = 2, id: {id(x)}")
print(f"New object created: {id(1) != id(2)}")

print("\n=== PYTHON'S INTEGER CACHING (Small Integer Optimization) ===")

# Python caches small integers (-5 to 256) for efficiency
a = 100
b = 100
print(f"a = 100, id: {id(a)}")
print(f"b = 100, id: {id(b)}")
print(f"Same object? {a is b}")  # True - same object in memory

# But not for large integers
c = 1000
d = 1000
print(f"c = 1000, id: {id(c)}")
print(f"d = 1000, id: {id(d)}")
print(f"Same object? {c is d}")  # Larger numbers may or may not be cached depending on context.
# Constants in the same code block can be interned by compiler optimizations.

print("\n=== STRING INTERNING OPTIMIZATION ===")

# Python interns some strings to save memory
str1 = "hello"
str2 = "hello"
print(f"str1 = 'hello', id: {id(str1)}")
print(f"str2 = 'hello', id: {id(str2)}")
print(f"Same object? {str1 is str2}")  # True

# But not all strings
str3 = "hello world with spaces"
str4 = "hello world with spaces"
print(f"str3 id: {id(str3)}")
print(f"str4 id: {id(str4)}")
print(f"Same object? {str3 is str4}")  # Might be False

print("\n=== MUTABLE vs IMMUTABLE OBJECTS ===")

# Immutable types create new objects
print("--- Immutable Types (int, str, tuple) ---")
original_int = 42
print(f"Original int id: {id(original_int)}")

modified_int = original_int + 1
print(f"Modified int id: {id(modified_int)}")
print(f"Different objects: {id(original_int) != id(modified_int)}")

# Mutable types modify in place
print("\n--- Mutable Types (list, dict, set) ---")
original_list = [1, 2, 3]
print(f"Original list id: {id(original_list)}")

original_list.append(4)  # Modifies in place
print(f"After append, list id: {id(original_list)}")
print(f"Same object: {id(original_list) == id(original_list)}")

print("\n=== MEMORY EFFICIENCY ANALYSIS ===")

import sys
import gc

# Function to get object count
def get_object_count():
    return len(gc.get_objects())

# Test 1: Multiple integer operations
print("--- Integer Operations Impact ---")
initial_objects = get_object_count()
print(f"Initial object count: {initial_objects}")

# Simulate many integer operations
result = 0
for i in range(1000):
    result = result + i

final_objects = get_object_count()
print(f"After 1000 integer operations: {final_objects}")
print(f"Net objects created: {final_objects - initial_objects}")

# Test 2: Using mutable objects instead
print("\n--- Using Mutable Container ---")
initial_objects = get_object_count()
counter = [0]  # Mutable container

for i in range(1000):
    counter[0] = counter[0] + i  # Still creates new int objects, but container stays same

final_objects = get_object_count()
print(f"After operations with mutable container: {final_objects}")
print(f"Net objects created: {final_objects - initial_objects}")

print("\n=== GARBAGE COLLECTION DEMONSTRATION ===")

import weakref

class TestObject:
    def __init__(self, value):
        self.value = value
    
    def __del__(self):
        print(f"Object with value {self.value} is being garbage collected")

# Create objects and see when they're collected
obj1 = TestObject(1)
obj1_id = id(obj1)

# Create a weak reference to track when object is deleted
weak_ref = weakref.ref(obj1)

print(f"Object created, id: {obj1_id}")
print(f"Weak reference alive: {weak_ref() is not None}")

# Reassign - old object becomes eligible for GC
obj1 = TestObject(2)

# Force garbage collection
gc.collect()

print(f"After reassignment, weak reference alive: {weak_ref() is not None}")

print("\n=== OPTIMIZATION STRATEGIES ===")

# Strategy 1: Use built-in functions (implemented in C)
print("--- Built-in vs Manual Operations ---")
import time

# Manual summation (creates many intermediate objects)
start_time = time.time()
result = 0
for i in range(100000):
    result = result + i
manual_time = time.time() - start_time

# Built-in sum (optimized in C)
start_time = time.time()
result = sum(range(100000))
builtin_time = time.time() - start_time

print(f"Manual summation time: {manual_time:.4f}s")
print(f"Built-in sum time: {builtin_time:.4f}s")
print(f"Built-in is {manual_time/builtin_time:.2f}x faster")

# Strategy 2: Use appropriate data structures
print("\n--- String Concatenation Comparison ---")

# Inefficient: creates new string objects repeatedly
start_time = time.time()
result = ""
for i in range(1000):
    result = result + str(i)  # Creates new string each time
inefficient_time = time.time() - start_time

# Efficient: use list and join
start_time = time.time()
result_list = []
for i in range(1000):
    result_list.append(str(i))  # Append to mutable list
result = "".join(result_list)  # Single string creation
efficient_time = time.time() - start_time

print(f"String concatenation time: {inefficient_time:.4f}s")
print(f"List join time: {efficient_time:.4f}s")
print(f"List join is {inefficient_time/efficient_time:.2f}x faster")

print("\n=== MEMORY PROFILING EXAMPLE ===")

def memory_intensive_function():
    """Function that creates many temporary objects"""
    data = []
    for i in range(10000):
        # Each iteration creates new objects
        temp_str = f"item_{i}"
        temp_dict = {"id": i, "name": temp_str, "value": i * 2}
        data.append(temp_dict)
    return data

# Monitor memory before and after
import psutil
import os

process = psutil.Process(os.getpid())
before_memory = process.memory_info().rss / 1024 / 1024  # MB

result = memory_intensive_function()

after_memory = process.memory_info().rss / 1024 / 1024  # MB

print(f"Memory before function: {before_memory:.2f} MB")
print(f"Memory after function: {after_memory:.2f} MB")
print(f"Memory increase: {after_memory - before_memory:.2f} MB")

print("\n=== WHY THIS DESIGN ISN'T AS INEFFICIENT AS IT SEEMS ===")

print("""
1. **Small Object Caching**: Python caches small integers (-5 to 256) and some strings
2. **Fast Allocation**: Python's memory allocator is optimized for small objects
3. **Reference Counting**: Objects are freed immediately when references drop to 0
4. **Memory Pools**: Python reuses memory blocks for objects of similar sizes
5. **Generational GC**: Focuses on short-lived objects (most new objects die young)
6. **Immutability Benefits**: Thread safety, hashability, caching opportunities

The trade-offs:
- **Pros**: Thread safety, simplicity, prevents accidental mutations
- **Cons**: More memory allocations, some performance overhead

For performance-critical code:
- Use NumPy for numeric computations (in-place operations)
- Use appropriate data structures (lists for building, join for strings)
- Leverage built-in functions (implemented in C)
- Consider libraries like Numba for JIT compilation
""")

print("\n=== COMPARATIVE PERFORMANCE TEST ===")

# Compare different approaches for accumulation
import timeit

def test_immutable_accumulation():
    result = 0
    for i in range(1000):
        result = result + i
    return result

def test_mutable_accumulation():
    result = [0]
    for i in range(1000):
        result[0] = result[0] + i
    return result[0]

def test_builtin_accumulation():
    return sum(range(1000))

# Time each approach
immutable_time = timeit.timeit(test_immutable_accumulation, number=1000)
mutable_time = timeit.timeit(test_mutable_accumulation, number=1000)
builtin_time = timeit.timeit(test_builtin_accumulation, number=1000)

print(f"Immutable approach: {immutable_time:.4f}s")
print(f"Mutable container: {mutable_time:.4f}s")
print(f"Built-in function: {builtin_time:.4f}s")

print(f"\nBuilt-in is {immutable_time/builtin_time:.2f}x faster than immutable approach")
print(f"Mutable container is {immutable_time/mutable_time:.2f}x faster than immutable approach")