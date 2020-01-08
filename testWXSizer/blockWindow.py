import wx


class BlockWindow(wx.Panel):
    def __init__(self,parent,ID=-1,label="",pos=wx.DefaultPosition,size=(100,25)):
        print(parent)
        wx.Panel.__init__(self,parent,ID,pos,size,wx.RAISED_BORDER,label)
        self.label = label
        self.SetBackgroundColour("yellow")
        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT,self.OnPaint)


    def OnPaint(self,evt):
        sz = self.GetClientSize()
        dc = wx.PaintDC(self)
        w,h = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())
        dc.DrawText(self.label,(sz.width-2)/2,(sz.height-h)/2)



