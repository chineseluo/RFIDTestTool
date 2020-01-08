import wx

#文本输入对话框
class ListTextEntryDialogSet(wx.Frame):
    def __init__(self,parent=None,id=-1):
        wx.Frame.__init__(self,parent,id,"RFIDtest",size=(800,600))
        myPanel = wx.Panel(self)
        myPanel.SetBackgroundColour("red")
        #wx.SingleChoiceDialog的参数类似于文本输入对话框，只是以字符串的列表代替了默认的字符串文本。要得到所选择的结果有两种方法，GetSelection()方法返回用户选项的索引，而GetStringSelection()返回实际所选的字符串。
        lteDig = wx.SingleChoiceDialog(myPanel,"请选择RFID性能测试版本","RFID版本选择",["V1.0","v1.1","V1.2"])
        if lteDig.ShowModal() == wx.ID_OK:
            result = lteDig.GetStringSelection()
            myPanel.SetBackgroundColour("blue")
            print(result)

class MyApp(wx.App):
    def OnInit(self):
        self.listTextEntryDialogSet = ListTextEntryDialogSet()
        self.listTextEntryDialogSet.Show(True)
        self.SetTopWindow(self.listTextEntryDialogSet)
        return True


if __name__ == "__main__":
    myApp = MyApp()
    myApp.MainLoop()
