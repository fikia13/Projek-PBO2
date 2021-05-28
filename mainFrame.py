import wx
import guiInterface
from models import products
from models import database

class classMainFrame(guiInterface.mainFrame):
    def __init__(self, parent):
        guiInterface.mainFrame.__init__(self,parent=None)
        self.productModel=products.Product()
        self.columns = ['Nama Produk','Harga']
        self.selectedProduct = None
        self.initColom()
        self.initData()

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listMakanan.InsertColumn(index, col)

    def initData(self):
            authors = self.productModel.get(columns="productName, unitPrice",orderByColumn='productID', orderByDirection='DESC', limit=10)
            for rowIndex, row in enumerate(authors):
                self.listMakanan.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    self.listMakanan.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
