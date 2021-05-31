import wx
from wx.core import NotifyEvent
from view.guiInterface import createFrame

class classCreateFrame(createFrame):
    def __init__(self, parent):
        createFrame.__init__(self, parent=None)
    
    def setProductName(self, productName):
        self.textProductName.SetValue(productName)
    
    def setUnitPrice(self, unitPrice):
        self.textUnitPrice.SetValue(str(unitPrice))
    
    def setCategory(self, category):
        self.textCategory.SetValue(str(category))