class HideFileCommand:
    def __init__(self):
        self._hidden_files = []

    def execute(self, filename):
        print(f"hidding {filename}")
        self._hidden_files.append(filename)

    def undo(self):
        filename = self._hidden_files.pop()
        print(f"un-hiding {filename}")


class DeleteFileCommand:
    def __init__(self):
        self._deleted_files = []

    def execute(self, filename):
        print(f"deleting {filename}")
        self._deleted_files.append(filename)

    def undo(self) -> None:
        filename = self._deleted_files.pop()
        print(f"restoring {filename}")


class MenuItem:
    def __init__(self, command):
        self._command = command

    def on_do_press(self, filename):
        self._command.execute(filename)

    def un_do_press(self):
        self._command.undo()

menu_command = MenuItem(DeleteFileCommand())
menu_command.on_do_press("sda")
menu_command.on_do_press("dsadsa")
menu_command.un_do_press()

test_file_name = 'test-file'
menu_command2 = MenuItem(HideFileCommand())
menu_command2.on_do_press(test_file_name)
menu_command2.on_do_press()