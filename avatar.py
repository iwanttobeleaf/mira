import wx
from RightClickMenu import PopMenu
import sys, os
os.chdir(sys._MEIPASS) #UNCOMMENT TO BUILD


IMAGE_PATH = "image.png"

class ShapedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Shaped Window",
                style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER)
        self.hasShape = False
        self.delta = wx.Point(0,0)

        # Load the image
        image = wx.Image(IMAGE_PATH, wx.BITMAP_TYPE_PNG)
        image.ConvertAlphaToMask(128)
        self.bmp = wx.Bitmap(image)

        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)
        self.SetWindowShape()
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp) 
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.ToggleWindowStyle(wx.STAY_ON_TOP) # we stay on toppe
        
    def OnEraseBackground(self,evt=None):
        pass        
    def SetWindowShape(self, evt=None):
        r = wx.Region(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnDoubleClick(self, evt):
        if self.hasShape:
            self.SetShape(wx.Region())
            self.hasShape = False
        else:
            self.SetWindowShape()

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

    def OnExit(self, evt): 
        self.Close() #this was used OnRightUp to close wondow.
        # However I do not wish for my friend to be closed

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)
        print (self.delta)

    def OnRightUp(self, evt):
        self.PopupMenu(PopMenu(self), evt.GetPosition())

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()

#this code is left to use during debugging
#it shouldn't be imported to the main App
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
