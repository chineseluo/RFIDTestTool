#coding:utf-8
import wx
#设置多行文本框
class MultipleRowSet(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
        myPanel = wx.Panel(self)
        multipleRowText = wx.TextCtrl(myPanel, -1,
                                      "this is a multipleRowSet test!!!"
                                      "helle wxPython",pos = (10,10),size = (100,80),style=wx.TE_MULTILINE|wx.TE_CENTER)
        multipleRowText.SetBackgroundColour(("blue"))
        multipleRowText.SetFocus()

if __name__ == "__main__":
    app = wx.App(False)
    mulitipleRowSet = MultipleRowSet()

    mulitipleRowSet.Show(True)
    app.MainLoop()
