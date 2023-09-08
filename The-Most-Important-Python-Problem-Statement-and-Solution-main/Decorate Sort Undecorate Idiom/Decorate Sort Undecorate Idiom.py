names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen"]

# Decorate: Create a list of tuples (name, length)
decorated_names = [(name, len(name)) for name in names]

# Sort: Sort the list of tuples based on the second element (length)
decorated_names.sort(key=lambda x: x[1])

# Undecorate: Extract the sorted names from the list of tuples
sorted_names = [name for name, _ in decorated_names]

print(sorted_names)


## Output: 
['Bob', 'Eve', 'Alice', 'David', 'Frank', 'Grace', 'Charlie', 'Helen']
