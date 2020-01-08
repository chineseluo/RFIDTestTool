#coding:utf-8
import wx

#window = wx.Frame(None, -1, "Hello", pos = (10, 10), size = (300, 200), style = wxDEFAULT_FRAME_STYLE, name = "frame")
app = wx.App(False)
window = wx.Frame(None, -1, "Hello", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
window.Show(True)
app.MainLoop()
