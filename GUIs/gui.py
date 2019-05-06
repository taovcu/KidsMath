import tkinter as tk
from tkinter import ttk 
from tkinter import *


class NotebookDemo(Frame):
 
    def __init__(self, isapp=True, name='notebookdemo'):
        Frame.__init__(self, name=name)
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

    def _create_answer_panel(self):
        ansPanel = Frame(self, name='answer')
        ansPanel.pack(side=LEFT, fill=BOTH, expand=Y)

        # create the notebook
        nb = ttk.Notebook(ansPanel, name='ansnotebook')

        nb.pack(fill=BOTH, expand=Y, padx=2, pady=3)
        self._create_text_tab(nb, "Check Answer")

 
    def _create_descrip_tab(self, nb):
        # frame to hold contentx
        frame = Frame(nb, name='descrip')
 
        # widgets to be displayed on 'Description' tab
        msg = [
            "Ttk is the new Tk themed widget set. One of the widgets ",
            "it includes is the notebook widget, which provides a set ",
            "of tabs that allow the selection of a group of panels, ",
            "each with distinct content. They are a feature of many ",
            "modern user interfaces. Not only can the tabs be selected ",
            "with the mouse, but they can also be switched between ",
            "using Ctrl+Tab when the notebook page heading itself is ",
            "selected. Note that the second tab is disabled, and cannot "
            "be selected.\n", "Message 2"]
 
        lbl = Label(frame, wraplength='4i', justify=LEFT, anchor=N,
                        text=''.join(msg))
 
        # position and set resize behaviour
        lbl.grid(row=0, column=0, columnspan=2, sticky='new', pady=5)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0,1), weight=1, uniform=1)
 
        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text='Question', underline=0, padding=2)
 
    def _say_neat(self, v):
        v.set('Yeah, I know...')
        self.update()
        self.after(500, v.set(''))
 
    # =============================================================================
    def _create_disabled_tab(self, nb):
        # Populate the second pane. Note that the content doesn't really matter
        frame = Frame(nb)
        nb.add(frame, text='Disabled', state='disabled')
 
    # =============================================================================
    def _create_text_tab(self, nb, s):
        # populate the third frame with a text widget
        frame = Frame(nb)
 
        txt = Text(frame, wrap=WORD, width=100, height=50)
        vscroll = Scrollbar(frame, orient=VERTICAL, command=txt.yview)
        txt['yscroll'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        txt.pack(fill=BOTH, expand=Y)
 
        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text=s, underline=0)
 
 
if __name__ == '__main__':
    NotebookDemo().mainloop()
