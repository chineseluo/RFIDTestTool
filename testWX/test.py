#coding:utf-8
import wx
from wx import xrc
class MyApp(wx.App):

    def OnInit(self):
        self.myFrame = MyFrame()
        #设置为应用程序的顶级窗口
        self.SetTopWindow(self.myFrame)
        #self.myFrame.show(False)使框架不可见
        #self.myFrame.Hide()等于self.myFrame.Show(False)
        self.myFrame.Show(True)
        return True

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
        self.myPanel = wx.Panel(self)

if __name__ == "__main__":
    #创建一个应用程序类实例
    app = MyApp(False)
    #进入应用程序主事件循环
    app.MainLoop()
