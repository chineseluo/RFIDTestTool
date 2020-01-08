import wx
from testWXSizer.blockWindow import BlockWindow


labels = "one two three four five six seven eight nine".split()
class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"basic Grid Sizer")
        #创建GridSizer
        sizer = wx.GridSizer(rows=3,cols=3,hgap=5,vgap=5)
        for label in labels:
            bw = BlockWindow(self,label=label)
            sizer.Add(bw,0,0)#添加窗口部件到Sizer
        self.SetSizer(sizer)#把Sizer与框架关联起来
        self.Fit()


app = wx.PySimpleApp()
GridSizerFrame().Show(True)
app.MainLoop()
