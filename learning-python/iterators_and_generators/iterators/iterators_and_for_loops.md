```py
dog_foods = {
    "Great Dane Foods": 4,
    "Min Pip Pup Foods": 10,
    "Pawsome Pup Foods": 8
}
for food_brand in dog_foods:
    print (food_brand + " has " + str(dog_foods[food_brand]) + " bags")
```

1. The for loop will first retrieve an iterator object for the dog_foods 
dictionary using iter().

2. Then, next() is called on each iteration of the for loop to retrieve 
the next value. This value is set to the for loop’s variable, food_brand.

3. On each for loop iteration, the print statement is executed, until finally,
 the for loop executes a call to next() that raises the StopIteration exception.
  The for loop then exits and is finished iterating.

  ![](https://static-assets.codecademy.com/Courses/Intermediate-Python/Iterables3-final.gif)