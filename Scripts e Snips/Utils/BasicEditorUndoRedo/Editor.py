'''
    This script implements a simple text editor using Tkinter, featuring
    undo and redo functionality to manage text stage changes efficiently.
    ---------------------------------------------------------------------
    The script utilizes an ActionManager class to record, undo and redo 
    text modifications, ensuring a user-friendly text editing experience.
    Each text stage is hashed for efficient comparison and stored with
    its corresponding text content for retrieval.
    ---------------------------------------------------------------------
    With the ability to handle text state changes, this editor is suitable 
    for various applications requiring basic text manipulation, such as
    note-taking, text editing, and document management.
    ---------------------------------------------------------------------
    The use of hashing and state managment ensures optimal performance, 
    while Tkinter provides a straightforward graphical user interface.
    ---------------------------------------------------------------------
    Concepts:
    - GUI Development
    - Tkinter
    - State Management
    - Hashing
    - Undo and Redo
'''

import tkinter as tk
from utils.actions import ActionManager

class TextEditorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        
        self.text = tk.Text(self.root, height=10, width=40)
        self.text.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.undo_button = tk.Button(self.button_frame, text="Undo", command=self.undo_action)
        self.undo_button.pack(side=tk.LEFT)

        self.redo_button = tk.Button(self.button_frame, text="Redo", command=self.redo_action)
        self.redo_button.pack(side=tk.LEFT)

        self.action_manager = ActionManager()

        self.text.bind("<KeyRelease", self.delayed_record_action)

        self.root.bind("<Control-z>", lambda event: self.undo_action())
        self.root.bind("<Control-Z>", lambda event: self.undo_action())
        self.root.bind("<Control-y>", lambda event: self.redo_action())
        self.root.bind("<Control-Y>", lambda event: self.redo_action())

        # Delaying to avoid recording too many states
        self._record_action_id = None

    def delayed_record_action(self, event=None):
        if self._record_action_id:
            self.root.after_cancel(self._record_action_id)
        self._record_action_id = self.root.after(100, self.record_action)

    def record_action(self):
        current_text = self.text.get(1.0, tk.END)
        self.action_manager.record_action(current_text)
        self._record_action_id = None

    def undo_action(self):
        self.action_manager.undo_action(self.text)

    def redo_action(self):
        self.action_manager.redo_action(self.text)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditorGUI(root)
    root.mainloop()