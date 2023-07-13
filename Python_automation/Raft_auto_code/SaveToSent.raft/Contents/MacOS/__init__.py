#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.SaveToSent
import Outlookclient.Actions.openssl_events_check
from datetime import datetime


userName = password = newFolder = imap_list_cmd = Change_environ_result = existing_count = Copy_msgs_result = sourceCustomFolder = DestinationCustomFolder = Account_configure_result = Account_remove_result = Send_mail_result = Folder_selection_result = Search_Mail_result = Search_Mail_result = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = userName = password = searchHeader = searchText = Check_delivery_result = Save_to_Sent_search_result = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
SaveToSent

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
   service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
   if "Success" in str(service_side_event_check_result_status):
       return "Success"
   else:
      logNote("\nService_side_event_check_result_status failed-1...hence retry one more time:%s"%(str(service_side_event_check_result_status)))
      service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
      if "Success" in str(service_side_event_check_result_status):
          return "Success"
      else:
         logNote("\ncreateFolder:service_side_event_check_result_status failed...some issue need to check manually", str(service_side_event_check_result_status))
         return "Failure"

def runTest(params):
    global Account_configure_result, Account_remove_result, Send_mail_result, Folder_selection_result, Search_Mail_result, from_addr, to_addr, cc_addr, bcc_addr, subject, folder, body_of_mail, attachment_file_path, userName, password, searchHeader, searchText, Check_delivery_result, Delete_msgs_result, Delete_folder_result, draft_subject, Copy_msgs_result, cleanupFolder, imap_list_cmd,Clean_up_account_result,draft_sub_time,existing_count,Save_to_Sent_search_result
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
        logNote("User provided From Addr:", str(from_addr))
    if "to_addr" in str(params):
        to_addr = params['to_addr']
        logNote("User provided To Addr:", str(to_addr))
    if "cc_addr" in str(params):
        cc_addr = params['cc_addr']
        logNote("User provided To Addr:", str(cc_addr))
    if "bcc_addr" in str(params):
        bcc_addr = params['bcc_addr']
        logNote("User provided To Addr:", str(bcc_addr))
    if "subj" in str(params):
        subject = params['subj']
        orig_subject = subject
    if "body" in str(params):
        body_of_mail = params['body']
        logNote("User provided folder text:", str(body_of_mail))
    if "attachment" in str(params):
        attachment_file_path = params['attachment']
        logNote("User provided attachment file path:", str(attachment_file_path))
    # -------Search for mail after folder selection---------
    Save_to_Sent_search_result = Outlookclient.Actions.SaveToSent.SavetoSentCheck(subject)
    if "Success" in Save_to_Sent_search_result:
        expected_output = "* SEARCH"
        imap_sent_Msg_cmd = ''' '3 select "Sent Messages"' '8 search text "%s"' | tail -10 | grep -A2 "* SEARCH" ''' % (str(subject))
        server_validation_result = server_side_events_validation(userName, password, imap_sent_Msg_cmd, expected_output,"False")
        logNote("\nOutlookclient -Save_to_sent- server-side validation result : %s" % (str(server_validation_result)))
        if "Success" in str(server_validation_result):
            logNote("\nReport: server-side validation status : pass")
            logNote("\nReport: Outlookclient - Save_to_Sent_search_result : pass")
        else:
            logNote("\nReport: server-side validation status : fail")
            logNote("\nReport: Outlookclient - Save_to_Sent_search_result : fail")
    else:
        logNote("\nReport: Outlookclient - Save_to_Sent_search_result : fail")