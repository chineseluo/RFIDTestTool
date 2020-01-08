#coding:utf-8

import wx
#单选按钮组件
class RadioButton(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
        myPanel = wx.Panel(self)
        radioFirst = wx.RadioButton(myPanel,-1,"红色",pos = (10,10))
        radioSecond = wx.RadioButton(myPanel,-1,"绿色",pos = (10,40))
        radioThird = wx.RadioButton(myPanel,-1,"黄色",pos = (10,80))
        #设置颜色和wx常量的对应关系
        self.colors = {"红色":wx.RED,"绿色":wx.GREEN,"黄色":wx.YELLOW}
        self.textColor = wx.TextCtrl(myPanel,-1,"",pos = (80,10))
        #注册radio事件
        for eachRadio in(radioFirst,radioSecond,radioThird):
            self.Bind(wx.EVT_RADIOBUTTON,self.onRadio,eachRadio)

    def onRadio(self,event):
        radioSelect = event.GetEventObject()#返回选中的radio
        str = radioSelect.GetLabel()
        #选择radio的背景颜色
        self.textColor.SetBackgroundColour(self.colors[str])
        self.textColor.SetFocus()


if __name__ == "__main__":
    app = wx.App(False)
    radioButton = RadioButton()

    radioButton.Show(True)
    app.MainLoop()
