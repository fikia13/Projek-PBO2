import wx
from view.guiInterface  import adminFrame
from models import database
from models import products
from view.createFrame import classCreateFrame

class classAdmFrame(adminFrame):
    def __init__(self, parent):
        adminFrame.__init__(self,parent=None)
        self.productModel=products.Product()
        self.columns = ['ID','Nama Produk','Harga','Category']
        self.selectedProduct = None
        self.initColom()
        self.initData()


    def initColom(self):
        for index, col in enumerate(self.columns):
            self.listData.InsertColumn(index, col)

    def initData(self):
            authors = self.productModel.get(columns="*",orderByColumn='productID', orderByDirection='DESC')
            for rowIndex, row in enumerate(authors):
                self.listData.InsertItem(rowIndex, row[0])
                for columnIndex, col in enumerate(self.columns):
                    self.listData.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
    
    def onBtnTambah1(self, event):
        self.Show()