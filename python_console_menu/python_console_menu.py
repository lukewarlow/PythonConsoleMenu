from abc import ABC, abstractclassmethod

class OperationError(Exception):
    def __init__(self):
        super().__init__("Invalid operation")


class AbstractMenu(ABC):
    def __init__(self, title: str):
        self.title = title
        self.menu_items = []
        self.initialise()

    @abstractclassmethod
    def initialise(self):
        return

    def update_menu_itmes(self):
        return

    def display(self):
        repeat = True
        while repeat:
            self.update_menu_itmes()
            print()
            print(self.title)
            for i in range(0, len(self.menu_items)):
                if self.menu_items[i].isVisible:
                    print(str(i) + ". " + self.menu_items[i].description)

            inp = input("Select Option: ")
            try:
                menu_item = self.menu_items[int(inp)]
                if menu_item.isVisible:
                    repeat = menu_item.run()
                else:
                    raise OperationError()
            except ValueError:
                print("Invalid option, you need to enter a number.", inp)
                repeat = True
            except IndexError:
                print("Invalid option. Option {0} doesn't exist.".format(inp))
                repeat = True
            except OperationError:
                print("Invalid option. Option at {0} is hidden.".format(inp))
                repeat = True

    def add_menu_item(self, menu_item):
        if not self.menu_items.__contains__(menu_item):
            self.menu_items.append(menu_item)
        else:
            raise ValueError("Menu item with id {0} already exists!.".format(menu_item.id))

    def add_hidden_menu_item(self, menu_item):
        self.add_menu_item(menu_item.hide())

    def show_menu_item(self, item_id):
        try:
            menu_item = MenuItem(item_id)
            index = self.menu_items.index(menu_item)
            self.menu_items[index].show()
        except ValueError:
            print("Error showing menu item. Menu item with ID {0} hasn't been added to this menu.".format(item_id))

    def hide_menu_item(self, item_id):
        try:
            menu_item = MenuItem(item_id)
            index = self.menu_items.index(menu_item)
            self.menu_items[index].hide()
        except ValueError:
            print("Error hiding menu item. Menu item with ID {0} hasn't been added to this menu.".format(item_id))


class MenuItem:
    def __init__(self, id: int, description: str = "", action: callable(None) = None, menu = None):
        self.id = id
        self.description = description
        self.action = action
        self.menu = menu
        self.isExitOption = False
        self.isVisible = True

    def hide(self):
        self.isVisible = False
        return self

    def show(self):
        self.isVisible = True
        return self

    def set_as_exit_option(self):
        self.isExitOption = True
        return self

    def run(self):
        if self.action is not None:
            self.action()
        elif self.menu is not None:
            self.menu.display()

        return not self.isExitOption

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
