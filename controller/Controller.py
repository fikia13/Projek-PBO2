from wx.core import NotifyEvent
from view.loginFrame import *
from view.mainFrame import *

class Controller():
    def __init__(self):
        self.loginView = classLoginFrame(parent=None)
        self.loginView.btnPesan.Bind(wx.EVT_BUTTON, self.onBtnPesan)

        #super class mainFrame
        self.mainView = classMainFrame(parent=None)



    #login
    def onBtnPesan(self, event):
        self.loginView.Destroy()
        self.mainFrame()

    def main(self):
        self.loginView.Show()

    def mainFrame(self):
        self.mainView.Show()