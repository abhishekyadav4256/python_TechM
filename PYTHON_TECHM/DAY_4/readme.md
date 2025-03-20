# README - Python Sequences and Operations

## 1. Define a sequence. What types of sequences exist in Python?

A sequence is an ordered collection of elements that can be indexed and iterated over. Python provides the following types of sequences:

- **Immutable Sequences**: `str`, `tuple`, `bytes`
- **Mutable Sequences**: `list`, `bytearray`

---

## 2. How are strings, lists, and tuples different from each other?

| Feature      | String (`str`) | List (`list`) | Tuple (`tuple`) |
|-------------|---------------|--------------|---------------|
| Mutability  | Immutable     | Mutable      | Immutable     |
| Elements    | Characters    | Any data type | Any data type |
| Performance | Faster        | Slower (modifications) | Faster (fixed size) |
| Syntax      | "hello"       | `[1, 2, 3]`  | `(1, 2, 3)`  |

---

## 3. Explain how indexing works in Python with an example.

Indexing in Python starts from `0` (first element) and `-1` (last element).

```python
my_list = [10, 20, 30, 40]
print(my_list[0])  # Output: 10
print(my_list[-1])  # Output: 40
```

---

## 4. Write code to access the last character of a string.

```python
text = "Python"
print(text[-1])  # Output: n
```

---

## 5. Create a list of numbers and access the third element.

```python
numbers = [5, 10, 15, 20, 25]
print(numbers[2])  # Output: 15
```

---

## 6. What is the result of `len([1, [2, 3], 4])` and why?

**Output:** `3`

**Explanation:** The list contains three elements: `1`, `[2, 3]` (a sublist), and `4`.

---

## 7. Explain slicing with a practical example.

```python
text = "Programming"
print(text[0:5])   # Output: Progr (from index 0 to 4)
print(text[:4])    # Output: Prog (implicit start at 0)
print(text[5:])    # Output: amming (implicit end)
print(text[::2])   # Output: Pormig (every second character)
```

---

## 8. How would you reverse a string using slicing?

```python
text = "Python"
print(text[::-1])  # Output: nohtyP
```

---

## 9. Demonstrate list concatenation and repetition with examples.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2  # [1, 2, 3, 4, 5, 6]
repeated = list1 * 2  # [1, 2, 3, 1, 2, 3]
```

---

## 10. Write code to count the occurrences of an element in a list.

```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # Output: 3
```

---

## 11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?

**Output:** `(2, 3)`

---

## 12. Explain the difference between `list.append()` and `list.extend()`.

- **`append(x)`**: Adds `x` as a single element.
- **`extend(iterable)`**: Adds each element of `iterable` to the list.

```python
l = [1, 2]
l.append([3, 4])  # [1, 2, [3, 4]]
l.extend([3, 4])  # [1, 2, 3, 4]
```

---

## 13. Write code to split the sentence into words.

```python
sentence = "Learn Python, step by step!"
words = sentence.split()
print(words)  # Output: ['Learn', 'Python,', 'step', 'by', 'step!']



## 14. Join a List into a Single String

```python
words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: Python is fun
```

### 15. Find the Index of the First Occurrence of 2 in a List

```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))  # Output: 1
```

### 16. Check if a String is a Palindrome

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
```

### 17. Return the Length of the Longest Word in a Sentence

```python
def longest_word(sentence):
    return max(len(word) for word in sentence.split())

print(longest_word("Python programming is fun"))  # Output: 11
```

### 18. Demonstrate Nested List Indexing

```python
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])  # Output: 6
```

### 19. Convert a List of Characters into a String

```python
chars = ['H', 'e', 'l', 'l', 'o']
print("".join(chars))  # Output: Hello
```

### 20. Remove Duplicates from a List While Preserving Order

```python
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))  # Output: [1, 2, 3, 4, 5]
```

### 21. Sort a List of Tuples by the Second Element

```python
def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_tuples([(1, 3), (4, 1), (2, 2)]))  # Output: [(4, 1), (2, 2), (1, 3)]
```

### 22. Flatten a Nested List of Arbitrary Depth

```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

### 23. Rotate a List to the Right by k Steps

```python
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
```

### 24. Check if Two Strings are Anagrams

```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Output: True
```

### 25. Split a List into Chunks of a Specified Size

```python
def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print(chunk_list([1, 2, 3, 4, 5], 2))  # Output: [[1, 2], [3, 4], [5]]
```

### 26. Merge Two Sorted Lists into One Sorted List

```python
def merge_sorted_lists(l1, l2):
    return sorted(l1 + l2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```