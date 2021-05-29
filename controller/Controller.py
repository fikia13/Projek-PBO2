from wx.core import EVT_PAINT, NotifyEvent
from view.loginFrame import *
from view.mainFrame import *
from view.notaFrame import *

class Controller():
    def __init__(self):
        self.jumlahItem = 0
        self.jumlahHarga = 0
        self.nama = ""
        self.meja = ""
        self.list = ""

        #class login
        self.loginView = classLoginFrame(parent=None)
        self.loginView.btnPesan.Bind(wx.EVT_BUTTON, self.onBtnPesan)

        #class mainFrame
        self.mainView = classMainFrame(parent=None)
        self.mainView.btnTambah.Bind(wx.EVT_BUTTON, self.onBtnTambah)
        self.mainView.listMakanan.Bind(wx.EVT_LIST_ITEM_SELECTED, self.handleSelectItem)
        self.mainView.btnKurang.Bind(wx.EVT_BUTTON, self.onBtnKurang)
        self.mainView.btnCek.Bind(wx.EVT_BUTTON, self.onBtnCek)
        self.mainView.selectedProduct = None
        self.mainView.btnBayar.Bind(wx.EVT_BUTTON, self.onBtnBayar)

        #class notaFrame
        self.notaView = clasNotaFrame(parent=None)


    #login
    def onBtnPesan(self, event):
        self.loginView.Destroy()
        self.nama = self.getUser()
        self.meja = self.getMeja()
        self.mainFrame()

    def getUser(self):
        nama = self.loginView.textNama.GetValue()
        return nama
    
    def getMeja(self):
        meja = self.loginView.textMeja.GetValue()
        return meja
    
    #main
    def onBtnTambah( self, event ):
        if self.mainView.selectedProduct == None : return
        ambil = self.mainView.selectedProduct
        hasil = self.mainView.listMakanan.GetItemText(item=int(ambil)-1, col=3)
        tambah = int(hasil) + 1 
        self.mainView.listMakanan.SetItem(int(ambil)-1, 3, str(tambah))

    def onBtnKurang( self, event ):
        if self.mainView.selectedProduct == None : return
        ambil = self.mainView.selectedProduct
        hasil = self.mainView.listMakanan.GetItemText(item=int(ambil)-1, col=3)
        tambah = int(hasil) - 1 
        if hasil == "0"  :
            self.mainView.listMakanan.SetItem(int(ambil)-1, 3, "0")
        else:
            self.mainView.listMakanan.SetItem(int(ambil)-1, 3, str(tambah))

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


    def onBtnBayar(self, event):
        self.toNotaFrame()
        self.notaView.textPembeli.SetValue(self.nama)
        self.notaView.textNoMeja.SetValue(self.meja)
        self.notaView.textItem.SetValue(str(self.jumlahItem))
        self.notaView.textHarga.SetValue(str(self.jumlahHarga))
        self.listNota()
    
    def listNota(self):
        for row in range(self.mainView.listMakanan.GetItemCount()):
            item = self.mainView.listMakanan.GetItemText(item=row, col=3)
            if item != "0":
                namaProduk = self.mainView.listMakanan.GetItemText(item=row, col=1)
                hargaProduk = self.mainView.listMakanan.GetItemText(item=row, col=2)
                jumlahProduk = self.mainView.listMakanan.GetItemText(item=row, col=3)
                self.list += namaProduk+" - "+hargaProduk+" - "+jumlahProduk+" x\n"
                self.notaView.textNota.SetValue(self.list)

    #================
    def main(self):
        self.loginView.Show()

    def mainFrame(self):
        self.mainView.Show()

    def toNotaFrame(self):
        self.notaView.Show()