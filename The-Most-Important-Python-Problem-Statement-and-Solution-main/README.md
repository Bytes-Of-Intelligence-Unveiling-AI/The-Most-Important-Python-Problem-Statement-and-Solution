




## 1. **Decorate Sort Undecorate Idiom (DSU):**
   
The **Decorate Sort Undecorate Idiom (DSU):** idiom is a programming technique used to sort a list of items based on some criteria while retaining the original order of equal items. It involves three steps:

1. **Decorate**: Create a new list of tuples, where each tuple contains the original item and the value computed based on the sorting criteria.
2. **Sort**: Sort the list of tuples based on the computed values.
3. **Undecorate**: Extract the original items from the sorted list of tuples.

Here's an example of how you can use the DSU idiom in Python:

Suppose you have a list of strings representing names, and you want to sort them based on their lengths while preserving the original order of names with the same length.

```python
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen"]

# Decorate: Create a list of tuples (name, length)
decorated_names = [(name, len(name)) for name in names]

# Sort: Sort the list of tuples based on the second element (length)
decorated_names.sort(key=lambda x: x[1])

# Undecorate: Extract the sorted names from the list of tuples
sorted_names = [name for name, _ in decorated_names]

print(sorted_names)
```

**Output:**
```
['Bob', 'Eve', 'Alice', 'David', 'Frank', 'Grace', 'Charlie', 'Helen']
```


``` python 

def schwartzian(arr, f):
    return [t[0] for t in sorted([(v, f(v)) for v in arr], key=lambda t: t[1])]


TEST = ["Rosetta", "Code", "is", "a", "programming", "chrestomathy", "site"]

print(TEST, "=>", schwartzian(TEST, len))


```
**Output:**

```
['Rosetta', 'Code', 'is', 'a', 'programming', 'chrestomathy', 'site'] => ['a', 'is', 'Code', 'site', 'Rosetta', 'programming', 'chrestomathy']
```

In this example, the DSU idiom was used to sort the list of names based on their lengths while maintaining the original order for names with the same length.

You can adapt this idiom for various sorting criteria by changing the key function used during sorting.
