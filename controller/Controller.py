from wx.core import CENTRE, EVT_PAINT, Event, NotifyEvent, OK
from view.loginFrame import *
from view.mainFrame import *
from view.notaFrame import *
from view.admFrame import * 
from view.createFrame import *

class Controller():
    def __init__(self):
        self.productModel=products.Product()
        self.jumlahItem = 0
        self.jumlahHarga = 0
        self.nama = ""
        self.meja = ""
        self.list = ""
        self.id = None
        self.selectedProduct = None

        #class login
        self.loginView = classLoginFrame(parent=None)
        self.loginView.btnPesan.Bind(wx.EVT_BUTTON, self.onBtnPesan)
        self.loginView.btnMasuk.Bind(wx.EVT_BUTTON, self.onBtnMasuk)

        #class mainFrame
        self.mainView = classMainFrame(parent=None)
        self.mainView.btnTambah.Bind(wx.EVT_BUTTON, self.onBtnTambah)
        self.mainView.listMakanan.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectItem)
        self.mainView.btnKurang.Bind(wx.EVT_BUTTON, self.onBtnKurang)
        self.mainView.btnCek.Bind(wx.EVT_BUTTON, self.onBtnCek)
        self.mainView.selectedProduct = None
        self.mainView.btnBayar.Disable()
        self.mainView.btnBayar.Bind(wx.EVT_BUTTON, self.onBtnBayar)


        #class notaFrame
        self.notaView = clasNotaFrame(parent=None)
        self.notaView.btnSelesai.Bind(wx.EVT_BUTTON, self.onBtnSelesai)

        #class admFrame
        self.admView = classAdmFrame(parent=None)
        self.admView.btnTambah1.Bind(wx.EVT_BUTTON, self.onBtnTambah1)
        self.admView.btnEdit.Bind(wx.EVT_BUTTON, self.onBtnEdit)
        self.admView.listData.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectItem1)
        self.admView.btnRefresh.Bind(wx.EVT_BUTTON, self.onBtnRefresh)
        self.admView.btnHapus.Bind(wx.EVT_BUTTON, self.onBtnHapus)
        self.admView.btnKeluar.Bind(wx.EVT_BUTTON, self.onBtnKeluar)

        #create frame
        self.createView = classCreateFrame(parent=None)
        self.createView.btnBatal.Bind(wx.EVT_BUTTON, self.onBtnBatal)
        self.createView.btnSimpan.Bind(wx.EVT_BUTTON, self.onBtnSimpan)

    #login
    def onBtnPesan(self, event):
        self.nama = self.getUser()
        self.meja = self.getMeja()
        if self.nama == '' or self.meja == '':
            wx.MessageBox('Tidak Bisa Masuk Form nya kosong ','Terjadi Kesalahan', wx.OK | wx.ICON_ERROR)
        else:
            self.loginView.Hide()
            self.mainFrame()

    def getUser(self):
        nama = self.loginView.textNama.GetValue()
        return nama
    
    def getMeja(self):
        meja = self.loginView.textMeja.GetValue()
        return meja
    
    def setFormKosong(self):
        self.loginView.textMeja.SetValue("")
        self.loginView.textNama.SetValue("")

    def onBtnMasuk(self, event):
        self.admView.Show()

    #main
    def onBtnTambah( self, event ):
        if self.mainView.selectedProduct == None : return
        ambil = self.mainView.selectedProduct
        hasil = self.mainView.listMakanan.GetItemText(item=int(ambil)-1, col=3)
        tambah = int(hasil) + 1 
        self.mainView.listMakanan.SetItem(int(ambil)-1, 3, str(tambah))
        self.mainView.btnBayar.Disable()

    def onBtnKurang( self, event ):
        if self.mainView.selectedProduct == None : return
        ambil = self.mainView.selectedProduct
        hasil = self.mainView.listMakanan.GetItemText(item=int(ambil)-1, col=3)
        tambah = int(hasil) - 1 
        if hasil == "0"  :
            self.mainView.listMakanan.SetItem(int(ambil)-1, 3, "0")
        else:
            self.mainView.listMakanan.SetItem(int(ambil)-1, 3, str(tambah))
        self.mainView.btnBayar.Disable()

    def handleSelectItem( self, event ):
        selectedId = event.GetItem().GetText()
        if not selectedId: return
        self.mainView.selectedProduct = selectedId


    def onBtnCek(self, event):
        self.jumlahItem = 0
        self.jumlahHarga = 0
        for row in range(self.mainView.listMakanan.GetItemCount()):
            item = self.mainView.listMakanan.GetItemText(item=row, col=3)
            self.jumlahItem += int(item)
            self.mainView.textItem.SetValue(str(self.jumlahItem))
        for row in range(self.mainView.listMakanan.GetItemCount()):
            item = self.mainView.listMakanan.GetItemText(item=row, col=3)
            harga = self.mainView.listMakanan.GetItemText(item=row, col=2)
            self.jumlahHarga += (int(item) * int(harga))
            self.mainView.textHarga.SetValue(str(self.jumlahHarga))
        self.mainView.btnBayar.Enable()

    def onBtnBayar(self, event):
        self.toNotaFrame()
        self.notaView.textPembeli.SetValue(self.nama)
        self.notaView.textNoMeja.SetValue(self.meja)
        self.notaView.textItem.SetValue(str(self.jumlahItem))
        self.notaView.textHarga.SetValue(str(self.jumlahHarga))
        self.listNota()
        self.mainView.Hide()
    
    def listNota(self):
        for row in range(self.mainView.listMakanan.GetItemCount()):
            item = self.mainView.listMakanan.GetItemText(item=row, col=3)
            if item != "0":
                namaProduk = self.mainView.listMakanan.GetItemText(item=row, col=1)
                hargaProduk = self.mainView.listMakanan.GetItemText(item=row, col=2)
                jumlahProduk = self.mainView.listMakanan.GetItemText(item=row, col=3)
                self.list += namaProduk+" - "+hargaProduk+" - "+jumlahProduk+" x\n"
                self.notaView.textNota.SetValue(self.list)

    #dialog Nota
    def onBtnSelesai(self, event):
        wx.MessageBox("Pesanan Sedang diproses, terima kasih dimohon menunggu","Informasi",wx.OK | wx.ICON_INFORMATION)
        self.notaView.Hide()
        self.loginView.Show(show=True)
        self.setFormKosong()

    #admin frame
    def onBtnTambah1(self, event):
        self.createView.Show()
    
    def onBtnEdit(self, event):
        if self.selectedProduct == None: return

        prod = self.productModel.find(self.selectedProduct, column='productID')
        self.createView.setProductName(prod[1])
        self.createView.setUnitPrice(prod[2])
        self.createView.setCategory(prod[3])
        self.id = self.selectedProduct
        self.createView.Show()
    
    def onBtnHapus(self, event):
        if self.selectedProduct == None: return
        r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()
        
        if r == wx.ID_YES:
            self.productModel.delete(value=self.selectedProduct, column='productID')
            wx.MessageDialog(None, 'Author has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()
    
    def handleSelectItem1(self, event):
        selectedId = event.GetItem().GetText()
        if not selectedId: return
        self.selectedProduct = selectedId
        print(selectedId)

    def onBtnRefresh(self, event):
        self.admView.listData.DeleteAllItems()
        authors = self.productModel.get(columns="*",orderByColumn='productID', orderByDirection='DESC')
        for rowIndex, row in enumerate(authors):
            self.admView.listData.InsertItem(rowIndex, row[0])
            for columnIndex, col in enumerate(self.admView.columns):
                self.admView.listData.SetItem(rowIndex, columnIndex, str(row[columnIndex]))

    #creteFrame


    def onBtnBatal(self, event):
        self.createView.Hide()
    
    def onBtnSimpan(self, event):
        product_name = self.createView.textProductName.GetValue()
        unit_price = self.createView.textUnitPrice.GetValue()
        category = self.createView.textCategory.GetValue()
        try:
            if self.id == None:
                result = self.productModel.insert(values=[product_name, int(unit_price), int(category)], columns=['productName', 'unitPrice', 'categoryID'])
            else:
                result = self.productModel.update(colValues={'productName': product_name, 'unitPrice': unit_price, 'categoryID': category}, identifierValue=self.id, identifierColumn='productID')

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            if self.id == None:
                wx.MessageDialog(None, 'New author successfully added.', 'Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()
                
            else:
                wx.MessageDialog(None, 'Author data has been updated.', 'Update Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()
                

    def onBtnKeluar(self, event):
        self.admView.Hide()

    #================
    def main(self):
        self.loginView.Show()

    def mainFrame(self):
        self.mainView.Show()

    def toNotaFrame(self):
        self.notaView.Show()
