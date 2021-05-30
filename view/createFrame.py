import wx
from wx.core import NotifyEvent
from view.guiInterface import createFrame

class classCreateFrame(createFrame):
    def __init__(self, parent):
        createFrame.__init__(self, parent=None)