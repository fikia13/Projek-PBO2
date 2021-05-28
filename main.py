import wx
from loginFrame import classLoginFrame
class MainApp(wx.App):
    def OnInit(self):
        self.frame = classLoginFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
