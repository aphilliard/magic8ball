import wx
import random
import sys

class MyFrame(wx.Frame): 
    
    def __init__(self): 
        
        wx.Frame.__init__(self, None, -1, "Magic 8 Ball",   
                size=(800, 800))  
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "Shake the Magic 8 Ball!")  
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)  
        self.button.SetDefault()
        self.button.SetPosition((300, 600))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        
        
    def OnEraseBackground(self, evt):
        
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("8ball.png")
        dc.DrawBitmap(bmp, 0, 0)
        

    def OnClick(self, event):
        
        answers = ("It is certain", "It is decidedly so", "Yes", "Reply hazy try again", "Ask again later", "Concentrate and ask again", "My reply is no", "Outlook not so good", "Very doubtful")
        
        self.button.SetLabel(random.choice(answers)) 
        

if __name__ == '__main__':  
    app = wx.App()  
    frame = MyFrame()  
    frame.Show()  
    app.MainLoop() 
