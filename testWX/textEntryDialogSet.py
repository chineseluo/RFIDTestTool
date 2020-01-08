import wx
#文本输入对话框
class TextEntryDialogSet(wx.Frame):
    def __init__(self,parent=None,id=-1):
        wx.Frame.__init__(self,parent,id,"RFIDtest",size=(800,600))
        myPanel = wx.Panel(self)
        myPanel.SetBackgroundColour("red")
        tedig = wx.TextEntryDialog(None,"你的名字是？","name","tony")
        tedig.SetValue("hahaha,你的设置没得用的")
        if tedig.ShowModal() == wx.ID_OK:
            response = tedig.GetValue()
            tedig.SetValue("hahaha,你的设置没得用的")
            print(response)
            tedig.Destroy()

class MyApp(wx.App):
    def OnInit(self):
        self.textEntryDialogSet = TextEntryDialogSet()
        self.textEntryDialogSet.Show(True)
        self.SetTopWindow(self.textEntryDialogSet)
        return True


if __name__ == "__main__":
    myApp = MyApp()
    myApp.MainLoop()
