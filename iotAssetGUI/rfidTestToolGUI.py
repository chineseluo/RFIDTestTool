#coding:utf-8

import wx
from base import testMain


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
        self.panelIndex = None
        #初始化菜单栏
        self.initMenuBar()
        #初始化状态栏
        self.initStatusBar()
        #分割窗口
        self.splitWindow()
        #初始化左侧侧边栏
        self.initSideMarkerBar()
        #初始化右边栏
        self.init_index_panel()

    #分割窗口
    def splitWindow(self):
        self.ParentWindow=wx.SplitterWindow(self) #创建分割窗口
        self.lpanel=wx.Panel(self.ParentWindow) #创建左面板
        self.rpanel=wx.Panel(self.ParentWindow) #创建右面板
        self.lpanel.SetBackgroundColour('#949449')
        #self.rpanel.SetBackgroundColour(colour='RED')
        self.ParentWindow.SplitVertically(self.lpanel,self.rpanel,200)
        self.ParentWindow.SetMinimumPaneSize(100) #设定最小的窗口不能小于100
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)
    
    #初始化进入RFID性能测试工具测试面板
    def init_index_panel(self):
        self.panelIndex = wx.Panel(self.rpanel,-1)
        indexBox = wx.StaticBox(self.panelIndex,-1,"loginPage",size = (400,400))
        indexVbox = wx.StaticBoxSizer(indexBox,wx.VERTICAL)
        welcomeHbox = wx.BoxSizer(wx.HORIZONTAL)
        versionHbox = wx.BoxSizer(wx.HORIZONTAL)
        authorHbox = wx.BoxSizer(wx.HORIZONTAL)
        welcomeStaticText = wx.StaticText(self.panelIndex,-1,"欢迎使用RFID性能测试工具")
        authorStaticText = wx.StaticText(self.panelIndex,-1,"author:chineseluo")
        versionStaticText = wx.StaticText(self.panelIndex,-1,"version:1.0")
        welcomeHbox.Add(welcomeStaticText)
        authorHbox.Add(authorStaticText)
        versionHbox.Add(versionStaticText)
        indexVbox.Add(welcomeHbox,proportion=0,flag = wx.CENTER,border = 1)
        indexVbox.Add(authorHbox,proportion=0,flag = wx.CENTER,border = 1)
        indexVbox.Add(versionHbox,proportion=0,flag = wx.CENTER,border = 1)
        self.panelIndex.SetSizer(indexVbox)
        main_sizer= wx.BoxSizer()
        main_sizer.Add(self.panelIndex,flag=wx.EXPAND,proportion=1)
        self.rpanel.SetSizer(main_sizer)
        self.rpanel.Layout()
        print("数据面板初始化结束")

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
        hbox.Add(text_model,flag=wx.ALIGN_LEFT,proportion=1)
        hbox.Add(modelContent,flag=wx.ALIGN_LEFT,proportion=1)
        vbox.Add(hbox,0,wx.ALL,5)
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
        #self.rpanel.Layout()
        print(self.rpanel.GetClientSize().width)
        print(self.rpanel.GetClientSize().height)
        self.panel_moniPkgTest = wx.Panel(self.rpanel,-1)
        #设置纵向布局管理器Sizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #设置横向布局管理器
        label_type_hbox = wx.BoxSizer(wx.HORIZONTAL)
        label_type_text_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.label_type_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.label_type_content.SetFocus()
        self.base_Attr_Model(label_type_hbox, vbox, label_type_text_model, self.label_type_content, "label_type：")
        
        shop_id_hbox = wx.BoxSizer(wx.HORIZONTAL)
        shop_id_text_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.shop_id_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(shop_id_hbox, vbox, shop_id_text_model, self.shop_id_content, "shop_id：")

        module_id_range_hbox = wx.BoxSizer(wx.HORIZONTAL)
        module_id_range_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.module_id_range_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(module_id_range_hbox, vbox, module_id_range_model, self.module_id_range_content, "module_id_range：")
        
        tmn_sn_range_hbox = wx.BoxSizer(wx.HORIZONTAL)
        tmn_sn_range_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.tmn_sn_range_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(tmn_sn_range_hbox, vbox, tmn_sn_range_model, self.tmn_sn_range_content, "tmn_sn_range：")
        
        current_value_range_hbox = wx.BoxSizer(wx.HORIZONTAL)
        current_value_range_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.current_value_range_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(current_value_range_hbox, vbox, current_value_range_model, self.current_value_range_content, "current_value_range：")
        
        status_tuple_hbox = wx.BoxSizer(wx.HORIZONTAL)
        status_tuple_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.status_tuple_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(status_tuple_hbox, vbox, status_tuple_model, self.status_tuple_content, "status_tuple：")
        
        ip_hbox = wx.BoxSizer(wx.HORIZONTAL)
        ip_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.ip_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(ip_hbox, vbox, ip_model, self.ip_content, "ip：")
        
        port_hbox = wx.BoxSizer(wx.HORIZONTAL)
        port_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.port_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(port_hbox, vbox, port_model, self.port_content, "port：")
        
        send_interval_hbox = wx.BoxSizer(wx.HORIZONTAL)
        send_interval_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.send_interval_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_CENTER|wx.EXPAND)
        self.base_Attr_Model(send_interval_hbox, vbox, send_interval_model, self.send_interval_content, "send_interval：")
        
        monitor_interval_hbox = wx.BoxSizer(wx.HORIZONTAL)
        monitor_interval_model = wx.StaticText(self.panel_moniPkgTest,-1)
        self.monitor_interval_content = wx.TextCtrl(self.panel_moniPkgTest,-1,style = wx.TE_RIGHT|wx.EXPAND)
        self.base_Attr_Model(monitor_interval_hbox, vbox, monitor_interval_model, self.monitor_interval_content, "monitor_interval：")
         
         
        #button按钮设置
        button_hbox = wx.BoxSizer()
        self.startButton = wx.Button(self.panel_moniPkgTest,label = "开始测试")
        self.endButton = wx.Button(self.panel_moniPkgTest,label = "结束测试")
        button_hbox.Add(self.startButton,proportion=0,flag=wx.RIGHT,border=5)
        button_hbox.Add(self.endButton,proportion=0,flag=wx.RIGHT,border=5)
        vbox.Add(button_hbox,proportion=0,flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)
        self.Bind(wx.EVT_BUTTON,self.startTest,self.startButton)
        self.panel_moniPkgTest.SetSizer(vbox)
        
        main_sizer= wx.BoxSizer()
        main_sizer.Add(self.panel_moniPkgTest,flag=wx.EXPAND,proportion=1)
        self.rpanel.SetSizer(main_sizer)
        self.rpanel.Layout()
        print("数据面板初始化结束")

    def startTest(self,evt):
        if evt.GetEventObject() == self.startButton:
            label_type = self.label_type_content.GetValue()
            shop_id = self.shop_id_content.GetValue()
            module_id_range = self.module_id_range_content.GetValue()
            tmn_sn_range = self.tmn_sn_range_content.GetValue()
            current_value_range = self.current_value_range_content.GetValue()
            status_tuple = self.status_tuple_content.GetValue()
            ip = self.ip_content.GetValue()
            port = self.port_content.GetValue()
            send_interval = self.send_interval_content.GetValue()
            monitor_interval = self.monitor_interval_content.GetValue()
            testMain(label_type, shop_id, module_id_range, tmn_sn_range, current_value_range, status_tuple, ip, port, send_interval, monitor_interval)
            print("label_type: {}, shop_id: {}, module_id_min: {}, module_id_max: {}, tmn_sn_min: {}, tmn_sn_max: {}, current_value_min: {}, current_value_max: {}, status_tuple: {}, ip: {}, port: {}, send_interval: {}, monitor_interval: {}".format(
            label_type,
            shop_id,
            module_id_range[0],
            module_id_range[1],
            tmn_sn_range[0],
            tmn_sn_range[1],
            current_value_range[0],
            current_value_range[1],
            status_tuple,
            ip,
            port,
            send_interval,
            monitor_interval))


    #左侧功能面板按钮事件
    def onClickEvent(self,event):
        print("test1")
        if event.GetEventObject() == self._inputTestDataBtn:
            if self.panel_testReport:
                if self.panelIndex is not None:
                    self.panelIndex.Destroy()
                    self.panelIndex=None
                else:
                    pass
                # print(self.panelIndex.Destroy())
                # print(self.panelIndex)
                self.panel_testReport.Destroy()
            if not self.panel_moniPkgTest:
                self.initMoniPkgTestPanel()

        if event.GetEventObject() == self._checkTestReportBtn:
            if self.panel_moniPkgTest:
                if self.panelIndex is not None:
                    self.panelIndex.Destroy()
                    self.panelIndex=None
                else:
                    pass

                self.panel_moniPkgTest.Destroy()
            if not self.panel_testReport:
                self.initTestReportPanel()
    

class MyApp(wx.App):
    def OnInit(self):
        self.rfidTestToolGui = RFIDTestToolGui()
        self.SetTopWindow(self.rfidTestToolGui)
        self.rfidTestToolGui.Show(True)
        return True
    
def guiMain():
    myApp = MyApp(False)
    myApp.MainLoop()
    
if __name__ == "__main__":
    guiMain()
