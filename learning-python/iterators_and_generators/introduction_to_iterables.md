# Introduction to Iterables

In Python, an iterable is an object that is capable of being looped through one element at a time. We commonly use iterables to perform the process of iteration and it is the backbone for how we perform consistent operations on sets of data.

While these may be new terminologies, we have actually been using iterables frequently. Dictionaries, lists, tuples, and sets are all classified as iterables! We have even performed the process of iteration anytime we used looping mechanisms such as for loops. In this lesson, we are going to dive deeper into how looping (iteration) works under the hood and the role iterables play in it!

Before we dive into the details, let’s imagine we are the new owners of a pet store and need to keep track of certain inventory such as bags of food and their quantities. We can accomplish this using a dictionary.

Suppose we have the following information we need to store:

Dog Food Brand    | Quantity
------------------|------------
Great Dane Foods  |	4 bags
Min Pip Pup Foods |	10 bags
Pawsome Foods     | 8 bags

Using a dictionary, our data would take this form:

```py
dog_foods = {
    "Great Dane Foods": 4,
    "Min Pin Pup Foods": 10,
    "Pawsome Pups Foods": 8
}
```

Now if we wanted to display all the dog brands and their respective quantities, we could use a common loop such as the for loop to accomplish this goal. Our program might look something like this:

```py
for food_brand in dog_foods:
    print(food_brand + " has " + str(dog_foods[food_brand]) + " bags")
```

In this case, our iterable is the dictionary called dog_foods and the for loop performs the process of iteration that allows us to access each element. It looks a bit like magic, but what is actually happening under the hood here? How does the for loop iterate over each dictionary member and know when to stop iterating once the end is reached?

In the next sections, we will dive into answering these questions. For now, observe a high-level overview of the inner workings of our dog_foods loop.

---

![](https://static-assets.codecademy.com/Courses/Intermediate-Python/Iterables1%20(1)222.gif)

Review the image to see how our dog food for loop executes under the hood. Note the three core components that comprise the loop process. In the next sections we will explore:

- The iter() function that creates an iterator object out of iterables (such as our dictionary).
- The next() function that captures each individual value during the iteration process.
- The StopIteration exception that forces our loop to stop where there are no elements remaining.