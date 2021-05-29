import wx
from wx.core import NO
from view.guiInterface import notaFrame
from models import products
from models import database

class clasNotaFrame(notaFrame):
    def __init__(self, parent):
        notaFrame.__init__(self,parent=None)
        self.productModel=products.Product()

