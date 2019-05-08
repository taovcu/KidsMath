import tkinter as tk
from tkinter import ttk 
from tkinter import IntVar
from tkinter import *



class NotebookDemo(Frame):
    def __init__(self, isapp=True, name='notebookdemo'):
        Frame.__init__(self, name=name)
        self.ansPanel = None
        self.answers = ["Answer0", "Answer1", "Answer2", "Answer3"]

        self.v = IntVar()
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Notebook Demo')
        self.isapp = isapp
        self._create_widgets()

    def _create_widgets(self):
        self._create_demo_panel()
        self._create_answer_panel()
 
    def _create_demo_panel(self):
        demoPanel = Frame(self, name='demo')
        demoPanel.pack(side=LEFT, fill=BOTH, expand=Y)
 
        # create the notebook
        nb = ttk.Notebook(demoPanel, name='notebook')
  
        # extend bindings to top level window allowing
        #   CTRL+TAB - cycles thru tabs
        #   SHIFT+CTRL+TAB - previous tab
        #   ALT+K - select tab using mnemonic (K = underlined letter)
        nb.enable_traversal()
 
        nb.pack(fill=BOTH, expand=Y, padx=2, pady=3)
        self._create_descrip_tab(nb)
        self._create_text_tab(nb, "Hint")
        self._create_answer_panel()

    def helloCallBack(self):
        return; 

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
 
    def _create_descrip_tab(self, nb):
        # frame to hold contentx
        frame = Frame(nb, name='descrip')
 
        # widgets to be displayed on 'Description' tab
        msg = ["dniakmndamndoadmnkasndkasdnkasdnkaeswdnkadnkasndkasndkasndkasdnkadnkasdnkadnaskn"]
 
        lbl = Label(frame, wraplength='4i', justify=LEFT, anchor=N,
                        text=''.join(msg))
 
        # position and set resize behaviour
        lbl.grid(row=0, column=0, columnspan=2, sticky='new', pady=5)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0,1), weight=1, uniform=1)
 
        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text='Question', underline=0, padding=2)
 
 
    # =============================================================================
    def _create_text_tab(self, nb, s):
        # populate the third frame with a text widget
        frame = Frame(nb)
 
        txt = Text(frame, wrap=WORD, width=60, height=40)
        vscroll = Scrollbar(frame, orient=VERTICAL, command=txt.yview)
        txt['yscroll'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        txt.pack(fill=BOTH, expand=Y)
 
        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text=s, underline=0)
 
 
if __name__ == '__main__':
    NotebookDemo().mainloop()
