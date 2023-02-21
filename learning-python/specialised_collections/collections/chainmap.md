First, we import the ChainMap container and set up our data.

```py
from collections import ChainMap

customer_info = {
    'name': 'Dmitri Buyer', 
    'age': '31', 
    'address': '123 Python Lane', 
    'phone_number': '5552930183'
    }

shirt_dimensions = {
    'shoulder': 20, 
    'chest': 42, 
    'torso_length': 29
    }

pants_dimensions = {'waist': 36, 
    'leg_length': 42.5, 
    'hip': 21.5, 
    'thigh': 25, 
    'bottom': 18
    }
```

Next, we initialize a ChainMap with the mappings which we want to use. In this case, the mappings are the dimensions dictionaries.

```py
customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)
```

Now we can access values from any of the stored mappings.

```py
customer_leg_length = customer_data['leg_length']
```


The parents property skips the first mapping and returns everything else (all of the parents of the first mapping).
```py
customer_size_data = customer_data.parents
```

We can directly modify the data only in the first dictionary.

```py
customer_data['address'] = '456 ChainMap Drive'
```