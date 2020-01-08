import wx
#设置字体颜色
class FontColorSet(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")


if __name__ == "__main__":
    app = wx.App(False)
    fontColorSet = FontColorSet()
    #生成父窗口
    fontColorSet = FontColorSet()
    #将面板（panel）放入父窗口中
    myPanel = wx.Panel(fontColorSet)
    fontColorSetDemo = wx.StaticText(myPanel, -1,"hello word",(10,10),(80,15),wx.ALIGN_CENTER)
    #设置字体颜色
    fontColorSetDemo.SetForegroundColour("yellow")
    #设置静态文本背景色
    fontColorSetDemo.SetBackgroundColour("green")


    fontColorSet.Show(True)
    app.MainLoop()
