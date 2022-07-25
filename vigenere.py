# Vigenere Encryptor
"""Programm wich encrypts and decrypts text files.
"""

import itertools
import string
import tkinter as tk
from tkinter import filedialog, messagebox

class VigenenreCode:
    '''Class representing Vigenenre Logic'''
    def __init__(self):
        self.file = ""
        self.path = ""
        self.unencoded_text = ""
        self.encoded_text = ""
        self.key = ""
        self.procedure = False
        self.charset = [x for x in itertools.chain(
            string.ascii_letters,
            string.digits,
            string.punctuation,
            " "
            )]

    def read_file(self):
        '''Reads text from the choosen file'''
        with open(self.file, 'r', encoding='utf-8') as file:
            for line in file:
                self.unencoded_text += line

    def write_file(self):
        '''Writes text to the choosen file'''
        with open(self.path, 'w+', encoding='utf-8') as file:
            file.write(self.encoded_text)

    def get_index(self, character:str) -> int:
        '''Returns the index of the given character
        Parameters
        ----------
        character : str
            a character to search for
        Retruns
        --------
        int : index of the given character in the list
        '''
        return self.charset.index(character)

    def calc_shift(self, character:str, corresponding_key_char:str) -> str:
        '''
        Takes a character and a corresponding key character, gets the index of the given charset,
        and returns the encoded respectively decrypted character.

        Parameters
        ----------
        character : str
            a character from the text
        corresponding_key_char : str
            a charected from the key

        Returns
        --------
        str : str
            encoded / decored character
        '''
        if character not in self.charset:
            return character
        else:
            char_i = self.get_index(character)
            key_i = self.get_index(corresponding_key_char)
            if self.procedure == 0:
                if (char_i + key_i) > (len(self.charset) - 1):
                    new_i = (char_i + key_i) % len(self.charset)
                    return self.charset[new_i]
                else:
                    return self.charset[char_i + key_i]
            elif self.procedure == 1:
                if (char_i - key_i) < 0:
                    rest = char_i - key_i
                    new_i = len(self.charset) + rest
                    return self.charset[new_i]
                else:
                    return self.charset[char_i - key_i]

    def code(self):
        '''
        Encodes respectively decodes the text
        '''
        t_lenght = len(self.unencoded_text)
        coding_list = [char for char in self.unencoded_text]

        l_key = (self.key * t_lenght)[:t_lenght]
        output = ""
        for idx, char in enumerate(coding_list):
            new_char = self.calc_shift(char, l_key[idx])
            output += new_char
        return output

class VigenereApp(tk.Tk):
    '''
    Class constructor for Vigenere GUI
    '''
    def __init__(self):
        super().__init__()
        self.title("Vigenere Encryptor")
        self.geometry("600x390")
        self.resizable(False, False)
        self._initialize()

    def _initialize(self):
        display_frame = tk.Frame(self)
        display_frame.pack(fill=tk.X, padx=5, pady=5)

        # Step 1: Select file
        file_frame = tk.LabelFrame(display_frame, text='Step 1: Select file', padx=5, pady=5)
        file_frame.pack(fill=tk.X, padx=5, pady=5)
        file_show_label = tk.Label(file_frame, width=65)
        file_show_label.configure(bg='lightgray', relief=tk.SUNKEN, pady=5, padx=5, anchor=tk.W)
        file_show_label.grid(row=0, column=0, sticky='nw',)

        def _get_file():
            choosen_file = filedialog.askopenfilename(filetypes=[('Text-Files', ".txt")])
            file_show_label.configure(text=choosen_file)

        file_label_button = tk.Button(file_frame, text="Select file", command=_get_file, width=10,)
        file_label_button.grid(row=0, column=1, sticky='nw', padx=(10,0))

        #Step 2: Choose Keyword
        keyword_frame = tk.LabelFrame(display_frame, text="Step 2: Enter Keyword:", padx=5, pady=5)
        keyword_frame.pack(fill=tk.X, padx=5, pady=5)
        keyword_text = tk.Text(keyword_frame, padx=5, pady=5, height=1, width=20)
        keyword_text.pack(fill=tk.X, padx=5, pady=5)

        #Step 3: Choose procedure
        variant_frame = tk.LabelFrame(
            display_frame,
            text="Step 3: Select Procedure:",
            padx=5,
            pady=5,
            )
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


        # Step 4: Choose Path
        dir_frame = tk.LabelFrame(
            display_frame,
            text="Step 4: Select Path & Filename",
            padx=5,
            pady=5
            )
        dir_frame.pack(fill=tk.X, padx=5, pady=5)
        dir_show_label = tk.Label(dir_frame, width=65)
        dir_show_label.configure(bg='lightgray', relief=tk.SUNKEN, pady=5, padx=5, anchor=tk.W)
        dir_show_label.grid(row=0, column=0, sticky='nw',)

        def _choose_dir():
            selected_dir = filedialog.asksaveasfilename(filetypes=[("Text-Files", "*.txt")])
            selected_dir = selected_dir if ".txt" in selected_dir else selected_dir + ".txt"
            dir_show_label.configure(text=selected_dir)

        dir_button = tk.Button(dir_frame, text="Save as", command=_choose_dir, width=10)
        dir_button.grid(row=0, column=1, sticky='nw', padx=(10,0))

        # Step 5: Run
        def run_btn():
            enc = VigenenreCode()
            enc.procedure = p_var.get()
            enc.file = file_show_label.cget("text")
            if not enc.file:
                return messagebox.showerror(
                    "Error: No file specified",
                    "Please provide a text file that should be encrypted respectively decrypted!"
                    )
            enc.key = keyword_text.get("1.0", tk.END).strip()
            print("DEBURG: ", enc.key)
            if not enc.key:
                return messagebox.showerror(
                    "Error: No key specified",
                    "Key has to be specified before running the command"
                    )
            mistake_characters = [y for y in enc.key if y not in enc.charset]
            if mistake_characters:
                return messagebox.showerror(
                    "Error: Key mismatch charset",
                    "The Keyword uses invalid characters."
                )
            enc.path = dir_show_label.cget("text")
            if not enc.path:
                return messagebox.showerror(
                    "Error: No path specified",
                    "Please provide a path and filename"
                    )

            enc.read_file()
            enc.encoded_text = enc.code()
            enc.write_file()

        run_frame = tk.LabelFrame(
            display_frame,
            text="Step5: Run Encrption / Decryption",
            padx=5,
            pady=5
        )
        run_frame.pack(fill=tk.BOTH)
        run_button = tk.Button(run_frame, text="Encrypt\n-------\nDecrypt", command=run_btn)
        run_button.pack(fill=tk.BOTH, padx=5, pady=5)


def main():
    '''Initial Function'''
    vcrypt = VigenereApp()
    vcrypt.mainloop()

if __name__ == "__main__":
    main()
