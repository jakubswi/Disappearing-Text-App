from tkinter import *
from tkinter.scrolledtext import ScrolledText

class DisappearingTextApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Disappearing Text App")
        self.window.geometry("1200x600")
        self.label = Label(self.window, text="If you stop writing the text will disappear.")
        self.label.pack()
        self.entry = ScrolledText(self.window, wrap=WORD, width=180, height=60)
        self.entry.pack()
        self.old_text = ''
        self.timer = None

    def check_input(self, event=None):
        new_text = self.entry.get("1.0", END).strip()
        if new_text != self.old_text:
            self.old_text = new_text
            if self.timer:
                self.window.after_cancel(self.timer)
            self.timer = self.window.after(5000, self.clear_text)
        else:
            if self.timer:
                self.window.after_cancel(self.timer)

    def clear_text(self):
        self.entry.delete("1.0", END)
        self.old_text = ''
        self.timer = None

if __name__ == "__main__":
    window = Tk()
    app = DisappearingTextApp(window)
    app.entry.bind("<KeyRelease>", app.check_input)
    window.mainloop()
