# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class loginFrame
###########################################################################

class loginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome page", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.Colour( 248, 248, 248 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.panelLogin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 0 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Selamat Datang Di KafeIjo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText11 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Silahkan Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer7.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textNama = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.textNama, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Meja  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.textMeja = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.textMeja, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.btnPesan = wx.Button( self.panelLogin, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnPesan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( bSizer4, 0, wx.ALIGN_CENTER, 0 )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Login Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer9.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6 = wx.Button( self.panelLogin, wx.ID_ANY, u"Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( bSizer9, 0, wx.ALL, 0 )


		self.panelLogin.SetSizer( bSizer10 )
		self.panelLogin.Layout()
		bSizer10.Fit( self.panelLogin )
		bSizer3.Add( self.panelLogin, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnPesan.Bind( wx.EVT_BUTTON, self.onBtnPesan )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnLoginAdm )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onBtnPesan( self, event ):
		event.Skip()

	def btnLoginAdm( self, event ):
		event.Skip()


###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Halaman Utama", pos = wx.DefaultPosition, size = wx.Size( 573,484 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Menu Makanan  Minuman UbiCafe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 15, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer14.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )


		bSizer13.Add( bSizer14, 0, wx.ALL|wx.EXPAND, 0 )

		self.m_notebook1 = wx.Notebook( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel8 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.listMakanan = wx.ListCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listMakanan.SetMinSize( wx.Size( 540,270 ) )

		fgSizer2.Add( self.listMakanan, 0, wx.ALL, 5 )


		self.m_panel8.SetSizer( fgSizer2 )
		self.m_panel8.Layout()
		fgSizer2.Fit( self.m_panel8 )
		self.m_notebook1.AddPage( self.m_panel8, u"Daftar Makanan", True )
		self.m_panel9 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tableMinuman = wx.grid.Grid( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableMinuman.CreateGrid( 5, 5 )
		self.tableMinuman.EnableEditing( True )
		self.tableMinuman.EnableGridLines( True )
		self.tableMinuman.EnableDragGridSize( False )
		self.tableMinuman.SetMargins( 0, 0 )

		# Columns
		self.tableMinuman.EnableDragColMove( False )
		self.tableMinuman.EnableDragColSize( True )
		self.tableMinuman.SetColLabelSize( 30 )
		self.tableMinuman.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableMinuman.EnableDragRowSize( True )
		self.tableMinuman.SetRowLabelSize( 80 )
		self.tableMinuman.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableMinuman.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.tableMinuman, 0, wx.ALL, 5 )


		self.m_panel9.SetSizer( fgSizer3 )
		self.m_panel9.Layout()
		fgSizer3.Fit( self.m_panel9 )
		self.m_notebook1.AddPage( self.m_panel9, u"Daftar Minuman", False )

		bSizer13.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnTambah = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnTambah.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer16.Add( self.btnTambah, 0, wx.ALL, 5 )

		self.btnKurang = wx.Button( self.m_panel7, wx.ID_ANY, u"Kurang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnKurang.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer16.Add( self.btnKurang, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jumlah Item :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		bSizer15.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textItem = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer15.Add( self.textItem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Total Harga :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		bSizer15.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textHarga = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.textHarga, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btnCek = wx.Button( self.m_panel7, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnCek.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REPORT_VIEW, wx.ART_OTHER ) )
		self.btnCek.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnCek.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		bSizer15.Add( self.btnCek, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0 )


		bSizer13.Add( bSizer15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.btnBayar = wx.Button( self.m_panel7, wx.ID_ANY, u"Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnBayar.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_OTHER ) )
		self.btnBayar.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnBayar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		bSizer22.Add( self.btnBayar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer13.Add( bSizer22, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.m_panel7.SetSizer( bSizer13 )
		self.m_panel7.Layout()
		bSizer13.Fit( self.m_panel7 )
		bSizer12.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.listMakanan.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectItem )
		self.btnTambah.Bind( wx.EVT_BUTTON, self.onBtnTambah )
		self.btnKurang.Bind( wx.EVT_BUTTON, self.onBtnKurang )
		self.btnCek.Bind( wx.EVT_BUTTON, self.onBtnCek )
		self.btnBayar.Bind( wx.EVT_BUTTON, self.onBtnBayar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleSelectItem( self, event ):
		event.Skip()

	def onBtnTambah( self, event ):
		event.Skip()

	def onBtnKurang( self, event ):
		event.Skip()

	def onBtnCek( self, event ):
		event.Skip()

	def onBtnBayar( self, event ):
		event.Skip()


###########################################################################
## Class notaFrame
###########################################################################

class notaFrame ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nota Pembelian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Pembeli", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer23.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textPembeli = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer23.Add( self.textPembeli, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"No. Meja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer23.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textNoMeja = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer23.Add( self.textNoMeja, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer23, 0, wx.ALL|wx.EXPAND, 0 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.textNota = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.textNota.SetMinSize( wx.Size( 540,270 ) )

		fgSizer5.Add( self.textNota, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer5, 1, wx.EXPAND, 5 )

		bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jumlah Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer231.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textItem = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer231.Add( self.textItem, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jumlah Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer231.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textHarga = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer231.Add( self.textHarga, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer231, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.btnSelesai = wx.Button( self.m_panel6, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.btnSelesai, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.m_panel6.SetSizer( bSizer17 )
		self.m_panel6.Layout()
		bSizer17.Fit( self.m_panel6 )
		bSizer16.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()
		bSizer16.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class adminFrame
###########################################################################

class adminFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button8 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer15, 0, wx.ALL|wx.EXPAND, 0 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer14.Add( fgSizer4, 0, wx.ALL|wx.EXPAND, 0 )


		self.m_panel5.SetSizer( bSizer14 )
		self.m_panel5.Layout()
		bSizer14.Fit( self.m_panel5 )
		bSizer11.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


