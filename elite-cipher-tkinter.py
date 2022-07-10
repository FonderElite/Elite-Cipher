from pprint import pprint
from tkinter import *
from turtle import width
from webbrowser import get
from PIL import ImageTk, Image
from operator import itemgetter
import base64
root = Tk()
root.title('Elite Cipher')
root.geometry("615x650")
root.resizable(True,True)

#Cipher Dictionary
encode_dict = {'a':'🙌','b':'👏','c':'👋','d':'👍','e':'👊','f':'✊','g':'✌️','h':'👌','i':'✋','j':'💪','k':'🙏','l':'☝️','m':'👆','n':'👇','o':'👈','p':'👉','q':'🖕','r':'🤘','s':'🖖','t':'🧏','u':'💅','v':'🤳','w':'🤞','x':'🤙','y':'🤛','z':'🤜',' ':' ',':':'🧠','/':'🦾','.':'🤟','0':'🥷','1':'🤺','2':'👩','3':'👑','4':'🥽','5':'😍','6':'🐶','7':'🐱','8':'🐭','9':'🐹'}
decode_dict  =  dict([item[::-1]for item in encode_dict.items()])
#Frame 
frame = Frame(
    root,
    bg="#1a1a1a",
    width=700,
    height=700
    )
frame.pack(expand=True, fill=BOTH)

#Icon - (You may change this)
ico = Image.open('D:\\Downloads\\Pictures\\elite.png')
photo_ico = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo_ico)

#Create a canvas
canvas= Canvas(frame, width= 1500, height= 1000,  scrollregion=(0,0,700,700))
canvas.configure(bg='#1a1a1a')
canvas.pack()

#Scrollbar 
horibar=Scrollbar(
    frame,
    orient=HORIZONTAL
    )
horibar.pack(side=BOTTOM,fill=X)
horibar.config(command=canvas.xview)

canvas.config(
    xscrollcommand=horibar.set, 
    )
canvas.pack(expand=True,side=LEFT,fill=BOTH)

#Open Image - (You may change this)
img= (Image.open("D:\\Downloads\\Pictures\\elite.png"))
  
#Resize the Image using resize method
resized_image= img.resize((140,90), Image.ANTIALIAS)
image_logo= ImageTk.PhotoImage(resized_image)

#Position Image
absolute_pos = Label(root, image=image_logo)
absolute_pos.image = image_logo
absolute_pos.config(bg="#1a1a1a")
absolute_pos.place(x=79,y=20)


# creating a label for name using widget Label
title_label = Label(root, text = 'Elite Cipher',  bg="#1a1a1a", fg="white",font=('courier new',25, 'bold'))
canvas.create_window(270, 50, window=title_label)
title_label.place(x=200,y=50)

# Base64 decode label
title_label = Label(root, text = 'Base64 Decoder',  bg="#1a1a1a", fg="white",font=('courier new',25, 'bold'))
canvas.create_window(270, 50, window=title_label)
title_label.place(x=870,y=50)

#Create Input for encoding text
enter_text = Entry(root,font=("courier new",20,"bold"),fg="#08ff08",bg="#1a1a1a",highlightbackground="#ffffff",highlightcolor="#ffffff",insertbackground='#08ff08')
canvas.create_window(280, 110, window=enter_text)
enter_text.insert(0,"Enter Text to Cipher here...")
enter_text.place(width=520,height=50,x=15, y= 120)

#Cipher text function
def elite_cipher(entry):
    if ciphered_text != '':
        ciphered_text.delete(1.0,END)
    output = ''
    for i in str(entry.get()):
        get_items = encode_dict.get(i)
        output+=str(get_items)
    output_bytes = output.encode('ascii')
    ciphered_text.insert(1.0,base64.b64encode(output_bytes))

def elite_decipher(entry):
  arr = []
  try:
    for i in entry.get():
        arr.append(decode_dict[i])
      #for v in decode_dict.keys():
      #    symbols+=[v]    
#[syms.append(x) for x in symbols if x not in syms]
    deciphered_text.insert(1.0,''.join(arr))
  except Exception as err:
    print(err)
          
          
    #Print key:value without , and []
    #print(*[str(v) for k,v in encode_dict.items()])
        

    
def base64_decode(entry):
    decoded = base64.b64decode(entry.get())
    decoded_text.insert(1.0,decoded)

# Ciphered Text Output goes here
ciphered_text = Text(root, height = 5, width = 52,fg="#08ff08",bg="#1a1a1a",highlightbackground="#ffffff",highlightcolor="#ffffff",insertbackground='#08ff08',font=("courier new", 15, "bold"))
ciphered_text.place(width=520,height=170,x=15,y=190)

#Encode Button
encode_button = Button(root,text='''
𝖤
𝖭
𝖢
𝖮
𝖣
𝖤
''',command=lambda: elite_cipher(enter_text),fg="#08ff08",bg='#1a1a1a',font=("default",19),highlightbackground="#ffffff",highlightcolor="#ffffff")
encode_button.place(x=540,y=120,width=50,height=240)


#Decipher Text Entry Widget
enter_text_to_decode = Entry(root,font=("courier new",20,"bold"),fg="#08ff08",bg="#1a1a1a",highlightbackground="#ffffff",insertbackground='#08ff08')
canvas.create_window(280, 110, window=enter_text_to_decode)
enter_text_to_decode.insert(0,"Enter Ciphered Text here...")
enter_text_to_decode.place(width=520,height=50,x=15, y= 380)

# Deciphered Text Output goes here
deciphered_text = Text(root, height = 5, width = 52,fg="#08ff08",bg="#1a1a1a",highlightbackground="#ffffff",highlightcolor="#ffffff",insertbackground='#08ff08',font=("courier new", 15, "bold"))
deciphered_text.place(width=520,height=170,x=15,y=450)

#Decode Button
decode_button = Button(root,text='''
𝖣
𝖤
𝖢
𝖮
𝖣
𝖤
''',command=lambda: elite_decipher(enter_text_to_decode),fg="#08ff08",bg='#1a1a1a',font=("default",19),highlightbackground="#ffffff",highlightcolor="#ffffff")
decode_button.place(x=540,y=380,width=50,height=240)

#Open Image - (You may change this)
b64_img= (Image.open("D:\\Downloads\\Pictures\\lock.png"))
  
#Resize the image using resize method
resized= b64_img.resize((90,80), Image.ANTIALIAS)
image2_logo= ImageTk.PhotoImage(resized)

#Position Image2
absolute_pos2 = Label(root, image=image2_logo)
absolute_pos2.image = image2_logo
absolute_pos2.config(bg="#1a1a1a")
absolute_pos2.place(x=770,y=20)

#Base64 decoder Input
base64_text_to_decode = Entry(root,font=("courier new",20,"bold"),fg="#08ff08",bg="#1a1a1a",highlightbackground="#ffffff",insertbackground='#08ff08')
canvas.create_window(280, 110, window=base64_text_to_decode)
base64_text_to_decode.insert(0,"        Enter Base64 text here...")
base64_text_to_decode.place(width=600,height=50,x=700, y= 115)

#Base64 Decoded Text Widget
decoded_text = Text(root, height = 5, width = 52,fg="#08ff08",bg="#1a1a1a",highlightbackground="#ffffff",highlightcolor="#ffffff",insertbackground='#08ff08',font=("courier new", 15, "bold"))
decoded_text.place(width=600,height=370,x=700,y=185)

#Base64 Decode Button
base64_decodebtn = Button(root,text="ＤＥＣＯＤＥ ＢＡＳＥ６４",command=lambda: base64_decode(base64_text_to_decode),fg="#08ff08", bg='#1a1a1a', font=("default",19),highlightbackground='#ffffff',highlightcolor='#ffffff')
base64_decodebtn.place(width=600,height=50,x=700, y= 570)



if __name__ == "__main__":
    root.mainloop()
