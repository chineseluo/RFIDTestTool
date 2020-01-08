#coding:utf-8
import wx
#设置单行文本框

class SingleRowSet(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
        myPanel = wx.Panel(self)
        #姓名输入框
        nameLabel = wx.StaticText(myPanel,-1,"姓名",pos = (10,10))
        #输入文本框
        self.inputText = wx.TextCtrl(myPanel,-1,"",pos = (80,10), size = (150,-1))
        #设置焦点
        self.inputText.SetInsertionPoint(0)
        #密码输入框
        pwdLabel = wx.StaticText(myPanel,-1,"密码",pos = (10,50))
        self.pwdText = wx.TextCtrl(myPanel,-1,"",pos = (80,50),size = (150,-1),style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER,self.onLostFocus,self.pwdText)

        
    def onLostFocus(self,evt):
        print(self.inputText.GetValue())
        print(self.pwdText.GetValue())
        wx.MessageBox("%s,%s" % (self.inputText.GetValue(),self.pwdText.GetValue()),"姓名和密码")

if __name__ == "__main__":
    app = wx.App(False)
    singleRowSet = SingleRowSet()
    singleRowSet.Show(True)
    app.MainLoop()
