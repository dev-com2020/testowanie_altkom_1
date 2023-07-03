import unittest
import threading
import queue

from src.todo.app import TODOApp


class TestTODOAcceptance(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()

        self.fake_output = lambda txt: self.outputs.put(txt)
        self.fake_input = lambda: self.inputs.get()

        self.get_output = lambda: self.outputs.get(timeout=1)
        self.send_input = lambda cmd: self.inputs.put(cmd)

    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))
        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "\n"
            "\n"
            "> "
        ))
        self.send_input('add Kupić mleko')
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. Kupić mleko\n"
            "\n"
            "> "
        ))

        self.send_input('add Kupić jajka')
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. Kupić mleko\n"
            "2. Kupić jajka\n"
            "\n"
            "> "
        ))

        self.send_input('del 1')
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. Kupić jajka\n"
            "\n"
            "> "
        ))

        self.send_input('quit')
        app_thread.join(timeout=1)
        self.assertEqual(self.get_output(), "Żegnaj!\n")
