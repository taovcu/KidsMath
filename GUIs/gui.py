import sys
sys.path.append('.')
sys.path.append('../')

import tkinter as tk
from tkinter import ttk 
from tkinter import IntVar
from tkinter import *

import Helpers.IO as io
import random
import emoji

import time
from Grade_K.TestCases import TestCases
import Helpers.Control as CTR

class KidsMath(Frame):
    def __init__(self, isapp=True, name='kidsmath'):
        Frame.__init__(self, name=name)
        self.ansPanel = None
        self.answers = [StringVar(), StringVar(), StringVar(), StringVar()]
        self.questText = StringVar()
        self.hintText = StringVar()

        self.v = IntVar()
        self.pack(expand=Y, fill=BOTH)
        self.master.title('KidsMath')
        self.isapp = isapp


        # user choose grade
        self.radioButtons = []
        self.ansButtons = []
        var = tk.IntVar()
        B0 = Button(self, text = "Select Grade", command=lambda: var.set(1), font=("Courier", 13))
        B0.pack(side=TOP, padx=50, pady=30)
        gradeList = [str(i) for i in range(1,9)]
        self.gradelist = ['k'] + gradeList
        for i in range(len(self.gradelist)):
            rb = Radiobutton(self, text = self.gradelist[i], variable = self.v, value = i)
            rb.pack()
            self.radioButtons.append(rb)

        B0.wait_variable(var)
        B0.pack_forget()
        for rb in self.radioButtons:
            rb.pack_forget()

        self.buildTestCases()
        self._create_widgets()
        self.runTests()

    def runTests(self):
        for t in self.selectedTests:
            #getattr(self.testcases, t)()
            print(t)
            self.displayTest(t)


    def displayTest(self, t):
        if t == 'AddObjectTestCases':
            self._update_question('Bob has 3 pears, Joy has 4 pears, how many pears do they have in total?')
            self._update_answer(['1', '2', '4', '7'])

    def buildTestCases(self):
        self.testcases = TestCases(self.gradelist[self.v.get()])
        object_methods = [method_name for method_name in dir(self.testcases)
                      if callable(getattr(self.testcases, method_name))]
        object_methods = CTR.RemoveSysMethods(object_methods)
        self.alltestcases = object_methods
        self.selectedTests = []

        var = tk.IntVar()
        B0 = Button(self, text = 'There are totally {} test cases implemented. Please select tests'.format(len(self.alltestcases)), command=lambda: var.set(1), font=("Courier", 13))
        B0.pack(side=TOP, padx=50, pady=30)

        checkvars = [tk.IntVar() for i in range(len(self.alltestcases))]
        allcheckbuttons = []
        for i in range(len(self.alltestcases)):
            cb = Checkbutton(self, text = self.alltestcases[i], variable=checkvars[i], onvalue=1, offvalue=0)
            cb.pack(padx = 20, anchor = W)
            allcheckbuttons.append(cb)
        B0.wait_variable(var)
        B0.pack_forget()
        for i in range(len(checkvars)):
            if checkvars[i].get():
                self.selectedTests.append(self.alltestcases[i]) 

        for cb in allcheckbuttons:
            cb.pack_forget()

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
        self.questText.set('Question Description')
        self._create_tab(nb, 'quest', self.questText, 'Question Description')
        self.hintText.set('Hint')
        self._create_tab(nb, 'hint', self.hintText, 'Hint')
        time.sleep(5)
        self._create_answer_panel()


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
            rb = Radiobutton(self.ansPanel, textvariable = self.answers[i], variable = self.v, value = i, command = self.helloCallBack, font=("Courier", 12))
            rb.pack(anchor = CENTER)
            self.ansButtons.append(rb)

    def _update_question(self, q):
        self.questText.set(q)

    def _update_hint(self, h):
        self.hintText.set(h)

    def _update_answer(self, ansList):
        for i in range(len(ansList)):
            self.answers[i].set(ansList[i])
 
    def _create_tab(self, nb, n, m, t):
        # frame to hold contentx
        #frame = Frame(nb, name='descrip')
        frame = Frame(nb, name=n)
 
        lbl = Label(frame, wraplength='4i', justify=LEFT, anchor=N, textvariable=m)
        # position and set resize behaviour
        lbl.grid(row=0, column=0, columnspan=2, sticky='new', pady=5)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0,1), weight=1, uniform=1)
 
        # add to notebook (underline = index for short-cut character)
        #nb.add(frame, text='Question', underline=0, padding=2)
        nb.add(frame, text=t, underline=0, padding=2)
 
 
if __name__ == '__main__':
    KidsMath().mainloop()
