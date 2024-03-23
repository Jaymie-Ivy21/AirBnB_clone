## AirBnB clone - The console

## Project Description

- This project is our first step towards building our first full web application: the AirBnB clone
- The console folder contains the code for the interpreter
- The model folder contains the Parent class (BaseModel), the subclasses (User, Amenity, State, Place, Review) and the engine folder hosting the Filestorage.
- tests Folder contains all the unittest for the codes.

## Command Interpreter Description

## How to start it

### Interactive Mode
```
$ ./console.py
```

Now you are on interactive mode and you will see the prompt `(hbnb)`
input a command:

```
(hbnb) create User
```
the id of the created model will be visible in the standard output, if you do:

```
(hbnb) show User [id]
```

All the attributes of the created model will be in your screen.

use:

```
(hbnb) help
```
For a list of usable commands, to exit press Ctrl+D or type the command quit.

### Non-Interactive Mode

The console can also be used in non-interactive mode:

```
$ echo "create User" | ./console.py

$ echo "help" | ./console.py
```

The program will create a file called: `file.json` whenever you create a new model, it'll be store in the top folder.


## How to use it

## Launching the console
```
$ ./console.py
(hbnb)
```
## Creating a new object
```
(hbnb) create
** class name missing **
(hbnb) create User
7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
```
## Show an object
```
(hbnb) show User
** instance id missing **
(hbnb) show User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
[User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433468), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433)}
```
## Update an object
```
(hbnb) all
[[BaseModel] (27f7849d-1bb9-4cce-9e1e-3d933b2e882d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215829), 'id': '27f7849d-1bb9-4cce-9e1e-3d933b2e882d', 'created_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215822), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (fc9c4248-2f98-4603-a716-27806a356b78) {'updated_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920273), 'id': 'fc9c4248-2f98-4603-a716-27806a356b78', 'created_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920267), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (27dd53e5-e308-4bed-ac3d-eaa2ab4e941d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796849), 'id': '27dd53e5-e308-4bed-ac3d-eaa2ab4e941d', 'created_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796818)}, [User] (d6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114823), 'id': 'd6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114813), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}, [User] (8ce747cb-ce8e-498f-a493-ce415b8a6e6c) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115617), 'id': '8ce747cb-ce8e-498f-a493-ce415b8a6e6c', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115610), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}, [User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433468), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433)}]
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
** attribute name missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61 Age "42"
(hbnb) all
[[BaseModel] (27f7849d-1bb9-4cce-9e1e-3d933b2e882d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215829), 'id': '27f7849d-1bb9-4cce-9e1e-3d933b2e882d', 'created_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215822), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (fc9c4248-2f98-4603-a716-27806a356b78) {'updated_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920273), 'id': 'fc9c4248-2f98-4603-a716-27806a356b78', 'created_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920267), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (27dd53e5-e308-4bed-ac3d-eaa2ab4e941d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796849), 'id': '27dd53e5-e308-4bed-ac3d-eaa2ab4e941d', 'created_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796818)}, [User] (d6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114823), 'id': 'd6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114813), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}, [User] (8ce747cb-ce8e-498f-a493-ce415b8a6e6c) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115617), 'id': '8ce747cb-ce8e-498f-a493-ce415b8a6e6c', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115610), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}, [User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 5, 57, 527661), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433), 'Age': '42'}]
```
## Destroy an object
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
(hbnb)
```
