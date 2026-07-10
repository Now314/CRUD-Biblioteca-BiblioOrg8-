from typing import Callable

from PySide6.QtWidgets import QMainWindow


class WindowManager:
    def __init__(self):
        self.current_window: QMainWindow | None = None
        self.history: list[QMainWindow] = []

    def start(self, controller: Callable[..., QMainWindow]) -> None:
        self.current_window = controller(self)

        if self.current_window is not None:
            self.current_window.show()

    def show(self, controller: Callable[..., QMainWindow]) -> None:

        previous = self.current_window

        new_window = controller(self)
        new_window.show()

        if previous is not None:
            self.history.append(previous)
            previous.hide()

        self.current_window = new_window

    def back(self) -> None:

        if not self.history:
            return

        previous = self.history.pop()

        previous.show()

        if self.current_window is not None:
            self.current_window.hide()

        self.current_window = previous

    def send_data(self, controller, data):
        if self.current_window is not None:
            self.history.append(self.current_window)

        new_window = controller(self, data)
        new_window.show()

        if self.current_window is not None:
            self.current_window.hide()

        self.current_window = new_window

    def clear_history(self) -> None:
        self.history.clear()
