import wx
import csv
import os

class RightClickList():
    def __init__(self):
        self.list = dict()
        with open('menu.txt') as csvfile:
            for row in csv.DictReader(csvfile, delimiter=";"):
                self.list.update({row['line']: row['command']}) 

class PopMenu(wx.Menu):

    def __init__(self, parent):
        rcl = RightClickList();
        super(PopMenu, self).__init__()

        self.parent = parent

        for x in rcl.list:
            popmenu = wx.MenuItem(self, wx.NewId(), x)
            self.Append(popmenu)
            self.Bind(wx.EVT_MENU, lambda event, command=rcl.list[x]: self.OnItemChosen(event, command), popmenu)

            
    def OnItemChosen(self, event, command):
        os.system(command)

        
#this code is left to use during debugging
#it shouldn't be imported to the main App
if __name__ == '__main__':
    rcl = RightClickMenu();
    for x in rcl.list:
        print(x, rcl.list[x]) 

