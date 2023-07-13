#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.CopyMails
import Outlookclient.Actions.CreateFolder
import Outlookclient.PageElements.OutlookMainPageElements
import Outlookclient.Actions.ChangeEnvironSwitch
import Outlookclient.Actions.openssl_events_check_outlook
from datetime import datetime


userName = password = newFolder = expected_output = trash_flag = imap_list_cmd = Account_configure_result = Account_remove_result = Change_environ_result = existing_count = Copy_msgs_result = sourceCustomFolder = DestinationCustomFolder = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = imap_copy_Msg_cmd = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
CopyMails

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

def server_side_events_validation(userName,pwd,imap_cmd,expected_output,trash_flag):
   global current_time
   #------------Check whether folder is created on server side----------------
   service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check_outlook.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
   if "Success" in str(service_side_event_check_result_status):
       return "Success"
   else:
      logNote("\nService_side_event_check_result_status failed-1...hence retry one more time:%s"%(str(service_side_event_check_result_status)))
      service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check_outlook.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
      if "Success" in str(service_side_event_check_result_status):
          return "Success"
      else:
         logNote("\ncreateFolder:service_side_event_check_result_status failed...some issue need to check manually", str(service_side_event_check_result_status))
         return "Failure"

def runTest(params):
    global userName, password, newFolder,expected_output,trash_flag,imap_list_cmd,Change_environ_result,environ,Account_configure_result,Account_remove_result,Delete_msgs_result,existing_count,sourceCustomFolder,DestinationCustomFolder,Copy_msgs_result, to_addr, cc_addr, bcc_addr, subject, folder, body_of_mail, attachment_file_path, userName, password, searchHeader, searchText, Check_delivery_result, Delete_msgs_result, Delete_folder_result, draft_subject, cleanupFolder,imap_copy_Msg_cmd
    if "sourceDefaultFolder" in str(params):
        sourceDefaultFolder = params['sourceDefaultFolder']
    if "sourceCustomFolder" in str(params):
        sourceCustomFolder = params['sourceCustomFolder']
    if "DestinationDefaultFolder" in str(params):
        DestinationDefaultFolder = params['DestinationDefaultFolder']
    if "DestinationCustomFolder" in str(params):
        DestinationCustomFolder = params['DestinationCustomFolder']
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "subj" in str(params):
        subject = params['subj']
        logNote("User provided attachment file path:", str(attachment_file_path))
    if "folder" in str(params):
        folder = params['folder']
        logNote("User provided folder text:", str(folder))
    else:
        folder = "Inbox"
    if "Count" in str(params):
        Count = params['Count']
    else:
        Count = 2 # Taken default value
    # ---CreateFolder----------
    folder_exists_result = Outlookclient.PageElements.OutlookMainPageElements.select_folder_element(DestinationCustomFolder)
    if "Success" in folder_exists_result:
        logNote("\nCreate_folder folder_already_exists_result : pass")
        logNote("\nReport : Outlookclient - Create_folder_result : pass")
    else:
        logNote("\nCreate_folder folder_already_exists_result : fail")
        Create_folder_result = Outlookclient.Actions.CreateFolder.createfolder(DestinationCustomFolder)
        if "Success" in Create_folder_result:
            logNote("\nCreate_folder before copy test : pass")
        else:
            logNote("\nCreate_folder before copy test : fail")
    # -----------------COPY multiple mails from between user Folders---------------
    existing_count = Outlookclient.Actions.openssl_events_check_outlook.Exist_mailbox_msgs_count(userName, password,DestinationCustomFolder, "Copy")
	# To fetch existing msgs count before deletion
    logNote("existing_count-3:%s"%(str(existing_count)))
    Copy_msgs_result = Outlookclient.Actions.CopyMails.copyMessages(sourceCustomFolder, DestinationCustomFolder, "1")
    logNote("---------------------------")
    imap_copy_Msg_cmd = ''' "3 select %s" | grep "EXISTS" | tail -1 | awk '{ print $2}' ''' % (DestinationCustomFolder)
    if "Success" in Copy_msgs_result:
        server_validation_result = server_side_events_validation(userName, password, imap_copy_Msg_cmd, existing_count,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlookclient -COPY Messages between user folders: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nReport: Outlookclient -Copy_msgs_result between User created folders : pass")
        else:
            logNote("\nOutlookclient -COPY Messages between user folders: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nReport: Outlookclient -Copy_msgs_result between User created folders : fail")
    else:
        logNote("\n Outlookclient - Copy_msgs_result between User created folders ...Check mail in JUNK folder as well: fail")
        Copy_msgs_result = Outlookclient.Actions.CopyMails.copyMessages("Junk", DestinationCustomFolder, "1")
        server_validation_result = server_side_events_validation(userName, password, imap_copy_Msg_cmd, existing_count,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlookclient -COPY Messages between user folders: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nReport: Outlookclient -Copy_msgs_result between User created folders : pass")
        else:
            logNote("\nOutlookclient -COPY Messages between user folders: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nReport: Outlookclient -Copy_msgs_result between User created folders : fail")