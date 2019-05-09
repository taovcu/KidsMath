import sys
sys.path.append('../')

import tkinter as tk
from tkinter import ttk 
from tkinter import IntVar
from tkinter import *

import Helpers.IO as io
import random
import emoji

from Grade_K.TestCases import TestCases
import Helpers.Control as CTR


class KidsMath(Frame):
    def __init__(self, isapp=True, name='kidsmath'):
        Frame.__init__(self, name=name)
        self.ansPanel = None
        self.answers = ["Answer0", "Answer1", "Answer2", "Answer3"]

        self.v = IntVar()
        self.pack(expand=Y, fill=BOTH)
        self.master.title('KidsMath')
        self.isapp = isapp


        # user choose grade
        self.radioButtons = []
        var = tk.IntVar()
        B0 = Button(self, text = "Select Grade", command=lambda: var.set(1), font=("Courier", 13))
        B0.pack(side=TOP, padx=50, pady=30)
        gradeList = [str(i) for i in range(1,9)]
        gradeList = ['k'] + gradeList
        for i in range(len(gradeList)):
            rb = Radiobutton(self, text = gradeList[i], variable = self.v, value = i)
            rb.pack()
            self.radioButtons.append(rb)

        B0.wait_variable(var)
        B0.pack_forget()
        for rb in self.radioButtons:
            rb.pack_forget()

        self._create_widgets()

    def chooseGrade(self):
        print(self.v.get())

    def _create_widgets(self):
        self._create_question_panel()
        self._create_answer_panel()
 
    def _create_question_panel(self):
        questionPanel = Frame(self, name='question')
        questionPanel.pack(side=LEFT, fill=BOTH, expand=Y)
 
        # create the notebook
        nb = ttk.Notebook(questionPanel, name='notebook')
  
        # extend bindings to top level window allowing
        #   CTRL+TAB - cycles thru tabs
        #   SHIFT+CTRL+TAB - previous tab
        #   ALT+K - select tab using mnemonic (K = underlined letter)
        nb.enable_traversal()
 
        nb.pack(fill=BOTH, expand=Y, padx=2, pady=3)
        #self._create_tab(nb, 'quest', 'Question description:', 'Question Description')
        #self._create_tab(nb, 'hint', 'Hint:', 'Hint')
        self._create_tab(nb, 'quest', '', 'Question Description')
        self._create_tab(nb, 'hint', '', 'Hint')
        self._create_answer_panel()

    def _update_question(self):
        return

    def _update_hint(self):
        return

    def helloCallBack(self):
        return

    def _create_answer_panel(self):
        self.ansPanel = Frame(self, name='answer')
        self.ansPanel.pack(side=LEFT, fill=BOTH, expand=Y)
        B1 = Button(self.ansPanel, text = "Check the answer", font=("Courier", 13))
        B1.pack(side=TOP, padx=50, pady=30)
        self._create_answer_button()

    def _create_answer_button(self):
        for i in range(len(self.answers)):
            Radiobutton(self.ansPanel, text = self.answers[i], variable = self.v, value = i,
                        command = self.helloCallBack, font=("Courier", 12)).pack(anchor = CENTER)
 
    def _update_answer(self):
        return

 
    def _create_tab(self, nb, n, m, t):
        # frame to hold contentx
        #frame = Frame(nb, name='descrip')
        frame = Frame(nb, name=n)
 
        # widgets to be displayed on 'Description' tab
        msg = [m]
 
        lbl = Label(frame, wraplength='4i', justify=LEFT, anchor=N, text=''.join(msg))
        # position and set resize behaviour
        lbl.grid(row=0, column=0, columnspan=2, sticky='new', pady=5)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0,1), weight=1, uniform=1)
 
        # add to notebook (underline = index for short-cut character)
        #nb.add(frame, text='Question', underline=0, padding=2)
        nb.add(frame, text=t, underline=0, padding=2)
 
 
if __name__ == '__main__':
    KidsMath().mainloop()
