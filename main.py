from tkinter import *
from subprocess import call

# Create 2 functions that call the Encoder and Decoder files when needed
def open_Encoder():
    call(["python", "Encoder.py"])

def open_Decoder():
    call(["python", "Decoder.py"])

window = Tk()
window.title("Hill Cipher")
window.geometry("1100x450")

canvas = Canvas(window,
                height=450,
                width=1100,
                highlightthickness=0)
# Left-side of the window
canvas.create_rectangle(0, 0, 450, 520, fill="#267DFF", outline="#267DFF")
# Right-side of the window
canvas.create_rectangle(450, 0, 1100, 520, fill="#FCFCFC", outline="#FCFCFC")
canvas.pack()

# Title
title_label = Label(window,
                    text="Mã hóa và giải mã mật mã Hill",
                    font=("Arial", 20, "bold"),
                    fg="white",  # Text color
                    bg="#267DFF")
title_label.place(x=18, y=50)
line = Canvas()
sub_title_label = Label(window,
                    text="Mã hoá Hill được phát minh bởi\nLester Hill năm 1929,là mật mã cổ\nđiển cho phép mã hoá hai, ba,hoặc\nnhiều hơn các ký tự tại cùng thời điểm.\nMã hoá Hill sử dụng hai lý thuyết\ntoán học cực kì quan trọng trong\nngành mật mã là Đại số tuyến tính\nvà Số học mô-đun.",
                    font=("Arial", 14, "bold"),
                    fg="white",  # Text color
                    bg="#267DFF",
                    justify="left")
sub_title_label.place(x=15, y=120)

# Encrypt
encrypt_label = Label(window,
                      text="Mã hóa",
                      font=("Arial", 30, "bold"),
                      fg="#26148f",  # Text color
                      bg="#FCFCFC")
encrypt_label.place(x=485, y=70)

    # User input msg
user_msg = Entry(window,
                 font=("Arial", 20),
                 bd=2)
user_msg.place(x=550, y=130)


def submit_msg():
    global code
    user_input_msg = user_msg.get()

    # Open the text.txt file and write the msg to the file (1)
    with open("text.txt", "w") as file:
        file.write(user_input_msg)
    # Call the Encoder.py file
    open_Encoder()
    # Open the text.txt file and read the code from the file (4)
    with open("text.txt", "r") as file:
        code.set("Mã hóa là: " + file.read())


submit_user_msg = Button(window,
                         text="Generate",
                         font=("Arial", 15),
                         command=submit_msg,
                         cursor="hand2",
                         bg="#267DFF",
                         fg="white",
                         activebackground="#2663ff",
                         activeforeground="white",
                         highlightthickness=2,
                         bd=0)
submit_user_msg.place(x=930, y=140)

code = StringVar()
encrypt_msg_output = Entry(window,
                           fg="red",
                           bg="#FCFCFC",
                           font=("Arial", 18),
                           bd=0,
                           textvariable=code,
                           width=800)
encrypt_msg_output.place(x=600, y=200)

# Decoder
decode_label = Label(window,
                     text="Giải mã",
                     font=("Arial", 30, "bold"),
                     fg="#26148f",  # Text color
                     bg="#FCFCFC")
decode_label.place(x=485, y=250)

    # User input msg
user_code = Entry(window,
                  font=("Arial", 20),
                  bd=2)
user_code.place(x=550, y=310)


def submit_code():
    global msg
    user_input_code = user_code.get()

    # Open the text.txt file and write the msg to the file (1)
    with open("text.txt", "w") as file:
        file.write(user_input_code)
    # Call the Encoder.py file
    open_Decoder()
    # Open the text.txt file and read the code from the file (4)
    with open("text.txt", "r") as file:
        msg.set("Giải mã là: " + file.read())


submit_user_code = Button(window,
                          text="Generate",
                          font=("Arial", 15),
                          command=submit_code,
                          cursor="hand2",
                          bg="#267DFF",
                          fg="white",
                          activebackground="#2663ff",
                          activeforeground="white",
                          highlightthickness=2,
                          bd=0)
submit_user_code.place(x=930, y=320)

msg = StringVar()
decode_code_output = Entry(window,
                           fg="red",
                           bg="#FCFCFC",
                           font=("Arial", 18),
                           bd=0,
                           textvariable=msg,
                           width=800)
decode_code_output.place(x=600, y=380)

window.mainloop()



