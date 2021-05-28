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

		self.m_textCtrl4 = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Meja  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl5, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.m_button4 = wx.Button( self.panelLogin, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


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
		self.m_button4.Bind( wx.EVT_BUTTON, self.btnPesan )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnLoginAdm )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnPesan( self, event ):
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
		self.listMakanan.SetMinSize( wx.Size( 540,380 ) )

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

		self.m_button9 = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.m_panel7, wx.ID_ANY, u"Kurang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button10, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jumlah Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer15.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Total Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer15.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button8 = wx.Button( self.m_panel7, wx.ID_ANY, u"Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button8.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_OTHER ) )
		bSizer15.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.m_panel7.SetSizer( bSizer13 )
		self.m_panel7.Layout()
		bSizer13.Fit( self.m_panel7 )
		bSizer12.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.listMakanan.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectItem )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleSelectItem( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer17.Add( self.m_staticText9, 0, wx.ALL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl3 = wx.ListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		self.m_listCtrl3.SetMinSize( wx.Size( 540,380 ) )

		fgSizer5.Add( self.m_listCtrl3, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer5, 1, wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel6, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


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

		self.m_listCtrl2 = wx.ListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		self.m_listCtrl2.SetMinSize( wx.Size( 540,380 ) )

		fgSizer4.Add( self.m_listCtrl2, 0, wx.ALL, 5 )


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


