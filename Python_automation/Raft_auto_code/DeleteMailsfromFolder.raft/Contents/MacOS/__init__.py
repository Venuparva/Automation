#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient
from Outlookclient import *
import Outlookclient.Actions.DeleteMails
import Outlookclient.Actions.ChangeEnvironSwitch
import Outlookclient.Actions.openssl_events_check_outlook
from datetime import datetime


userName = password = newFolder = expected_output = trash_flag = flag_folder = flag_count = read_count = imap_list_cmd = Account_configure_result = Delete_msgs_result = Account_remove_result = Change_environ_result = existing_count = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
DeleteMailsfromFolder

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
    global userName, password, flag_folder,flag_count,read_count,newFolder,expected_output,trash_flag,imap_list_cmd,Change_environ_result,environ,Account_configure_result,Account_remove_result,Delete_msgs_result,existing_count,from_addr,to_addr, cc_addr, bcc_addr, subject, body_of_mail
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params) or "from_addr" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "to_addr" in str(params):
        to_addr = params['to_addr']
        logNote("User provided To Addr:", str(to_addr))
    if "subj" in str(params):
        subject = params['subj']
        orig_subject = subject
    if "body" in str(params):
        body_of_mail = params['body']
        logNote("User provided folder text:", str(body_of_mail))
    if "folder" in str(params):
        folder = params['folder']
        flag_folder = folder
        logNote("User provided folder text:", str(folder))
    else:
        flag_folder = "Inbox"
    if "Count" in str(params):
        Count = params['Count']
        flag_count = read_count = Count
    # -----------------Delete single mail from INBOX---------------
    logNote("---------------------------")
    existing_count = Outlookclient.Actions.openssl_events_check_outlook.Exist_mailbox_msgs_count(userName, password,"Deleted Messages", "Delete") # To fetch existing msgs count before deletion from Trash
    logNote("existing_count-5:%s"%(str(existing_count)))
    if str(existing_count).isdigit:
        logNote(" Looks like existing_count is not null:%s"%(str(existing_count)))
    else:
        logNote(" Looks like existing_count is empty...set it to Zero:%s"%(str(existing_count)))
        existing_count = 0
    logNote("---------------------------")
    Delete_msgs_result = Outlookclient.Actions.DeleteMails.deleteMessages(folder, Count)
    logNote("---------------------------")
    if "Success" in Delete_msgs_result:
        imap_del_Msg_cmd = ''' '3 select "Deleted Messages"' | grep "EXISTS" | tail -1 | awk '{ print $2}' '''
        server_validation_result = server_side_events_validation(userName, password, imap_del_Msg_cmd, existing_count,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlookclient -Deleted Messages:(single mail from INBOX): server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nReport : Outlookclient - Delete_single Mail from INBOX result : pass")
        else:
            logNote("\nOutlookclient - Deleted Messages:(single mail from INBOX): server-side validation status : fail")
            logNote("\nReport : Outlookclient - Delete_single Mail from INBOX result : fail")
    else:
        logNote("\nReport : Outlookclient - Delete_single Mail from INBOX result-1 : fail")