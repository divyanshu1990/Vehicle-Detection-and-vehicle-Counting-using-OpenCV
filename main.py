from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition system")



# first image
        img=Image.open(r"C:\Users\divya\OneDrive\Desktop\face recognition\image\stanford.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

# second image
        img1=Image.open(r"C:\Users\divya\OneDrive\Desktop\face recognition\image\stanford.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_1bl=Label(self.root,image=self.photoimg)
        f_1bl.place(x=400,y=0,width=500,height=130)

# third image
        img2=Image.open(r"C:\Users\divya\OneDrive\Desktop\face recognition\image\stanford.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_1bl=Label(self.root,image=self.photoimg)
        f_1bl.place(x=800,y=0,width=500,height=130)
       







if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()