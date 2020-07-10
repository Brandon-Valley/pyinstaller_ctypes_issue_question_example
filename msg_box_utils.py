# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox?redirectedfrom=MSDN
# https://stackoverflow.com/questions/27257018/python-messagebox-with-icons-using-ctypes-and-windll

 
import ctypes

# Needed to fix DLL issue with pyinstaller
ctypes.windll.kernel32.SetDllDirectoryW(None)



TYPE_NUM__OK                 = 0 
TYPE_NUM__OK_CANCEL          = 1 
TYPE_NUM__ABORT_RETRY_IGNORE = 2 
TYPE_NUM__YES_NO_CANCEL      = 3 
TYPE_NUM__YES_NO             = 4
TYPE_NUM__RETRY_CANCEL       = 5 
TYPE_NUM__CRITICAL_MSG_ICON  = 16
 
TYPE_NUM__STOP_ICON          = 0x10
TYPE_NUM__QUESTION_ICON      = 0x20
TYPE_NUM__EXLAIM_ICON        = 0x30
TYPE_NUM__INFO_ICON          = 0x40
 
ICON_KEY_TYPE_NUM_D = {
                        'stop'    : TYPE_NUM__STOP_ICON    ,
                        'question': TYPE_NUM__QUESTION_ICON,
                        'exclaim' : TYPE_NUM__EXLAIM_ICON  ,
                        'info'    : TYPE_NUM__INFO_ICON     
                      }
BTN_NUM_NAME_D = {
                   1 : 'ok'    , # also X for OK
                   2 : 'cancel', # also X for anything with CANCEL btn
                   3 : 'abort' ,
                   4 : 'retry' ,
                   5 : 'ignore',
                   6 : 'yes'   ,
                   7 : 'no'    
                 }
 
 
 
''' Internal '''
def root_msg_box(type_num, title, msg, icon, output_define_d, app_id):

     
     
    # add icon if given
    if icon != None:
        type_num = type_num | ICON_KEY_TYPE_NUM_D[icon]
     
    # sets tool bar icon to match parent's if any
    if app_id != None:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
     
     
    # create msg_box
    MessageBox = ctypes.windll.user32.MessageBoxW

    title = 'If this message box appears, the program has worked'
    msg = 'This works fine when running as a py file and when built with pyinstaller in Python 3.7, but when trying to run this on another computer, an error will occur before this box can appear'

    out_num = MessageBox(None, msg, title, type_num)
  
def msg_box__YES_NO             (title, msg, icon = None, output_define_d = None, app_id = None): return root_msg_box(TYPE_NUM__YES_NO             , title, msg, icon, output_define_d, app_id)        
        
         
         
 
if __name__ == '__main__':
    print('In Main:  msg_box_utils')

    app_id = None
    type_num = None

    # # add icon if given
    # if icon != None:
    #     type_num = type_num | ICON_KEY_TYPE_NUM_D[icon]
     
    # sets tool bar icon to match parent's if any
    if app_id != None:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
     
     
    # create msg_box
    MessageBox = ctypes.windll.user32.MessageBoxW

    title = 'If this message box appears, the program has worked'
    msg = 'This works fine when running as a py file and when built with pyinstaller in Python 3.7, but when trying to run this on another computer, an error will occur before this box can appear'

    out_num = MessageBox(None, msg, title, type_num)



     
    
     
     
     
#     title = 'test title'
#     msg = 'test msg'

     
#     icon = 'question'
     
# #     print(root_msg_box(type_num, title, msg, output_define_d))
#     print(msg_box__YES_NO(title, msg, icon ))
# #     print(msg_box__WARNING_MSG_ICON(title, msg, output_define_d))
     
     
     
     
     