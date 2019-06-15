# Python Console Menu
![license](https://img.shields.io/hexpm/l/plug.svg)

This library provides a way to quickly create the menu for your Python console app.

##  Overview

### Classes

#### AbstractMenu
This is the abstract class you need to extend in your menus.
Its constructor takes in a title which is displayed at the top of the menu. This should be called from your implementation's constructor. Like so:
```pythonstub
class MenuImplementation(AbstractMenu):
    def __init__(self):
        super().__init__("Menu Title")
```
##### Methods
- `initialise()` this needs overriding in your implementations and is where you add the items to the menu.
- `display()` this starts this menu. This only needs to be called on the root menu in your system, as all sub-menus are handled by this library.
- `add_menu_item(MenuItem(id, description, subMenu or action))` this adds an item to the menu. 
- `add_hidden_menu_item(new MenuItem(id, description, subMenu or action))` this is a helper method that adds a menu item, which is then hidden.
- `update_menu_items()` this can be overridden per menu to update items based on changes to your application, such as showing hidden menu items if they're now needed.
- `show_menu_item(id)` this can be used to show hidden menu items, most commonly in the method above. This uses the unique id given to the menu item.
- `hide_menu_item(id)` this can be used to hide menu items.

#### MenuItem
This is the class used to define items for the menus in your system. 
It has two constructors one for if the item is a sub menu and another for if its an action. 
These should be called like this: `MenuItem(id, description, subMenu or action)`
##### Methods
- `hide()` which is used on menu items, to hide them from the list.
- `show()` which is used on hidden menu items, to show them in the list.
- `set_as_exit_option()` which is used to set menu items as the exit option for a menu, either going to the parent menu, or exiting the application.

## Example
#### Menu initialisation
```pythonstub
mainMenu = MainMenu()
mainMenu.display()
```
#### Main Menu Class
```pythonstub
class MainMenu(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the main menu")
    
    def initialise(self):
        self.add_menu_item(MenuItem(100, "Exit menu").set_as_exit_option())
        self.add_menu_item(MenuItem(101, "Print Hello World", lambda: print("Hello World!")))
```

#### Output
```text
Welcome to the main menu
0. Exit menu
1. Print Hello World
Select option: 1
Hello World!

Welcome to the main menu
0. Exit menu
1. Print Hello World
Select option: 0

Process finished with exit code 0
```

Look in demo/menu_demo.py for a better example implementation of the library.
