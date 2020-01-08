import wx


class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1):
        wx.Frame.__init__(self,parent,id,"RFIDtest",size=(800,600))
        myPanel = wx.Panel(self)
        myPanel.SetBackgroundColour("blue")
        #创建底部状态栏
        statusBar = self.CreateStatusBar()
        #创建工具栏
        toolBar = self.CreateToolBar()
        image = wx.Image("button.jpg",wx.BITMAP_TYPE_JPEG)
        temp = image.ConvertToBitmap()
        #给工具栏增加一个工具
        toolBar.AddSimpleTool(wx.NewId(),temp,"new","help me'new'")
        #准备显示工具栏
        toolBar.Realize()
        #创建菜单栏
        menuBar = wx.MenuBar()
        #创建菜单1
        menu1 = wx.Menu()
        #将菜单1添加到菜单栏中
        menuBar.Append(menu1,"第一个菜单")
        menu2 = wx.Menu()
        #创建两个主菜单2的菜单项
        menu2.Append(wx.NewId(),"菜单项目1","test1")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"菜单项目2","test2")
        menuBar.Append(menu2,"第二个菜单")#将菜单2添加到菜单栏
        self.SetMenuBar(menuBar)#在框架上加上菜单栏


class MyApp(wx.App):
    def OnInit(self):
        self.myFrame = Frame()
        self.myFrame.Show(True)
        self.SetTopWindow(self.myFrame)
        return True

def main():
    myApp = MyApp(False)
    myApp.MainLoop()


if __name__ == "__main__":
    main()
