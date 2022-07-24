# Vigenere Encryptor
"""Programm wich encrypts and decrypts text files.
"""

import itertools
import string
import tkinter as tk
from  tkinter import filedialog


class VigenenreCode:
    def __init__(self):
        self.file = ""
        self.path = ""
        self.unencoded_text = ""
        self.encoded_text = ""
        self.key = ""
        self.procedure = False
        self.charset = [x for x in itertools.chain(string.ascii_letters, string.digits)]

    def read_file(self):
        '''Reads text from the choosen file'''
        with open(self.file, 'r', encoding='utf-8') as file:
            for line in file:
                self.unencoded_text += line

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
            if self.procedure is False:
                if (char_i + key_i) > (len(self.charset) - 1):
                    new_i = (char_i + key_i) % len(self.charset)
                    return self.charset[new_i]
                else:
                    return self.charset[char_i + key_i]
            elif self.procedure is True:
                if (char_i - key_i) < 0:
                    rest = char_i - key_i
                    new_i = len(self.charset) + rest
                    return self.charset[new_i]
                else:
                    return self.charset[char_i - key_i]

    def code(self):
        if self.procedure is False:
            t_lenght = len(self.unencoded_text)
            coding_list = [char for char in self.unencoded_text]
        elif self.procedure is True:
            t_lenght = len(self.encoded_text)
            coding_list = [char for char in self.encoded_text]

        l_key = (self.key * t_lenght)[:t_lenght]
        print('DBUG:', l_key)
        output = ""
        for idx, char in enumerate(coding_list):
            output += self.calc_shift(char, l_key[idx])
        return output

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


def main():
    '''Initial Function'''
    #vcrypt = VigenereApp()
    #vcrypt.mainloop()

if __name__ == "__main__":
    main()
