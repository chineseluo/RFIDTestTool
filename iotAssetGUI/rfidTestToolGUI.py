#coding:utf-8

import wx
import base.main


class RFIDTestToolGui(wx.Frame):
    label_type = None
    shop_id = None
    module_id_range = None
    tmn_sn_range = None
    current_value_range = None
    status_tuple = None
    ip = None
    port = None
    send_interval = None
    monitor_interval = None

    def __init__(self,parent = None,id = -1,title ='RFID性能测试工具'):
        wx.Frame.__init__(self,parent,id,title,size=(800,600))
        self.panel_moniPkgTest = None
        self.panel_testReport = None
        #初始化菜单栏
        self.initMenuBar()
        #初始化状态栏
        self.initStatusBar()
        #分割窗口
        self.splitWindow()
        #初始化左侧侧边栏
        self.initSideMarkerBar()
        #初始化右边栏
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
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)


    #初始化菜单栏
    def initMenuBar(self):
        #创建菜单栏
        menuBar = wx.MenuBar()
        #创建文件菜单
        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, title="文件")
        #创建文件菜单项
        fileImportBarItem = wx.MenuItem(fileMenu,-1,"导入",kind=wx.ITEM_NORMAL)
        #将文件菜单项添加到文件菜单下
        fileMenu.AppendItem(fileImportBarItem)
        fileExportBarItem = wx.MenuItem(fileMenu,-1,"导出",kind=wx.ITEM_NORMAL)
        fileMenu.AppendItem(fileExportBarItem)
        closeBarItem = wx.MenuItem(fileMenu,wx.ID_CLOSE,"退出",kind=wx.ITEM_NORMAL)
        fileMenu.AppendItem(closeBarItem)
        helpMenu = wx.Menu()
        menuBar.Append(helpMenu,title="帮助")
        aboutBarItem = wx.MenuItem(helpMenu,wx.ID_ABOUT,"关于",kind=wx.ITEM_NORMAL)
        helpMenu.AppendItem(aboutBarItem)
        self.SetMenuBar(menuBar)
        
    #初始化状态栏
    def initStatusBar(self):
        statusBar = self.CreateStatusBar(number=2)
        #设置状态栏比例
        statusBar.SetStatusWidths([-1,-2])
        statusBar.SetStatusText("Run Start Test Work",0)

    #初始化侧边栏
    def initSideMarkerBar(self):
        self._backgroundImageIcon = wx.Image("RFID.jpg",wx.BITMAP_TYPE_ANY)
        self._backgroundImageIcon = self._backgroundImageIcon.Rescale(200,150) #改变图像大小
        wx.StaticBitmap(self.lpanel,-1,wx.BitmapFromImage( self._backgroundImageIcon))
        #设置测试数据输入按钮
        self._inputTestDataBtn = wx.Button(self.lpanel,-1,"测试数据面板",pos =(0,150),size=(200,30))
        self.Bind(wx.EVT_BUTTON,self.onClickEvent,self._inputTestDataBtn)
        #设置查看测试报告按钮
        self._checkTestReportBtn = wx.Button(self.lpanel,-1,"查看测试报告",pos = (0,180),size=(200,30))
        self.Bind(wx.EVT_BUTTON,self.onClickEvent,self._checkTestReportBtn)

    #横纵布局生成器
    def base_Attr_Model(self,hbox,vbox,text_model,modelContent,attrText):
        text_model.SetLabel(attrText)
        hbox.Add(text_model,proportion=0,flag=wx.LEFT)
        hbox.Add(modelContent,proportion=1,flag=wx.LEFT,border=5)
        vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)
        return vbox

    #初始化测试报告面板
    def initTestReportPanel(self):
        self.panel_testReport = wx.Panel(self.rpanel,-1,size=(self.rpanel.GetClientSize().width,self.rpanel.GetClientSize().height))
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)
        self.panel_testReport.SetBackgroundColour("blue")
        self.panel_testReport.Refresh()

    #初始化测试数据面板
    def initMoniPkgTestPanel(self):
        print("正在初始化测试数据面板")
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)
        self.panel_moniPkgTest = wx.Panel(self.rpanel,-1,size=(self.rpanel.GetClientSize().width,self.rpanel.GetClientSize().height))
        self.panel_moniPkgTest.SetBackgroundColour("green")
        #设置纵向布局管理器Sizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #设置横向布局管理器
        label_type_hbox = wx.BoxSizer(wx.HORIZONTAL)
        label_type_text_model = wx.StaticText(self.panel_moniPkgTest,-1,label="test")
        self.label_type_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT)
        label_type_hbox.Add(label_type_text_model,1,wx.ALIGN_LEFT|wx.EXPAND,1)
        label_type_hbox.Add(self.label_type_content,1,wx.ALIGN_LEFT|wx.EXPAND,1)
        vbox.Add(label_type_hbox)
        self.panel_moniPkgTest.SetSizer(vbox)
        #self.panel_moniPkgTest.Refresh()
        print("数据面板初始化结束")


    def startTest(self):
        pass

    #左侧功能面板按钮事件
    def onClickEvent(self,event):
        print("test1")
        if event.GetEventObject() == self._inputTestDataBtn:
            if self.panel_testReport:
                self.panel_testReport.Destroy()
            if not self.panel_moniPkgTest:
                self.initMoniPkgTestPanel()

        if event.GetEventObject() == self._checkTestReportBtn:
            if self.panel_moniPkgTest:
                self.panel_moniPkgTest.Destroy()
            if not self.panel_testReport:
                self.initTestReportPanel()
    

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
