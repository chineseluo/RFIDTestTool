import wx

#静态文本框组件
class RFIDTestToolGui(wx.Frame):
    panel_moniPkgTest = None
    def __init__(self,parent = None,id = -1,title ='RFID性能测试工具'):
        wx.Frame.__init__(self,parent,id,title,size=(800,600))

        #初始化菜单栏
        #self.initMenuBar()
        #初始化状态栏
        #self.initStatusBar()
        #分割窗口
        self.splitWindow()
        #初始化左侧侧边栏
        #self.initSideMarkerBar()
        #初始化右边栏
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)
        #self.initMoniPkgTestPanel()

    #分割窗口

    def splitWindow(self):
        self.ParentWindow=wx.SplitterWindow(self) #创建分割窗口
        self.lpanel=wx.Panel(self.ParentWindow) #创建左面板
        self.rpanel=wx.Panel(self.ParentWindow) #创建右面板
        self.lpanel.SetBackgroundColour('#949449')
        self.rpanel.SetBackgroundColour(colour='RED')
        self.ParentWindow.SplitVertically(self.lpanel,self.rpanel,200)
        self.ParentWindow.SetMinimumPaneSize(100) #设定最小的窗口不能小于100
        self.rpanel.Refresh()
        #初始化测试数据面板

    def initMoniPkgTestPanel(self):
        print("正在初始化测试数据面板")
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)
        #panel_moniPkgTest = wx.Panel(self.rpanel,-1,size=(self.rpanel.GetClientSize().width,self.rpanel.GetClientSize().height))
        panel_moniPkgTest = wx.Panel(self.rpanel,-1,size=(200,30))
        panel_moniPkgTest.SetBackgroundColour("green")
        #设置纵向布局管理器Sizer
        # vbox = wx.BoxSizer(wx.VERTICAL)
        # #设置横向布局管理器
        # label_type_hbox = wx.BoxSizer(wx.HORIZONTAL)
        # label_type_text_model = wx.StaticText(panel_moniPkgTest,-1,label="test")
        # self.label_type_content = wx.TextCtrl(panel_moniPkgTest,-1,style = wx.TE_RIGHT)
        # label_type_hbox.Add(label_type_text_model,0,wx.ALIGN_LEFT|wx.EXPAND,1)
        # label_type_hbox.Add(self.label_type_content,0,wx.ALIGN_LEFT|wx.EXPAND,1)
        # vbox.Add(label_type_hbox)
        # panel_moniPkgTest.SetSizer(vbox)
        #self.panel_moniPkgTest.Refresh()
        print("数据面板初始化结束")



class MyApp(wx.App):
    def OnInit(self):
        self.rfidTestToolGui = RFIDTestToolGui()
        self.SetTopWindow(self.rfidTestToolGui)
        self.rfidTestToolGui.Show(True)
        return True

def main():
    myApp = MyApp(False)

    myApp.MainLoop()

if __name__ == "__main__":
    main()
