#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.CheckDelivery
import Outlookclient.Actions.SendMailandCheckdelivery
import Outlookclient.Actions.openssl_events_check
from datetime import datetime


Account_configure_result = Account_remove_result = Send_mail_result = Folder_selection_result = Delete_folder_result = Search_Mail_result = newFolder = DestinationCustomFolder = DestinationDefaultFolder = Count = oldFolder = renameFolder = flag_count = read_folder = read_count = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = userName = password = searchHeader = searchText = Check_delivery_result = Save_to_Sent_search_result = Create_folder_result = Rename_folder_result = UnFlag_msgs_result = Flag_msgs_result = Save_To_Draft_result = Delete_msgs_before_copy_result = Forward_mail_result = Reply_mail_result = Delete_msgs_result = Read_MailbodyText_result = Copy_msgs_result = Read_msgs_result = UnRead_msgs_result = draft_subject = Change_environ_result = current_time = cleanupFolder = imap_list_cmd = Clean_up_account_result = imap_del_Msg_cmd = imap_copy_Msg_cmd = imap_flag_Msg_cmd = imap_read_Msg_cmd = draft_sub_time = existing_count = sourceCustomFolder= sourceDefaultFolder = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
SendMail

Contact: Owner
2018/12/20
"""

# This is a Raft test. For more information see http://raft.apple.com
testDescription  = ""                 # Add a brief description of test functionality
testVersion      = "0.1"              # Used to differentiate between results for different versions of the test
testState        = DevelopmentState   # Possible values: DevelopmentState, ProductionState

def get_current_time():
   global current_time
   today = datetime.now()
   current_time = today.strftime("%h%d%s")
   current_time = current_time[0:7] + current_time[11:16]
   return current_time

def runTest(params):
    global Account_configure_result, Account_remove_result, Send_mail_result, Folder_selection_result, Search_Mail_result, from_addr, to_addr, cc_addr, bcc_addr, subject, folder, body_of_mail, attachment_file_path, userName, password, searchHeader, searchText, Check_delivery_result, Delete_msgs_result, Delete_folder_result, draft_subject, Copy_msgs_result, cleanupFolder, imap_list_cmd,Clean_up_account_result,draft_sub_time,existing_count,imap_del_Msg_cmd,sourceCustomFolder,sourceDefaultFolder,newFolder,orig_subject,DestinationCustomFolder,DestinationDefaultFolder,Count,oldFolder,renameFolder,flag_count,read_folder,read_count
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "from_addr" in str(params):
        from_addr = params['from_addr']
        userName = params['from_addr']
        logNote("User provided From Addr:\n", str(from_addr))
    if "to_addr" in str(params):
        to_addr = params['to_addr']
        logNote("User provided To Addr:\n", str(to_addr))
    if "cc_addr" in str(params):
        cc_addr = params['cc_addr']
        logNote("User provided To Addr:\n", str(cc_addr))
    if "bcc_addr" in str(params):
        bcc_addr = params['bcc_addr']
        logNote("User provided To Addr:\n", str(bcc_addr))
    if "subj" in str(params):
        subject = params['subj']
        orig_subject = subject
    if "body" in str(params):
        body_of_mail = params['body']
        logNote("User provided folder text:\n", str(body_of_mail))
    if "attachment" in str(params):
        attachment_file_path = params['attachment']
        logNote("User provided attachment file path:", str(attachment_file_path))
    if "folder" in str(params):
        folder = params['folder']
        flag_folder = folder
        logNote("User provided folder text:\n", str(folder))
    else:
        flag_folder = "Inbox"
    if "Count" in str(params):
        Count = params['Count']
        flag_count = read_count = Count
    # -------Send mail to single User first---------
    #mail_app_broken_fix_result = Outlookclient.Actions.Interruption_windows_handler.mail_app_broken_window_fix()
    #logNote(" Final mail_app_broken_fix_result:",mail_app_broken_fix_result)
    #if "Success" in mail_app_broken_fix_result:
    #    logNote("Outlookclient - SendMail - Mail App interruption window result : pass")
    #else:
    #    logNote("Outlookclient - SendMail - Mail App interruption window result : fail")
    #logPass()  # This line is implicit and can be removed
    Send_mail_result = Outlookclient.Actions.SendMailandCheckdelivery.SendMailtoSingleUserfromOutlookandCheckdelivery(from_addr, to_addr, subject, body_of_mail, attachment_file_path)
    if "Success" in Send_mail_result:
        logNote("Report: Outlookclient - Send_mail_result result : pass")
    else:
        logNote("Report: Outlookclient - Send_mail_result : fail")
    logPass()  # This line is implicit and can be removed