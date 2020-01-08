import wx

class Frame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title="hello,student"):
        #显示图像
        temp = image.ConvertToBitmap()
        #通过获取图片的长和宽，来进行设置Frame的长和宽
        size = (temp.GetWidth(),temp.GetHeight())
        wx.Frame.__init__(self,parent,id,title,pos,size)
        #将图像转化为位图
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

class MyApp(wx.App):
    def OnInit(self):
        #图像处理
        image = wx.Image("button.jpg",wx.BITMAP_TYPE_JPEG)
        self.myFrame = Frame(image)
        self.myFrame.Show(True)
        self.SetTopWindow(self.myFrame)
        return True
def main():
    myApp = MyApp(False)
    myApp.MainLoop()
if __name__ == "__main__":
    main()
