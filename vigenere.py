# Vigenere Encryptor
"""Programm wich encrypts and decrypts text files.
"""

import tkinter as tk
from  tkinter import filedialog


class VigenereApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vigenere Encryptor")
        self.geometry("600x400")
        self.resizable(False, False)
        self._initialize()

    def _initialize(self):
        display_frame = tk.Frame(self)
        display_frame.pack(fill=tk.X, padx=5, pady=5)

        file_frame = tk.LabelFrame(display_frame, text='Select file', padx=5, pady=5)
        file_frame.pack(fill=tk.X, padx=5, pady=5)
        file_show_label = tk.Label(file_frame, width=65)
        file_show_label.configure(bg='lightgray', relief=tk.SUNKEN, pady=5, padx=5, anchor=tk.W)
        file_show_label.grid(row=0, column=0, sticky='nw',)

        def _get_file():
            choosen_file = filedialog.askopenfilename()
            file_show_label.configure(text=choosen_file)


        file_label_button = tk.Button(file_frame, text="Choose file", command=_get_file)
        file_label_button.grid(row=0, column=1, sticky='nw', padx=(10,0))

        # Choose procedure
        variant_frame = tk.LabelFrame(display_frame, text="select procedure:", padx=5, pady=5)
        variant_frame.pack(fill=tk.X, padx=5, pady=5)
        procedures = [('Encrypt', 0), ('Decrypt', 1)]
        p_var = tk.IntVar()
        for txt, val in procedures:
            tk.Radiobutton(
                variant_frame,
                text=txt,
                padx=20,
                variable=p_var,
                value=val
            ).pack(anchor=tk.W, side=tk.LEFT)
        keyword_frame = tk.LabelFrame(variant_frame, text="keyword:", padx=5, pady=5)
        keyword_frame.pack(side=tk.RIGHT)
        keyword_text = tk.Text(keyword_frame, padx=5, pady=5, height=1, width=20)
        keyword_text.pack()

        # Run Buttom
        def run_btn():
            procedure_value = p_var.get()
            print(procedure_value)
        # TODO: Needs run function!
        run_button = tk.Button(display_frame, text="RUN", command=run_btn)
        run_button.pack(fill=tk.X, padx=5, pady=(10, 5))

class VigenenreCode:
    def __init__(self):
        super().__init__()
        self.file = ""
        self.path = ""
        self.key = ""

def main():
    '''Initial Function'''
    vcrypt = VigenereApp()
    vcrypt.mainloop()

if __name__ == "__main__":
    main()
