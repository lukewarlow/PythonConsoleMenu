from python_console_menu import AbstractMenu, MenuItem

class TestSubMenu(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the test sub menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "Exit current menu").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Test sub menu item", lambda: print("Test sub menu item selected")))


class TestMenu(AbstractMenu):
    show_hidden_menu = False

    def __init__(self):
        super().__init__("Welcome to the test menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "Exit menu").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Test sub menu", menu=TestSubMenu()))
        self.add_menu_item(MenuItem(2, "Show hidden menu item", lambda: self.__should_show_hidden_menu__()))
        self.add_hidden_menu_item(MenuItem(3, "Hidden menu item", lambda: print("I was a hidden menu item")))

    def __should_show_hidden_menu__(self):
        print("Showing hidden menu item")
        self.show_hidden_menu = True

    def update_menu_itmes(self):
        if self.show_hidden_menu:
            self.show_menu_item(3)


testMenu = TestMenu()
testMenu.display()
