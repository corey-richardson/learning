# New Teacher in Town

You are a new teacher at Pine Valley Elementary School!

This project will help you practice and further master the learned material from the Iterables and Iterators lesson by utilizing the information learned to set up and organize your new classroom and roster of students.

---

It’s the first day of summer and you have a new incoming class of elementary students to prepare for in the coming months!

First, look at the code in roster.py. You have been provided a roster of students for the 10 children in your class. Each child’s record contains name, age, height (in inches), favorite classroom subject, and favorite animal to help you get to know them better.

We’ve learned that an iterable is simply a Python object that can be traversed. This list of dictionaries is your first iterable. Navigate to script.py and import the student_roster list from roster.py. Create an iterator for the student_roster list and print out each student’s information using next().

---

Now that we know a little more about the students in our classroom, let’s start organizing the classroom! First, we should create a custom class that will allow us to manage our classroom and students.

You’ve been provided a file called classroom_organizer.py. Start defining out your custom ClassroomOrganizer class.

First, we should import the student_roster list from the roster.py file so that we can utilize it within our custom class. Another module we will need later on will be the itertools module. Let’s import these both into the classroom_organizer.py file now.

---

Next, we want to create a simple way to run through morning roll call, by ordering all students by first name alphabetically. When you iterate on your ClassroomOrganizer object, it should return each student’s name one at a time on each next() call or for loop iteration.

Define the iterator protocol for our ClassroomOrganizer class that can achieve this. Once defined, use either next() calls or a for loop on the ClassroomOrganizer object to print out the next student on the roll call.

---


Next, we need to organize our classroom and decide where our students will be sitting. We have 5 tables in our classroom that can seat 2 students each. We’d like to see what combination of students we can put at each table.

Using the itertools module, define a method within ClassroomOrganizer that will retrieve a final list of all tuple combinations of 2 students that can be seated at each table.

From script.py, print out the result to see all the possible combinations.

---

You are offering an afterschool program for those students whose favorite subjects are Math and Science.

Your tables can fit 4 students at them. Retrieve a list of all 4 combinations of students whose favorite subjects are Math and Science.

The get_students_with_subject() method can be used to retrieve iterables for each of the subjects.

From script.py, print the final list of combinations.

---

Congrats, you were able to set up and organize your student roster, classroom, and school programs!

Through this project, you were able to reinforce what iterables and iterators are, how to write custom classes that can be made into iterables, and how to use various Python itertools to manipulate iterables.

You may use the remaining dictionary info within the student roster list (favorite animal, height, age) to practice more with itertools or custom iterators.