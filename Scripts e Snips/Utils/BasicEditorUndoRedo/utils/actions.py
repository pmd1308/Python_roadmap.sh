import hashlib
import tkinter as tk

class ActionManager:
    def __init__(self):
        self.history = []
        self.undone_actions = []
        self.hash_to_text_map = {}

    def record_action(self, text):
        hashed_text = self._hash_text(text)
        if not self.history or hashed_text != self.history[-1]:
            self.history.append(hashed_text)
            self.undone_actions = []
            self.hash_to_text_map[hashed_text] = text

    def undo_action(self, text_widget):
        if self.history:
            current_text_hash = self.history.pop()
            if self.history:
                self.undone_actions.append(current_text_hash)
                self._update_text_widget(text_widget, self.history[-1])
            else:
                self.undone_actions.append(current_text_hash)
                self._update_text_widget(text_widget, "")

    def redo_action(self, text_widget):
        if self.undone_actions:
            self.history.append(self.undone_actions.pop())
            self._update_text_widget(text_widget, self.undone_actions.pop())

    def _update_text_widget(self, text_widget, text_hash):
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, self._hash_to_text(text_hash))

    def _hash_text(self, text):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    def _hash_to_text(self, text_hash):
        return self.hash_to_text_map.get(text_hash, "")