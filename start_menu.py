import tkinter as Tk
import Edit


class Main_window:
    BUTTONS = []
    NAMES = ["NEW", "OPEN DB"]
    Start_win = Tk.Tk()
    FRAME = Tk.Frame(master=Start_win)

    def delete_frame(self):
        self.FRAME.destroy()
        pass

    def handle_click_open(self, event):
        print('open window')
        self.delete_frame()
        Edit.window_edit_init(self.Start_win)
        print('g')
        pass

    def handle_click_new(self, event):
        print('open new')
        self.delete_frame()
        pass

    def __init__(self):
        self.Start_win.title('ultimate friends db')
        self.Start_win.geometry('400x400')

        for i in range(len(self.NAMES)):
            self.BUTTONS.append([self.NAMES[i], Tk.Button(master=self.FRAME, text=self.NAMES[i], width=25, height= 10)])
            (self.BUTTONS[i][1]).grid(row = i + 1)
            if self.NAMES[i] == 'NEW':
                self.BUTTONS[i][1].bind("<Button-1>", self.handle_click_open)
            else:
                self.BUTTONS[i][1].bind("<Button-1>", self.handle_click_new)

        self.FRAME.pack()
        self.Start_win.mainloop()



