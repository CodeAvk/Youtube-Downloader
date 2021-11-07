from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
from tkinter import filedialog # used for where to download our file
from pytube import YouTube # used download Youtube video

Folder_Name=""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        location_error.config(text=Folder_Name,fg="green")
    else:
        location_error.config(text="Please choose a Folder !!",fg="red")

def Download():
    global select
    choice=ydchoices.get()
    url=entry_url.get()


    if len(url) > 1:
       link_error.config(text="")
       yt=YouTube(url)
       if choice==choices[0]:
            select=yt.streams.filter(progressive=True).first()
       elif choice==choices[1]:
            select=yt.streams.filter(progressive=True,file_extension="mp4").last()
       elif choice==choices[2]:
            select=yt.streams.filter(only_audio=True).first()
       else:
           link_error.config(text="Paste link again !!",fg="red")

    select.download(Folder_Name)
    link_error.config(text="Download Completed")
    tmsg.showinfo("Download-Result",
                  f"Your Video/Audio is Reday Check your Folder")

root=Tk()
root.title("@Avk Youtube_Downloader")
root.wm_iconbitmap("Youtube.ico")
root.config(bg="gray3")
root.geometry("500x500+350+100")
root.resizable(False,False)
root.columnconfigure(0,weight=1) # used to set all content in Center


ytLabel=Label(root,text="Youtube Video Downloader",bg="gray3",fg="dark orange",font="BahnschriftSemiBold 20 bold",pady=15)
ytLabel.grid()


link_label=Label(root,text="Enter the URL of the video",bg="gray3",fg="dark orange",font="BahnschriftSemiBold 15 bold",pady=20)
link_label.grid()

# Entry
entry_url=StringVar()
link_entry=Entry(root,width=55 ,textvariable=entry_url)
link_entry.grid()

#Error Msg
link_error=Label(root,bg="gray3",fg="red",font="BahnschriftSemiBold 12 bold",pady=10)
link_error.grid()


# path
path_label=Label(root,text="Save the Video File",bg="gray3",fg="dark orange",font="BahnschriftSemiBold 12 bold",pady=10)
path_label.grid()

# save button
save_Button=Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
save_Button.grid()

# error msg
location_error=Label(root,text="Can't find path",bg="gray3",fg="red",font="BahnschriftSemiBold 12 bold",pady=10)
location_error.grid()

# quality
quality=Label(root,text="Select Quality",bg="gray3",fg="dark orange",font="BahnschriftSemiBold 12 bold",pady=10)
quality.grid()

#combo box

choices=["1080p","240p","mp3"]
ydchoices=ttk.Combobox(root,text="Quality",values=choices)
ydchoices.grid()

# download button
dwld_button=Button(root,text="Download",bg="red",fg="white",command=Download,)
dwld_button.grid()




# path=Label(root,text="Path",bg="gray3",fg="dark orange",font="BahnschriftSemiBold 10 bold")
# path.pack(anchor="nw",padx=25,pady=25)



root.mainloop()
