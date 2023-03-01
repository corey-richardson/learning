# Create a class called PoemFiles.
class PoemFiles:
    # Create an __init__ method inside of the PoemFiles class that prints 
    # 'Creating Poems!'
    def __init__(self):
        print("Creating Poems!")
    # Implement the __enter__ method. Have the method print 
    # 'Opening poem file'.
    def __enter__(self):
        print("Opening poem file")
    # Create an __exit__ method that prints 'Closing poem file'.
    def __exit__(self, *exc):
        print("Closing poem file")

 # Have the with statement save the invoked class to a variable called manager 
 # and have it print a famous line from the poet Emily Dickinson: 
 # 'Hope is the thing with feathers'.
with PoemFiles() as manager:
    print("Hope is the thing with feathers")