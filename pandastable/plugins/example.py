#!/usr/bin/env python
"""
    DataExplore Application plugin example.
    Created Oct 2015
    Copyright (C) Damien Farrell

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 3
    of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from pandastable.plugin import Plugin
import tkinter
from tkinter import *
from tkinter.ttk import *

class ExamplePlugin(Plugin):
    """Template plugin for DataExmplore"""

    capabilities = ['gui']#,'uses_sidepane']
    requires = ['']
    menuentry = 'Example Plugin'
    gui_methods = {}
    about = 'This plugin is a template'

    def main(self, parent):
        if parent==None:
            return
        self.parent = parent
        self.parentframe = None
        self._doFrame()
        return

    def _doFrame(self):

        if 'uses_sidepane' in self.capabilities:
            self.mainwin = self.parent.createChildFrame()
        else:
            self.mainwin=Toplevel()
            self.mainwin.title('A DataExplore Plugin')
            self.mainwin.geometry('600x600+200+100')

        self.ID='Basic Plugin'
        #self._createMenuBar()
        methods = self._getmethods()
        methods = [m for m in methods if m[0] in self.gui_methods]
        #self._createButtons(methods)
        l=Label(self.mainwin, text='This is a template plugin')
        l.pack(side=TOP,fill=BOTH)
        self.mainwin.bind("<Destroy>", self.quit)
        return

    def _createButtons(self, methods):
        """Dynamically create buttons for supplied methods"""
        for m in methods:
            b=Button(self.mainwin,text=m[0],command=m[1])
            b.pack( side=TOP,fill=BOTH)
        return

    def _createMenuBar(self):
        """Create the menu bar for the application. """
        self.menu=Menu(self.mainwin)
        self.file_menu={ '01Quit':{'cmd':self.quit}}
        self.file_menu=self.create_pulldown(self.menu,self.file_menu)
        self.menu.add_cascade(label='File',menu=self.file_menu['var'])

        self.mainwin.config(menu=self.menu)
        return

    def quit(self, evt=None):
        """Override this to handle pane closing"""
        return