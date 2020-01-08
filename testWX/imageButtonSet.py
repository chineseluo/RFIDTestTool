#coding:utf-8
import wx
#图片按钮设置
class ImageButtonSet(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "RFID性能测试工具", pos = (10,10), size = (800,600),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
        myPanel = wx.Panel(self)
        buttonfImage = wx.Image("button.jpg",wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.button = wx.BitmapButton(myPanel,-1,buttonfImage,pos=(20,20),size=(120,60))
        self.Bind(wx.EVT_BUTTON,self.onClick,self.button)
        self.button.SetDefault()

    def onClick(self,evt):
        wx.MessageBox("hello wxpython","哈哈")




if __name__ == "__main__":
    app = wx.App(False)
    imageButtonSet = ImageButtonSet()

    imageButtonSet.Show(True)
    app.MainLoop()
