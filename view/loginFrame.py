import wx
from wx.core import Frame
from view.guiInterface import loginFrame
# from mainFrame import classMainFrame
# from admFrame import classAdmFrame

class classLoginFrame(loginFrame):
    def __init__(self, parent):
        loginFrame.__init__(self,parent)
