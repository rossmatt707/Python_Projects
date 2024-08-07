import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")
        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # Crates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # Crates exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Positions exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    # Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    # Creates function to transfer files from one directory to the other
    def transferFiles(self):
        #Gets source dir
        source = self.source_dir.get()
        #Gets destination dir
        destination = self.destination_dir.get()
        # Gets current time
        now = datetime.now()
        # Gets time 24 hours ago
        day_ago = now - timedelta(hours=24)
        #Gets list of files in source dir
        source_files = os.listdir(source)     
        for file in source_files:
            # Gets file path
            file_path = os.path.join(source, file)
            # Gets mod time of file
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Checks  if the file was modified in past day
            if file_mod_time > day_ago:
                # Moves files from source to destination folder if they meet the criteria
                shutil.move(file_path, destination)
                print(file + ' was successfully transfered.')
 

    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinhter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

if __name__== "__main__":
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
