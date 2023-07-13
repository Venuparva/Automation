#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.LoginintoOutlook
import Outlookclient.Actions.LogoutfromOutlook
import Outlookclient.Actions.SendMailandCheckdelivery
import Outlookclient.PageElements.OutlookMainPageElements
import Outlookclient.Actions.CheckDelivery
import Outlookclient.Actions.ForwardMail
import Outlookclient.Actions.ChangeEnvironSwitch
import Outlookclient.Actions.openssl_events_check
from datetime import datetime


userName = password = newFolder = imap_list_cmd = Change_environ_result = existing_count = Copy_msgs_result = sourceCustomFolder = DestinationCustomFolder = Account_configure_result = Account_remove_result = Send_mail_result = Folder_selection_result = Search_Mail_result = Search_Mail_result = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = userName = password = searchHeader = searchText = Check_delivery_result = Forward_mail_result = Save_to_Sent_search_result = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
ForwardMail

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
    global Account_configure_result, Account_remove_result, Send_mail_result, Folder_selection_result, Search_Mail_result, from_addr, to_addr, cc_addr, bcc_addr, subject, folder, body_of_mail, attachment_file_path, userName, password, searchHeader, searchText, Check_delivery_result, Delete_msgs_result, Delete_folder_result, draft_subject, Copy_msgs_result, cleanupFolder, imap_list_cmd,Clean_up_account_result,draft_sub_time,existing_count,Forward_mail_result
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "to_addr" in str(params):
        to_addr = params['to_addr']
        logNote("User provided To Addr:", str(to_addr))
    if "subj" in str(params):
        subject = params['subj']
        orig_subject = subject
    # -------Select the destination folder first---------
    Search_Mail_result = Outlookclient.PageElements.OutlookMainPageElements.select_folder_element("INBOX")
    if "Success" in Search_Mail_result:
        logNote("\nwbt-report : Outlookclient - Folder_selection_result : pass")
    else:
        logNote("\nwbt-report : Outlookclient - Folder_selection_result : fail")
    # -------Search for mail after folder selection---------
    #subject = str(orig_subject) + ":Forwarded msg"
	logNote("\nBefore Check_delivery_result call subject:",str(subject))
    Check_delivery_result = Outlookclient.Actions.CheckDelivery.CheckdeliveryinFolder(subject)
    if "Success" in Check_delivery_result:
        logNote("\nReport: Outlookclient - Search Mail result : pass")
    else:
        logNote("\nReport: Outlookclient - Search Mail result : fail")
    logPass()  # This line is implicit and can be removed