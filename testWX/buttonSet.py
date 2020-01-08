#coding:utf-8
import wx

class ButtonSet(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
        myPanel = wx.Panel(self)
        self.button = wx.Button(myPanel,-1,"确定",pos = (10,10))
        self.Bind(wx.EVT_BUTTON, self.onClick,self.button)
        #设置按钮为默认选中状态
        self.button.SetDefault()
        self.inputText = wx.TextCtrl(myPanel,-1,"",pos = (100,10),size = (1250,-1),style = wx.TE_PROCESS_ENTER)

    def onClick(self,evt):
        self.inputText.Value = "hello wxPython"

if __name__ == "__main__":
    app = wx.App(False)
    buttonSet = ButtonSet()

    buttonSet.Show(True)
    app.MainLoop()
