# Lists

Lists are an ordered group of elements. Elements can be added, removed, accessed, and modified.

```py
products = ['t-shirt', 'pants', 'shoes', 'dress', 'blouse']
 
products.append('jacket')
products.sort()
products.remove('shoes')
```

# Tuples

Tuples are immutable objects which group multiple elements together. They are similar to lists, except that they cannot be modified once created.

```py
searched_terms = \
    ('clothes', 'phone', 'app', 'purchase', 'clothes', 'store', 'app', 'clothes')
 
term = searched_terms[2]
num_of_occurrences = searched_terms.count('clothes')
```

# Dictionaries

Dictionaries are unordered groups of key-value pairs.

```py
orders = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}, 
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}
         }
 
order_4829_price = orders['order_4829']['price']
order_6184_size = orders['order_6184']['size']
orders['order_4829']['size'] = 'x-large'
num_of_orders = len(orders)
```

# Sets

Sets are unordered groups of elements that cannot contain duplicates, elements cannot be modified.

```py
old_products_set = {'t-shirt', 'pants', 'shoes'}
new_products_set = {'t-shirt', 'pants', 'blouse', 'dress'}
updated_products = new_products_set | old_products_set
removed_products = old_products_set - new_products_set
```