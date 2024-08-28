import wx

class MainFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)
        
        self.makeTabs()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Working!")

    def makeTextArea(self, panel):
        self.input_text_area = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300, 200))
        self.output_text_area = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300, 200))
        
        self.btn_all = wx.Button(panel, label="> Todo >")
        self.btn_all.Bind(wx.EVT_BUTTON, lambda event: self.textTransformations(event, 0))

        self.btn_commas = wx.Button(panel, label="> Pasar a comas >")
        self.btn_commas.Bind(wx.EVT_BUTTON, lambda event: self.textTransformations(event, 1))

        self.btn_unique = wx.Button(panel, label="> Unico >")
        self.btn_unique.Bind(wx.EVT_BUTTON, lambda event: self.textTransformations(event, 2))

        vbox_buttons = wx.BoxSizer(wx.VERTICAL)
        vbox_buttons.Add(self.btn_all, flag=wx.ALL | wx.CENTER, border=10)
        vbox_buttons.Add(self.btn_commas, flag=wx.ALL | wx.CENTER, border=10)
        vbox_buttons.Add(self.btn_unique, flag=wx.ALL | wx.CENTER, border=10)
        
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(self.input_text_area, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 10 )
        vbox.Add(vbox_buttons, flag=wx.ALL | wx.EXPAND, border=10 )
        vbox.Add(self.output_text_area, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 10 )

        panel.SetSizer(vbox)
        return vbox

    def makeTabs(self):
        notebook = wx.Notebook(self)

        tab1 = wx.Panel(notebook)
        notebook.AddPage(tab1, "Listados")

        # vbox1 = wx.BoxSizer(wx.VERTICAL)
        # label1 = wx.StaticText(tab1, label="This is the first tab")
        # vbox1.Add(label1, flag=wx.ALL, border = 10)
        # tab1.SetSizer(vbox1)

        vbox1 = self.makeTextArea(tab1)

        tab2 = wx.Panel(notebook)
        notebook.AddPage(tab2, "Calendario de Cierre")

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        label2 = wx.StaticText(tab2, label="This is the second tab")
        vbox2.Add(label2, flag=wx.ALL, border = 10)
        tab2.SetSizer(vbox2)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        self.SetSizerAndFit(sizer)

        self.SetSize((400, 300))
        self.Centre()

    def textTransformations(self, event, flag:int):
        # Retrieve the text from the text area
        input_text = self.input_text_area.GetValue()
        output_text = ""
        match flag:
            case 0:
                output_text = self.uniques(self.linesToCommas(input_text), ',')
            case 1:
                output_text = self.linesToCommas(input_text)
            case 2:
                output_text = self.uniques(input_text, '\n')
        self.output_text_area.SetValue(output_text)
        self.clipboardOutput(output_text)
        wx.MessageBox(f"Se ha copiado el resultado a tu portapapeles", "Datos transformados", wx.OK | wx.ICON_INFORMATION)


    def linesToCommas(self, text:str):
        return text.replace("\n", ",")
    
    def uniques(self, text:str, separation:str):
        unique_values = set(text.split(separation))
        output = ""
        for unique in unique_values:
            output += unique + separation
        return output.strip(separation)

    def clipboardOutput(self, text):
        if wx.TheClipboard.Open():
            wx.TheClipboard.Clear()
            wx.TheClipboard.SetData(wx.TextDataObject(text))
            wx.TheClipboard.Close()

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None, title='SubcontrataLey Misc. Functions')
    frm.Show()
    app.MainLoop()