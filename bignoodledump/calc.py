import wx

app = wx.App()

defaultstyle = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER \
               | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN

myStyle = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN


frame = wx.Frame(None, title="Calcul8r", style=myStyle, size=(400, 600))

frame.Show()

app.MainLoop()

