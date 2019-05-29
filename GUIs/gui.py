from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import sys
sys.path.append('.')
sys.path.append('../')

import tkinter as tk
from tkinter import ttk 
from tkinter import IntVar
from tkinter import *

from PIL import ImageTk
from PIL import Image


import Helpers.IO as io
import random
import emoji
import testquestions

import time
from Grade_K.TestCases import TestCases
import Helpers.Control as CTR


class KidsMath(Frame):
    def __init__(self, isapp=True, name='kidsmath'):
        Frame.__init__(self, name=name, borderwidth=5, height=150, width=200)
        self.ansPanel = None
        self.answers = [StringVar(), StringVar(), StringVar(), StringVar()]
        self.questText = StringVar()
        self.hintText = StringVar()
        self.expectedAns = StringVar()
        self.v = IntVar()
        self.pack(expand=Y, fill=BOTH)
        self.master.title('KidsMath')
        self.isapp = isapp

        self.stat = {'correctCases' : 0, 'wrongCases' : 0}

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
        self.nextval = tk.IntVar()
        photo=PhotoImage(file="joypixels/NextSymbol.gif")
        self.cross=PhotoImage(file="joypixels/crossmark.gif")
        self.check=PhotoImage(file="joypixels/checkmark.gif")
        self.nextbutton = tk.Button(self.questionPanel, image = photo, command=lambda: self.nextval.set(1))
        #self.nextbutton = tk.Button(self.ansPanel, image = photo, command=lambda: self.nextval.set(1))
        for t in self.selectedTests:
            self.checkedAns.config(text = '')
            self.checkedAns.pack_forget()
            #getattr(self.testcases, t)()
            self.displayTest(t)
            #self.nextbutton.wait_variable(self.nextval)
        for rb in self.ansButtons:
            rb.pack_forget()
        self.B1.pack_forget()
        self.nextbutton.pack_forget()
        #self.checkedAns.config(text = 'All tests are done.')
        self.checkedAns.pack_forget()
        self._update_question('')
        Label(self.ansPanel, text='All tests are done.\nCorrect:{}\nWrong:{}\nScore:{}'.format(self.stat['correctCases'], self.stat['wrongCases'], (self.stat['correctCases']/(self.stat['correctCases']+self.stat['wrongCases'])*100))).pack() 

    def checkAns(self, a):
        if self.answers[self.v.get()].get() == a:
            t = "Correct!"
            self.checkedAns.config(image = self.check)
            self.stat['correctCases'] += 1
        else:
            t = "Wrong!"
            self.checkedAns.config(image = self.cross)
            self.stat['wrongCases'] += 1
        #self.checkedAns.config(text = t)
        self.checkedAns.pack(anchor = CENTER)
        self.nextbutton.pack(anchor = CENTER)


    def displayTest(self, t):
        paras = testquestions.testcases[t]
        for p in paras:
            self._update_question(p['questiontext'])
            self.expectedAns.set(p['expectedAns'])
            self._update_answer(p['ansList'])
            self.checkedAns.pack_forget()
            objs = []
            if 'pictures' in p:
                plist = p['pictures']
                pics = {}
                rows = len(plist)
                for i in range(rows):
                    for j in range(len(plist[i])):
                        if plist[i][j] not in pics:
                            pics[plist[i][j]] = PhotoImage(file='joypixels/' + plist[i][j] + '.gif')
                        lb = Label(self.pictureFrame, image = pics[plist[i][j]])
                        objs.append(lb)
                        lb.grid(row=i, column=j, sticky=W) 
            self.nextbutton.wait_variable(self.nextval)
            for o in objs:
                o.grid_forget()

    def buildRandomTests(self, r):
        RandomMethodList = []
        tests = self.alltestcases
        for i in range(r):
            secure_random = random.SystemRandom()
            m = secure_random.choice(tests)
            RandomMethodList.append(m)
            tests.remove(m)
        self.selectedTests = RandomMethodList


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

        randomList = [0, 5, 10, 15, 20]
        self.radioButtons = []
        for i in range(len(randomList)):
            rb = Radiobutton(self, text = 'Randomly Select {} Tests'.format(randomList[i]), variable = self.v, value = i, font=("Courier", 13))
            rb.pack(padx = 50, anchor = W)
            self.radioButtons.append(rb)

        checkvars = [tk.IntVar() for i in range(len(self.alltestcases))]
        allcheckbuttons = []
        for i in range(len(self.alltestcases)):
            cb = Checkbutton(self, text = self.alltestcases[i], variable=checkvars[i], onvalue=1, offvalue=0)
            cb.pack(padx = 55, anchor = W)
            allcheckbuttons.append(cb)


        B0.wait_variable(var)
        B0.pack_forget()

        RandomMethodList = []
        tests = self.alltestcases
        for i in range(randomList[self.v.get()]):
            secure_random = random.SystemRandom()
            m = secure_random.choice(tests)
            RandomMethodList.append(m)
            tests.remove(m)
        self.selectedTests = RandomMethodList

        for i in range(len(checkvars)):
            if checkvars[i].get():
                self.selectedTests.append(self.alltestcases[i]) 

        for rb in self.radioButtons:
            rb.pack_forget()

        for cb in allcheckbuttons:
            cb.pack_forget()

    def _create_widgets(self):
        self._create_question_panel()
        self._create_answer_panel()
 
    def _create_question_panel(self):
        self.questionPanel = Frame(self, name='question', width=100, height=100)
        self.questionPanel.pack(side=LEFT, fill=BOTH, expand=Y)
 
        # create the notebook
        nb = ttk.Notebook(self.questionPanel, name='notebook')
  
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
        self.pictureFrame = Frame(self.questionPanel, name='picture')
        self.pictureFrame.pack()
        self._create_answer_panel()


    def helloCallBack(self):
        return

    def _create_answer_panel(self):
        self.ansPanel = Frame(self, name='answer')
        self.ansPanel.pack(side=LEFT, fill=BOTH, expand=Y)
        self.B1 = Button(self.ansPanel, text = "Check the answer", font=("Courier", 13), command = lambda: self.checkAns(self.expectedAns.get()))
        self.B1.pack(side=TOP, padx=50, pady=30)
        self._create_answer_button()
        self.checkedAns = Label(self.ansPanel, wraplength='4i', justify=LEFT, anchor=N, text=None)

    def _create_answer_button(self):
        for i in range(len(self.answers)):
            rb = Radiobutton(self.ansPanel, textvariable = self.answers[i], variable = self.v, value = i, font=("Courier", 12))
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
