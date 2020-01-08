import wx

#静态文本框组件
class StaticTextTest(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")




if __name__ == "__main__":
    app = wx.App(False)
    #生成父窗口
    staticTextTest = StaticTextTest()
    #将面板（panel）放入父窗口中
    myPanel = wx.Panel(staticTextTest)
    staticTextDemo = wx.StaticText(myPanel, -1,"hello word",(10,10),(80,15))

    staticTextTest.Show()
    app.MainLoop()
