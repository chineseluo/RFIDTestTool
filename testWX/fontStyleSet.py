import wx
#设置字体类型

class FontStyleSet(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")


if __name__ == "__main__":
    app = wx.App(False)
    fontStyleSet = FontStyleSet()
    #将面板（panel）放入父窗口中
    myPanel = wx.Panel(fontStyleSet)
    fontStyleSetDemo = wx.StaticText(myPanel, -1,"hello word",(10,10),(80,15))
    #创建字体类型
    font = wx.Font(12,wx.DEFAULT,wx.ITALIC,wx.NORMAL,True)
    #设置字体
    fontStyleSetDemo.SetFont(font)

    fontStyleSet.Show(True)
    app.MainLoop()
