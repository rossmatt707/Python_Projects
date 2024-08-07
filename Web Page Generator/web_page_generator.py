import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        # Text above blank entry space
        self.label = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.label.grid(padx=(20,20), pady=(35,5),row = 0, column = 0, columnspan = 3, sticky=W)
        # Creates blank entry area for user to type
        self.enterText = Entry(width = 150)
        self.enterText.grid(padx=(20,20), pady=(10,10),row = 1, rowspan=1, column = 0, columnspan=3, sticky=W+E)
        # Creates and places Default HTML button
        self.btn_Default = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn_Default.grid(padx=(700, 0), pady=(0, 15), row=2,column=1, sticky=E)
        # Creates and places Submit custom text button
        self.btn_Custom = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.customHTML)
        self.btn_Custom.grid(padx=(10, 40), pady=(0, 15), row=2,column=2, sticky=E)
    #This creates the command function that acts when pressing the default HTML button
    #Opens new browser tab and places default text on website.
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #This creates the command function that acts when pressing the default custom text button
    #Opens new browser tab and places custom text on site.
    def customHTML(self):
        customText = self.enterText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
