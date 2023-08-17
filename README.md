# CONSOLE

# Description of the Projects

This is a command-line console for managing data using the HBNB (HomeBnB) application's models. 

It provides a command-line interface to create, show, update, and delete instances of different classes, such as BaseModel, State, City, Amenity, Place, Review, and User.

The console operates based on user inputs and responds by interacting with the underlying models package and storage system. 

It allows the user to perform various actions on instances, such as ```creating new instances```, ```displaying their details```, ```updating attributes```, and ```deleting instances```. 

# Installation

To have access to the console:

```git clone https://github.com/bmariga/AirBnB_clone.git```


# How to start the console:

```$ python3 console.py```

or

```$ ./console.py```

# Interactive Mode

```$ ./console.py```

Now you are on interactive mode and the prompt ```hbnb``` will appear:

```(hbnb) create User```

The id of the created user  will appear:

```(hbnb) show User [id]```

All the attributes of the created model will be in your screen.

```(hbnb) User.destroy()```

This command will destroy an instance based on the ID created.

```(hbnh) User.update()```

This command will update an instance based on the ID created. 

```(hbnb) User.count()```

This command will retrieve the number of instances of a class.

```(hnbn) User.show(id)```

This command will retrieve an instance based on the  ID created.

```(hbnb) User.all()```

This command will retrieve all instances of IDs created. 

use:

```(hbnb) help```

To display a list of usable commands.

To exit press ```Ctrl+D``` or type the command ```quit```.


# Testing

To execute unit tests:

```python3 -m unittest discover tests```


