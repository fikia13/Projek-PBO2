import wx
from wx.core import Frame
import guiInterface
from mainFrame import classMainFrame
from admFrame import classAdmFrame

class classLoginFrame(guiInterface.loginFrame):
    def __init__(self, parent):
        guiInterface.loginFrame.__init__(self,parent)
        # super().__init__(parent)

    def btnPesan(self, event):
        # self.coba = guiInterface.cobaFrame(parent=self)
        # self.panelLogin.Hide()
        frame = classMainFrame(parent=None)
        frame.Show()
        self.Hide()
    
    def btnLoginAdm(self, event):
        frame = classAdmFrame(parent=None)
        frame.Show()
        self.Hide()