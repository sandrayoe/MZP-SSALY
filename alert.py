from tkinter import * 
from tkinter import messagebox 

#nanti main windownya di sini ya 
root = Tk() 
root.geometry("300x200") 
root.title("SSALY")

#show notificationnya, tapi belum ditambahin kondisi
messagebox.showwarning("Notification Message", "Stunting Alert")

#===================================
#Fungsi drop down listnya nanti 

#Fungsi show untuk menampilkan kebijakan
def show(): 
    label.config( text = 'Faktor paling berpengaruh ...' ) 
  
#Dropdown menu options 
#array-nya bisa dimodif, disesuaikan, ini cuma contoh list
options = [ 
    "Kalimantan", 
    "DKI Jakarta", 
    "Papua Barat", 
    "NTB"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
#initial menu text 
clicked.set( "Provinsi" ) 
  
#Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = Button( root , text = "Pilih" , command = show ).pack() 
  
# Create Label 
label = Label( root , text = " " ) 
label.pack() 
  
# Execute tkinter 
root.mainloop() 