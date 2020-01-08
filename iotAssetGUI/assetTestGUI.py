#coding:utf-8
import wx
import base.main

class IotAssetGUI(wx.Frame):

    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")

    def base_Attr_Model(self,hbox,vbox,text_model,modelContent,attrText):
        text_model.SetLabel(attrText)
        hbox.Add(text_model,proportion=0,flag=wx.LEFT)
        hbox.Add(modelContent,proportion=1,flag=wx.LEFT,border=5)
        vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)
        return vbox,hbox,modelContent

    def startTest(self):
        pass

if __name__=='__main__':

    #10个
    app = wx.App(False)
    #生成父窗口
    myMainFrame = IotAssetGUI()
    #生成面板，将面板添加到父窗口中
    myPanel = wx.Panel(myMainFrame)
    vbox = wx.BoxSizer(wx.VERTICAL)
    label_type_text_model = wx.StaticText(myPanel,-1,style = wx.ALIGN_LEFT)
    label_type_content = wx.TextCtrl(myPanel)
    label_type_hbox = wx.BoxSizer()
    vbox,hbox,label_type_content = myMainFrame.base_Attr_Model(label_type_hbox,vbox,label_type_text_model,label_type_content,"label-type:")

    shop_id_text_model = wx.StaticText(myPanel,-1,style = wx.ALIGN_LEFT)
    shop_id_hbox = wx.BoxSizer()
    shop_id_content = wx.TextCtrl(myPanel)
    vbox,hbox,shop_id_content = myMainFrame.base_Attr_Model(shop_id_hbox,vbox,shop_id_text_model,shop_id_content,"shop-id:")

    button_hbox = wx.BoxSizer()
    # #操作按钮
    startButton = wx.Button(myPanel,label = "开始测试")
    endButton = wx.Button(myPanel,label = "结束测试")
    button_hbox.Add(startButton,proportion=0,flag=wx.RIGHT,border=5)
    button_hbox.Add(endButton,proportion=0,flag=wx.RIGHT,border=5)
    vbox.Add(button_hbox,proportion=0,flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)

    #startButton.Bind(wx.KeyEvent,myMainFrame.startTest())

    myPanel.SetSizer(vbox)
    myMainFrame.Show()
    app.MainLoop()

