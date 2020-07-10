import ctypes

def make_msg_box_popup():
    # create msg_box
    MessageBox = ctypes.windll.user32.MessageBoxW
    
    title = 'If this message box appears, the program has worked'
    msg = 'This works fine when running as a .py file and when built with pyinstaller in Python 3.7, but when trying to run this on another compute after building with pyinstaller, an error will occur before this box can appear'
    
    # show the msg_box
    type_num = None
    MessageBox(None, msg, title, type_num)


