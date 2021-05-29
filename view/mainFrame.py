import wx
from view.guiInterface import mainFrame
from models import products
from models import database

class classMainFrame(mainFrame):
    def __init__(self, parent):
        mainFrame.__init__(self,parent=None)
        self.productModel=products.Product()
        self.columns = ['No.','Nama Produk','Harga','Jumlah']
        self.selectedProduct = None
        self.initColom()
        self.initData()

    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listMakanan.InsertColumn(index, col)

    def initData(self):
            authors = self.productModel.get(columns="productName,productName, unitPrice",orderByColumn='productID', orderByDirection='DESC', limit=10)
            n = 1
            for rowIndex, row in enumerate(authors):
                self.listMakanan.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    print(rowIndex,columnIndex)
                    if columnIndex == 0:
                        self.listMakanan.SetItem(rowIndex, columnIndex, str(n))
                    elif columnIndex == 3:
                        self.listMakanan.SetItem(rowIndex, columnIndex, "0")
                    else:
                        self.listMakanan.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
                n += 1