from avatar import ShapedFrame
import wx

if __name__ == '__main__':
    app = wx.App()
    display = wx.Display(0)  # Main display
    client_rect = display.ClientArea #Visible area
    
    frame = ShapedFrame()
    w, h = frame.GetSize()
    newPos =  wx.Point(client_rect.width - w, client_rect.height - h)

    frame.Show()
    frame.Move(newPos)
    app.MainLoop()
