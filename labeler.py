from tkinter import *

class Lbl_Bttn(Frame):
    """Refactored labeling function code for the various labels made in the timer2 script"""
    def __init__(self, master):
        super(Lbl_Bttn, self).__init__(master)
        
    def make_label(self, row_num, col_num, in_text):
        """refactored from create widgets to reduce lines creating labels"""
        self.lbl = Label(self, text = in_text)
        self.lbl.grid(row = row_num, column = col_num, columnspan=3, sticky = W)
        # sticky W means west (left justified)
        return self.lbl
    
    def var_labeler(self, row_num, col_num, in_text, text_var):
        """refactored from create widgets to reduce lines creating labels that can change"""
        text_var.set(in_text)
        self.lbl = Label(self, textvariable = text_var)
        self.lbl.grid(row = row_num, column = col_num, columnspan=3, sticky = W)
        # sticky W means west (left justified)
        return self.lbl
