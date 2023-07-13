#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.SendMailtoSingleRecipientandCheckdelivery
import Outlookclient.Actions.SearchMailinFolder
import Outlookclient.Actions.Checkdelivery
import Outlookclient.Actions.SavetoSentCheck
import Outlookclient.Actions.ChangeEnvironSwitch
import Outlookclient.Actions.openssl_events_check_outlook
from datetime import datetime


userName = password = newFolder = imap_list_cmd = Change_environ_result = existing_count = Copy_msgs_result = sourceCustomFolder = DestinationCustomFolder = Account_configure_result = Account_remove_result = Send_mail_result = Folder_selection_result = Search_Mail_result = Search_Mail_result = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = userName = password = searchHeader = searchText = Check_delivery_result = Save_to_Sent_search_result = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
ReadMailBodyText

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
    global Account_configure_result, Account_remove_result, Send_mail_result, Folder_selection_result, Search_Mail_result, from_addr, to_addr, cc_addr, bcc_addr, subject, folder, body_of_mail, attachment_file_path, userName, password, searchHeader, searchText, Check_delivery_result, Delete_msgs_result, Delete_folder_result, draft_subject, Copy_msgs_result, cleanupFolder, imap_list_cmd,Clean_up_account_result,draft_sub_time,existing_count,Save_to_Sent_search_result
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
  	if "subj" in str(params):
        subject = params['subj']
        orig_subject = subject
	if "body" in str(params):
        body_of_mail = params['body']
        logNote("User provided body text:", str(body_of_mail))
	if "searchHeader" in str(params):
        searchHeader = params['searchHeader']
   	if "searchText" in str(params):
        searchText = params['searchText']
    if "folder" in str(params):
        folder = params['folder']
        flag_folder = folder
        logNote("User provided folder text:", str(folder))
    else:
        flag_folder = "Inbox"
    if "Count" in str(params):
        Count = params['Count']
        flag_count = read_count = Count
    Read_MailbodyText_result = Outlookclient.Actions.ReadMailBody.readMailBodyText("INBOX",searchHeader,subject)
    if "Success" in Read_MailbodyText_result:
        logNote("\nReport : Outlookclient -Read_MailbodyText_result : pass")
   	else:
        logNote("\nReport : Outlookclient - Read_MailbodyText_result : fail")