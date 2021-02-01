import tkinter as tk
import keyboard
import time


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Main frame")

        self.editor = tk.Text(self)
        self.editor.pack()
        self.editor.config(font="Courier 12")
        self.editor.focus_set()

        keyboard.add_hotkey('ctrl+alt+s', self.show)
        keyboard.add_hotkey('ctrl+alt+h', self.hide)
        keyboard.add_hotkey('ctrl+c', self.addToList)

    def show(self):
        self.update()
        self.deiconify()

    def hide(self):
        self.update()
        self.withdraw()

    def addToList(self):
        time.sleep(0.2)
        self.editor.window_create(self.editor.index(tk.END),
                                  window=tk.Button(self.editor, text=tk.Tk.clipboard_get(self),
                                                   command=lambda
                                                       localText=tk.Tk.clipboard_get(self): self.insertToClipboard(
                                                       localText)))
        self.editor.insert(tk.END, '\n')

    def insertToClipboard(self, txt):
        tk.Tk.withdraw(self)
        tk.Tk.clipboard_clear(self)
        tk.Tk.clipboard_append(self, txt)
        tk.Tk.update(self)


if __name__ == "__main__":
    App().mainloop()
