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
        self.initMenuBar()
        self.initStatusBar()
        self.initSideMarkerBar()
    
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
        self.sideMarkBarPanel = wx.Panel(self,-1,pos=(0,0),size=(200,600))
        self._backgroundImageIcon = wx.Image("RFID.jpg",wx.BITMAP_TYPE_ANY)
        self._backgroundImageIcon = self._backgroundImageIcon.Rescale(200,150) #改变图像大小
        wx.StaticBitmap(self.sideMarkBarPanel,-1,wx.BitmapFromImage( self._backgroundImageIcon))
        #设置测试数据输入按钮
        self._inputTestDataBtn = wx.Button(self.sideMarkBarPanel,-1,u"测试数据面板",pos =(0,150),size=(200,30))
        self.Bind(wx.EVT_BUTTON,self.onClickEvent,self._inputTestDataBtn)
        #设置查看测试报告按钮
        self._checkTestReportBtn = wx.Button(self.sideMarkBarPanel,-1,"查看测试报告",pos = (0,180),size=(200,30))
        self.Bind(wx.EVT_BUTTON,self.onClickEvent,self._checkTestReportBtn)
        self.panel_moniPkgTest = wx.Panel(self,-1,pos=(200,0),size=(600,520))
        self.panel_moniPkgTest.SetBackgroundColour("yellow")

    #横纵布局生成器
    def base_Attr_Model(self,hbox,vbox,text_model,modelContent,attrText):
        text_model.SetLabel(attrText)
        hbox.Add(text_model,proportion=0,flag=wx.LEFT)
        hbox.Add(modelContent,proportion=1,flag=wx.LEFT,border=5)
        vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)
        return vbox

    #初始化测试报告面板
    def initTestReportPanel(self):
        self.panel_testReport = wx.Panel(self,-1,pos=(200,0),size=(600,520))
        self.panel_testReport.SetBackgroundColour("blue")
        self.panel_testReport.Refresh()

    #初始化测试数据面板
    def initMoniPkgTestPanel(self):
        self.panel_moniPkgTest = wx.Panel(self,-1,pos=(200,0),size=(600,520))
        print(self.panel_moniPkgTest)
        self.panel_moniPkgTest.SetBackgroundColour("green")
        self.panel_moniPkgTest.Refresh()
        #设置纵向布局管理器Sizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #设置横向布局管理器
        label_type_hbox = wx.BoxSizer()
        label_type_text_model = wx.StaticText(self.panel_moniPkgTest,-1,style = wx.ALIGN_LEFT)
        label_type_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.ALIGN_RIGHT,pos=(400,0))
        vbox = self.base_Attr_Model(label_type_hbox,vbox,label_type_text_model,label_type_content,"label-type:")

        # shop_id_hbox = wx.BoxSizer()
        # shop_id_text_model = wx.StaticText(self.panel_moniPkgTest,-1,style = wx.ALIGN_LEFT,pos=(0,20))
        # shop_id_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.ALIGN_RIGHT,pos=(400,30))
        # vbox,hbox,shop_id_content = self.base_Attr_Model(shop_id_hbox,vbox,shop_id_text_model,shop_id_content,"shop-id:")

        #操作按钮
        # button_hbox = wx.BoxSizer()
        # startButton = wx.Button(self.panel_moniPkgTest,label = "开始测试")
        # endButton = wx.Button(self.panel_moniPkgTest,label = "结束测试")
        # button_hbox.Add(startButton,proportion=0,flag=wx.RIGHT,border=5)
        # button_hbox.Add(endButton,proportion=0,flag=wx.RIGHT,border=5)
        # vbox.Add(button_hbox,proportion=0,flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)
        # startButton.Bind(wx.KeyEvent,self.startTest())

        self.panel_moniPkgTest.SetSizer(vbox)


    def startTest(self):
        pass


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
