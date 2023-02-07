#### LEARN INTERMEDIATE PYTHON 3
# Event Coordinator

You are starting up your own event coordination business and want to create a Python application using generators to help manage your events.

This project will help you practice and further master the use of generators by managing and coordinating customer events for your business.

---

You are managing your first customer event! You’ve been provided a guestlist of names and their ages that are within the file guest_list.txt.

Within the file script.py, there is a defined function called read_guestlist() that will read in the guestlist file line by line. This function will separate the name and age values and store them into variables named name and age respectively.

Modify this function to be a generator function that will yield each read line so that each guest name is yielded each time for the generator.

Using a for loop, iterate through the generator object that is retrieved by calling the generator function read_guestlist() and print out the first 10 guests on the guestlist.

---

We’ve printed out our first 10 guests when our phone rings! It’s our customer who has another guest to add to the guestlist.

She wants to add a guest with the information: "Jane,35". Use one of the three generator methods we have learned to accomplish this.

---

We can now finish yielding the rest of the names on the guestlist file to our generator by adding numerous next() calls on the generator object until a StopIteration exception is reached. This can also be accomplished by using a for loop on the generator object to automatically make the appropriate amount of next() calls.

---


Now that we have all our guests, we want to see which guests are aged 21 and over so that we can inform the bartending vendor.

Define a generator expression that will use the guests dictionary to retrieve a generator of names of all guests who are 21 and over.

We should see our newly added guest, Jane on this list as well!

---

Connected Generators & Generator Pipelines


Now it’s time to assign meals to each table and the seats at the tables. Our event will have 3 tables with 5 seats at each.

Create 3 separate generator functions, one for each table, that will yield tuples of ("Food Name", "Table X", "Seat Y") for each of the 5 seats at each table.

You may use the following foods for the tables: Chicken, Beef, Fish.

---

Finally, we want to assign a table and seat number with meal selection to each guest. Create another generator function that will take in as input our guests dictionary and the connected generator seating/food selection we created in the previous step. This function should yield a tuple of the guest name and the next value from the connected generator.

---

Congratulations, you were able to successfully plan and coordinate your first event!

Through this project, you were able to reinforce what generators are, how they can be created, manipulated, and connected together to perform complex generator operations.