import wx
#消息对话框
class MessageDialogSet(wx.Frame):
    def __init__(self,parent=None,id=-1):
        wx.Frame.__init__(self,parent,id,"RFIDtest",size=(800,600))
        self.myPanel = wx.Panel(self)
        self.myPanel.SetBackgroundColour("green")
        self.dlg = wx.MessageDialog(self.myPanel, "消息对话框", "你是不是大帅哥？", style=wx.YES_NO|wx.ICON_QUESTION)
        #ShowModal()方法将对话框以模式框架的方式显示，这意味着在对话框关闭之前，应用程序中的别的窗口不能响应用户事件。ShowModal()方法的返回值是一个整数，对于wx.MessageDialog，返回值是下面常量之一： wx.ID_YES, wx.ID_NO, wx.ID_CANCEL, wx.ID_OK。
        result = self.dlg.ShowModal()
        print(result)
        self.dlg.Destroy()

class MyApp(wx.App):
    def OnInit(self):
        self.messageDialogSet = MessageDialogSet()
        self.messageDialogSet.Show(True)
        self.SetTopWindow(self.messageDialogSet)
        return True




if __name__ == "__main__":
    myApp = MyApp(False)
    myApp.MainLoop()
